def check_str(s: str):
    clean = "".join(i for i in s if i.isalnum() or i.isalpha()).lower()
    left = 0
    right = len(clean) - 1
    while left < right:
        if clean[right] != clean[left]:
            return False
        left += 1
        right -= 1
    return True
