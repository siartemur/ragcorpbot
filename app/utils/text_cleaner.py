import re

def clean_text(text: str) -> str:
    text = text.replace("\n", " ").replace("\r", " ")
    text = re.sub(r'\s+', ' ', text) 
    return text.strip()
