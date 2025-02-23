# Bubble Sort Algorithm
# Time Complexity: O(n^2)
# Memory Space: O(1)

# Best Case: O(n) (Everything is sorted already)
# Average Case: O(n^2)
# Worst Case: O(n^2)

def bubble_sort(arr: list):
    size = len(arr)
    is_swaped = False

    for i in range(size - 1):
        is_swaped = False
        for j in range(size - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_swaped = True
        
        if not is_swaped:
            break

    return arr

# NOTES:
# - i due to the highest element will always be sorted first, then the next highest, etc. Don't need to compare the end anymore
# is_swaped checked if anything was swaped. If nothing was then the array is sorted. Therefore, break out and return array.
                



