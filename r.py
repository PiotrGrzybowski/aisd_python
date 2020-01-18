import time
from random import randint

import pickle
import matplotlib.pyplot as plt
from tqdm import tqdm

from sorting import merge_sort, insertion_sort, bubble_sort


def create_durations(max_length, algorithm, name):
    durations = []
    for i in tqdm(range(1, max_length)):
        # generować kolejne listy do sortowania
        numbers_to_sort = [randint(0, 100) for _ in range(i)]
        # zmierzyć czas wykonywania algorytmu sortowania i dodać go do listy wynikowej durations
        start = time.time()
        algorithm(numbers_to_sort)
        durations.append(time.time() - start)
    # zapisz listę durations do pliku pickle o nazwie name_{max_lenght}.pickle
    with open(f'{name}_{max_length}.pickle', 'wb') as f:
        pickle.dump(durations, f)


def get_durations(max_lenth: int, name: str):
    """loads pickle with durations from max_lenth and algorithm name"""
    with open(f'{name}_{max_lenth}.pickle', 'rb') as f:
        return pickle.load(f)


if __name__ == '__main__':
    # create_durations(1000, bubble_sort, "bubble")
    bubble_durations = get_durations(1000, 'bubble')
    # bubble_last = bubble_durations[-1]
    # bubble_durations.extend([bubble_last for _ in tqdm(range(9000))])
    # create_durations(1000, insertion_sort, "insertion")
    insertion_durations = get_durations(1000, 'insertion')
    # insertion_last = insertion_durations[-1]
    # insertion_durations.extend([insertion_last for _ in tqdm(range(9000))])
    create_durations(1000, merge_sort, 'merge')
    merge_durations = get_durations(1000, 'merge')
    x = range(len(merge_durations))
    plt.plot(x, bubble_durations)
    plt.plot(x, insertion_durations)
    plt.plot(x, merge_durations)
    plt.legend(['bubble_sort',
                'insertion_sort',
                'merge sort'
                ], loc='upper center')
    plt.savefig('research_fig.png')
