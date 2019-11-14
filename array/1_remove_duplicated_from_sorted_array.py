from typing import List


def remove_duplicates(values: List[int]) -> int:
    if not values:
        return 0

    i = 0
    j = 1

    while j < len(values):
        if values[j] != values[i]:
            i += 1
            values[i] = values[j]

        j += 1

    return i + 1


if __name__ == '__main__':
    print(remove_duplicates([1, 1, 1, 1, 2, 2, 2, 3]))