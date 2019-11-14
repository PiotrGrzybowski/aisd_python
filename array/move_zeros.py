from typing import List


def move_zeros(values: List[int]):
    last_not_zero_index = 0
    for i in range(len(values)):
        if values[i] != 0:
            values[last_not_zero_index] = values[i]
            last_not_zero_index += 1

    for i in range(last_not_zero_index, len(values)):
        values[i] = 0
    print(values)

move_zeros([0,0,0,0,4,3,2,1,0])