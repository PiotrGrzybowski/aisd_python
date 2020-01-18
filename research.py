import random
import time

from tqdm import tqdm
import pickle
from sorting import bubble_sort, insertion_sort, merge_sort
import matplotlib.pyplot as plt


def create_durations(max_length, algorithm, name):
    durations = []
    for i in tqdm(range(max_length)):
        numbers_to_sort = [random.randint(0, 100) for _ in range(i)]

        start = time.time()
        algorithm(numbers_to_sort)
        durations.append(time.time() - start)

    with open(f'{name}_{max_length}.pickle', 'wb') as f:
        pickle.dump(durations, f)


def get_durations(max_length, name):
    with open(f'{name}_{max_length}.pickle', 'rb') as f:
        return pickle.load(f)


if __name__ == '__main__':
    n = 1000
    # create_durations(n, bubble_sort, "bubble")
    # create_durations(n, insertion_sort, "inserts")
    create_durations(n, merge_sort, "merge")

    # bubbles = get_durations(n, "bubble")
    # inserts = get_durations(n, "inserts")
    # print(len(bubbles))
    # print(len(inserts))
    #
    # x = range(n)
    # plt.plot(x, bubbles)
    # plt.plot(x, inserts)
    # plt.legend(['Bubble Sort', 'Insert Sort'])
    # plt.show()
