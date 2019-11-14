from typing import List


def remove_duplicates(values: List[int], val: int) -> int:
    i = 0
    for j in range(len(values)):
        if values[j] != val:
            values[i] = values[j]
            i += 1
    return i


print(remove_duplicates([4, 3, 7, 3, 2, 3], 3))
