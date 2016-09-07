import algorithm as algo
import random


def test_merge_sort():
    for _ in range(100):
        r = random.randint(0, 100)
        arr = [random.randint(-100, 100) for _ in range(r)]
        assert algo.merge_sort(arr) == sorted(arr)
