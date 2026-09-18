def get_fractions(a_b: str, c_b: str) -> str:
    a, b = a_b.split("/")
    c, _ = c_b.split("/")

    return f"{a}/{b} + {c}/{b} = {int(a)+int(c)}/{b}"
