from typing import Dict


def get_dict(s: str) -> Dict[str, int]:
    # result = {}
    # for i in s.lower():
    #     result[i] = 1
    # for i in s.lower():
    #     if i in result.keys():
    #         result[i] += 1
    # for key, value in result.items():
    #     result[key] = value - 1
    # return result
    result = {}
    s = s.lower()

    for i in s:
        result[i] = result.get(i, 0) + 1

    return dict(sorted(result.items()))


