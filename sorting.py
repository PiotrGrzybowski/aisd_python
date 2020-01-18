import time
import random

from typing import List

from tqdm import tqdm


def bubble_sort(array: List[int]):
    length = len(array)

    for i in range(length):
        is_sorted = True
        for j in range(length - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                is_sorted = False

        if is_sorted:
            break


def insertion_sort(array):
    for index in range(1, len(array)):
        current_element = array[index]

        j = index - 1
        while j >= 0 and current_element < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = current_element


def merge(left, right):
    left_pointer = 0
    right_pointer = 0
    result = []

    while len(result) < len(left) + len(right):
        if left_pointer >= len(left):
            result.append(right[right_pointer])
            right_pointer += 1
        elif right_pointer >= len(right):
            result.append(left[left_pointer])
            left_pointer += 1

        elif left[left_pointer] <= right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer += 1
        else:
            result.append(right[right_pointer])
            right_pointer += 1

    return result


def merge_sort(array):
    length = len(array)
    if length == 1:
        return array

    left = merge_sort(array[length // 2:])
    right = merge_sort(array[:length // 2])

    return merge(left, right)


def partition(array, low, high):
    random_index = random.randint(low, high)
    array[high], array[random_index] = array[random_index], array[high]
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            array[j], array[i] = array[i], array[j]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)


if __name__ == '__main__':
    a = [1, 3, 3, 3, 8, 3, 9, 4, 5, 7]
    quick_sort(a, 0, len(a) - 1)
    print(a)

    # print(merge([1, 4, 9], [3, 4]))
    # for i in tqdm(range(1, 5000)):
    #     array = [random.randint(0, 9) for _ in range(i)]
    #     merge_sort(array)
