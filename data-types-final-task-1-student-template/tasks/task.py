from typing import Any, Dict, List, Set

def check(lst: List[Dict[Any, Any]]) -> Set[Any]:
    new_lst = set()
    for i in lst:
        for _, value in i.items():
            new_lst.add(value)
    return list(new_lst)

