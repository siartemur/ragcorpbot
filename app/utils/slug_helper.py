from slugify import slugify

def safe_filename(filename: str) -> str:
    return slugify(filename)
