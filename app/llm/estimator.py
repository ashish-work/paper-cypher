import tiktoken

encoding = tiktoken.get_encoding("cl100k_base")


def get_token_count(text:str) -> int:
    return len(encoding.encode(text))