import time
from random import shuffle
import pickle


def timeit(method):
    def timed(*args, **kw):
        start = time.time()
        result = method(*args, **kw)
        end = time.time()
        time_result = (end - start) * 1000000
        return result, time_result

    return timed


def insertion_sort(numbers):
    for index in range(1, len(numbers)):
        current_element = numbers[index]
        j = index - 1
        while j >= 0 and current_element < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = current_element


def generate_ordered_list(length):
    return list(range(length))


def generate_invert_list(length):
    return list(reversed(range(length)))


def generate_random_list(length):
    values = list(range(length))
    shuffle(values)
    return values


@timeit
def sort_list(values, sorting_function):
    sorting_function(values)


def generate_sorting_durations(max_length, values_generator, sort_function):
    durations = []
    for i in range(max_length):
        values = values_generator(i)
        _, time_result = sort_list(values, sort_function)
        durations.append(time_result)

    with open(build_sorting_filename(max_length, values_generator, sort_function), 'wb') as f:
        pickle.dump(durations, f)
    return durations


@timeit
def factorial(n):
    return 1 if n == 1 else n * factorial(n - 1)


def generate_factorial_durations(max_size):
    durations = []
    for i in range(max_size):
        _, time_result = factorial(i)
        durations.append(time_result)

    with open(f'factorial_{max_size}', 'wb') as f:
        pickle.dump(durations, f)
    return durations


def build_sorting_filename(max_length, values_generator, sort_function):
    sort_name = sort_function.__name__.split('_')[0]
    data_name = values_generator.__name__.split('_')[1]
    return f'{sort_name}_{data_name}_{max_length}.pickle'


def swap(numbers, i, j):
    tmp = numbers[i]
    numbers[i] = numbers[j]
    numbers[j] = tmp


# def make_experiment
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

if __name__ == '__main__':
    # generate_sorting_durations(1000, generate_ordered_list, insertion_sort)
    # generate_sorting_durations(1000, generate_invert_list, insertion_sort)
    # generate_sorting_durations(1000, generate_random_list, insertion_sort)
    l = [9, 0, 1, 11]
    r = merge_sort(l)
    print(r)
