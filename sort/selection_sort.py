# Selection Sort Algorithm
# Time Complexity: O(n^2)
# Memory Space: O(1)

# Best Case: O(n^2)
# Average Case: O(n^2)
# Worst Case: O(n^2)

def selection_sort(arr: list):
    size = len(arr)

    for i in range(size - 1):
        min_element = arr[i]
        min_idx = i
        for j in range(i + 1, size):
            if arr[j] < min_element:
                min_element = arr[j]
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

# NOTES:
# i + 1 in loop because everything before will already be sorted