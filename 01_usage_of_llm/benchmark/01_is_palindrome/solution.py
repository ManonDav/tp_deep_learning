import re

def is_palindrome(s: str) -> bool:
    processed = re.sub(r'[^a-z0-9]', '', s.lower())
    return processed == processed[::-1]