def get_longest_word(s: str) -> str:
    filtered_s = s.split()
    max_len = filtered_s[0]
    for i in filtered_s:
        if len(i) > len(max_len):
            max_len = i

    return max_len


