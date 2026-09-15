import dspy  # noqa: E402
from litellm.llms.custom_httpx.llm_http_handler import BaseLLMHTTPHandler  # noqa: E402

OLLAMA_BASE = "http://172.31.143.202/ollama"
MODEL = "qwen3:8b"

# litellm's `ollama_chat` provider (what dspy.LM uses under this model
# prefix) sends its POST body via httpx's `content=` param -- a
# pre-serialized JSON string -- but never sets `Content-Type:
# application/json`. Without that header, the reverse proxy in front of
# this Ollama server can't tell the body is JSON and hands the whole raw
# string to its schema validator as a bare value instead of parsing it into
# an object, which is the confirmed root cause of the
# "Input should be a valid dictionary" error this session kept hitting
# against this specific proxy (independent of the trailing "/" on
# api_base, which was a separate, unrelated nginx routing quirk). Patched
# once, at import time, by adding the missing header before the request is
# sent; everything else about the call is untouched. Verified end-to-end
# through real dspy.LM + dspy.Predict calls against the live server.
def _patched_make_common_sync_call(
    self,
    sync_httpx_client,
    provider_config,
    api_base,
    headers,
    data,
    timeout,
    litellm_params,
    logging_obj,
    stream=False,
    signed_json_body=None,
):
    headers = {**headers, "Content-Type": "application/json"}
    return sync_httpx_client.post(
        url=api_base,
        headers=headers,
        content=(signed_json_body if signed_json_body is not None else json.dumps(data)),
        timeout=timeout,
        stream=stream,
        logging_obj=logging_obj,
    )


BaseLLMHTTPHandler._make_common_sync_call = _patched_make_common_sync_call
