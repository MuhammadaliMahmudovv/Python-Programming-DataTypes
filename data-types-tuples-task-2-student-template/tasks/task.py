from typing import Any, Tuple, List


def get_pairs(lst: List[Any]) -> List[Tuple[Any, Any]]:
    result = []
    if len(lst) > 1:
        for i in range(len(lst) - 1):
            print(i)
            a = lst[i], lst[i + 1]
            result.append(tuple(a))
    return result


