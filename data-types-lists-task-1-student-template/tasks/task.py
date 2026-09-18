from typing import List, Tuple

def sort_unique_elements(str_list: Tuple[str, ...]) -> List[str]:
    clean = set(str_list)
    return list(sorted(clean))
