import algorithm as algo
import random


def get_random_arr(n):
    return [random.randint(-100, 100) for _ in range(n)]


def test_merge_sort():
    for _ in range(500):
        r = random.randint(0, 100)
        arr = get_random_arr(r)
        assert algo.mergesort(arr) == sorted(arr)


def test_quicksort():
    for _ in range(500):
        r = random.randint(0, 100)
        arr = get_random_arr(r)
        arr_copy = arr[:]

        algo.quicksort(arr, 0, len(arr) - 1)
        assert arr == sorted(arr_copy)
