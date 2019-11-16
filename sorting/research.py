import numpy as np
import pickle

import matplotlib.pyplot as plt
from tqdm import tqdm
from random import shuffle
from time import time

from sorting.algorithms import insertion_sort, bubble_sort, merge_sort


def test_durations(n, fun, name):
    durations = []
    for i in tqdm(range(n)):
        # generowanie tablicy do sortowania
        numbers_to_sort = list(range(i))
        shuffle(numbers_to_sort)
        start = int(round(time() * 1000))
        fun(numbers_to_sort)
        end = int(round(time() * 1000))
        durations.append(end - start)
    # wyświetl wykres (patrz na Slacka)
    with open(f'durations_{name}_{n}.pkl', 'wb') as f:
        pickle.dump(durations, f)


def display_durations(n, name):
    with open(f'durations_{name}_{n}.pkl', 'rb') as f:
        durations = pickle.load(f)
    x = np.arange(len(durations))
    plt.plot(x, durations)
    plt.show()


def get_durations(n, name):
    with open(f'durations_{name}_{n}.pkl', 'rb') as f:
        return pickle.load(f)


if __name__ == "__main__":
    # test_durations(1000, insertion_sort, "insertion")
    # test_durations(1000, bubble_sort, "bubble")
    test_durations(1000, merge_sort, "merge")
    insertions = get_durations(1000, "insertion")
    bubbles = get_durations(1000, "bubble")
    merges = get_durations(1000, "merge")
    x = np.arange(len(bubbles))
    plt.plot(x, bubbles)
    plt.plot(x, insertions)
    plt.plot(x, merges)
    plt.show()
