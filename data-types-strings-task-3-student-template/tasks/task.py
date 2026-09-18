def replacer(s: str) -> str:
    table = str.maketrans("\"'", "'\"")
    return s.translate(table)
