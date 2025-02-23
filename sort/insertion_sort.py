# Insertion Sort Algorithm
# Time Complexity: O(n^2)
# Memory Space: O(1)

# Best Case: O(n) (Everything is already sorted)
# Average Case: O(n^2)
# Worst Case: O(n^2)

def insertion_sort(arr: list):
    size = len(arr)

    for i in range(1, size):
        num_to_order = arr[i]
        j = i - 1
        while j >= 0 and num_to_order < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = num_to_order

    return arr