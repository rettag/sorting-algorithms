import sort

# Quick Sort Tests
def test_quick_sort_empty():
    assert sort.quick_sort([], 0, 0) == []


def test_quick_sort_one():
    test_arr, correct_arr = sort.create_test_arrays(1, 50, 1)
    assert sort.quick_sort(test_arr, 0, len(test_arr) - 1) == correct_arr


def test_quick_sort_xs():
    test_arr, correct_arr = sort.create_test_arrays(1, 50, 10)
    print(test_arr, correct_arr)
    assert sort.quick_sort(test_arr, 0, len(test_arr) - 1) == correct_arr


def test_quick_sort_s():
    test_arr, correct_arr = sort.create_test_arrays(1, 50, 100)
    print(test_arr, correct_arr)
    assert sort.quick_sort(test_arr, 0, len(test_arr) - 1) == correct_arr


def test_quick_sort_m():
    test_arr, correct_arr = sort.create_test_arrays(1, 50, 1000)
    print(test_arr, correct_arr)
    assert sort.quick_sort(test_arr, 0, len(test_arr) - 1) == correct_arr


def test_quick_sort_l():
    test_arr, correct_arr = sort.create_test_arrays(1, 50, 10000)
    print(test_arr, correct_arr)
    assert sort.quick_sort(test_arr, 0, len(test_arr) - 1) == correct_arr