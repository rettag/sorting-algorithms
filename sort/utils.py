import numpy as np


def create_test_arrays(lowest_val=1, highest_val=50, size=10):
    """
    Args:
        lowest_val (int): the lowest value generated in the array
        highest_val (int): the highest value generate in the array
        size (int): the size of the generated array

    Returns:
        random_arr (list): a randomly generated array
        sorted_arr (list): the sorted array of random_arr
    """
    random_arr = np.random.randint(lowest_val, highest_val + 1, size=size)
    sorted_arr = np.sort(random_arr.copy())

    return random_arr.tolist(), sorted_arr.tolist()