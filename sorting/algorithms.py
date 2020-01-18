def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]


def insertion_sort(numbers):
    for index in range(1, len(numbers)):
        # index przechowuje indeks liczby, dla której szukamy
        # odpowiedniego miejsca
        current_element = numbers[index]
        j = index - 1
        while j >= 0 and current_element < numbers[j]:
            # print(numbers)
            pass  # swap
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = current_element
    return numbers


def merge_sort(numbers):
    n = len(numbers)
    if n == 1:
        return numbers
    left = numbers[:n // 2]
    right = numbers[n // 2:]
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    return merge(left_sorted, right_sorted)


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
        elif left[left_pointer] > right[right_pointer]:
            result.append(right[right_pointer])
            right_pointer += 1
        else:
            result.append(left[left_pointer])
            left_pointer += 1
    return result


# Python program for implementation of Quicksort Sort

# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than the pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


if __name__ == '__main__':
    a = [3, 3, 3, 3, 3, 4, 5, 6, 1, 2]
    quickSort(a, 0, len(a) - 1)
    print(a)
