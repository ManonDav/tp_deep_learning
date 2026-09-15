import dspy  # noqa: E402
import json
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
lm = dspy.LM("ollama/qwen3:8b", api_base=OLLAMA_BASE, api_key="sk-b68056021f8b4755ab06b7d4cfc24e9b")
dspy.configure(lm=lm)

class ReponseSignature(dspy.Signature):
	"""Répond àune question de programmation par du code Python."""
	question: str = dspy.InputField()
	reponse: str = dspy.OutputField()
repondre = dspy.Predict(ReponseSignature)
print(repondre(question="""# Compression par plages (RLE)

Implémentez une fonction :

```python
def run_length_encode(s: str) -> str:
```

qui encode `s` par compression de plages (*run-length encoding*) : chaque suite de caractères
identiques consécutifs est remplacée par le nombre d'occurrences suivi du caractère.

Règles précises :
- Le compte est **toujours** inclus, même s'il vaut 1 (donc `"abc"` devient `"1a1b1c"`, pas `"abc"`).
- La comparaison est sensible à la casse : `'a'` et `'A'` sont des caractères différents.
- Une chaîne vide donne une chaîne vide.

## Exemples

```python
run_length_encode("aaabbbccd")  # "3a3b2c1d"
run_length_encode("abcd")  # "1a1b1c1d"
run_length_encode("")  # ""
run_length_encode("aAaa")  # "1a1A2a"
```""").reponse)
