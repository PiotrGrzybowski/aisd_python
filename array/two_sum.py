from typing import List, Tuple


def two_sum_1(values: List[int], target: int) -> Tuple[int, int]:
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            if values[j] == target - values[i]:
                return i, j

    return -1, -1


print(two_sum_1([2, 7, 11, 15], 13))


def two_sum_2(values: List[int], target: int) -> Tuple[int, int]:
    mapping = {value: i for i, value in enumerate(values)}

    for i, value in enumerate(values):
        complement = target - value
        if complement in mapping and mapping[complement] != i:
            return i, mapping[complement]

    return -1, -1


print(two_sum_2([2, 7, 11, 15], 13))


def two_sum_3(values: List[int], target: int) -> Tuple[int, int]:
    mapping = {}

    for i, value in enumerate(values):
        complement = target - value
        if complement in mapping and mapping[complement] != i:
            return mapping[complement], i
        mapping[value] = i

    return -1, -1


print(two_sum_3([2, 7, 11, 15], 13))
