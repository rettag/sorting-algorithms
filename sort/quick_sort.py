# Quick Sort Algorithm
# Time Complexity: O(n^2)
# Memory Space: O(nlogn)

# Best Case: O(nlog)
# Average Case: O(nlogn)
# Worst Case: O(n^2)


def partition(arr: list, low: int, high: int):
    pivot = arr[low]
    i = low - 1
    j = high + 1
    while True:
        # Move i to the right until an element is found that is not less than pivot.
        i += 1
        while arr[i] < pivot:
            i += 1
        # Move j to the left until an element is found that is not greater than pivot.
        j -= 1
        while arr[j] > pivot:
            j -= 1
        # If pointers have crossed, return the partition index.
        if i >= j:
            return j
        # Otherwise, swap the elements at i and j.
        arr[i], arr[j] = arr[j], arr[i]


def quick_sort(arr: list, low: int, high: int):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p)
        quick_sort(arr, p + 1, high)
    return arr
