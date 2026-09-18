from typing import Tuple


def get_tuple(num: int) -> Tuple[int]:
    # final_result = []
    # result = []
    # num = str(num)
    # for i in num:
    #     result.append(i)
    # for i in result:
    #     i = int(i)
    #     final_result.append(i)
    # return tuple(final_result)
    result = []
    for i in str(num):
        result.append(int(i))
    return tuple(result)
