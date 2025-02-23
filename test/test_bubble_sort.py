import sort

# Bubble Sort Tests
def test_bubble_sort_empty():
    assert sort.bubble_sort([]) == []


def test_bubble_sort_one():
    test_arr, correct_arr = sort.create_test_arrays(1, 50, 1)
    assert sort.bubble_sort(test_arr) == correct_arr


def test_bubble_sort_xs():
    test_arr, correct_arr = sort.create_test_arrays(1, 50, 10)
    print(test_arr, correct_arr)
    assert sort.bubble_sort(test_arr) == correct_arr


def test_bubble_sort_s():
    test_arr, correct_arr = sort.create_test_arrays(1, 50, 100)
    print(test_arr, correct_arr)
    assert sort.bubble_sort(test_arr) == correct_arr


def test_bubble_sort_m():
    test_arr, correct_arr = sort.create_test_arrays(1, 50, 1000)
    print(test_arr, correct_arr)
    assert sort.bubble_sort(test_arr) == correct_arr


def test_bubble_sort_l():
    test_arr, correct_arr = sort.create_test_arrays(1, 50, 10000)
    print(test_arr, correct_arr)
    assert sort.bubble_sort(test_arr) == correct_arr