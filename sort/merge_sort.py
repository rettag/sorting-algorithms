# Merge Sort Algorithm
# Time Complexity: O(nlogn)
# Memory Space: O(n)

# Best Case: O(nlog)
# Average Case: O(nlogn)
# Worst Case: O(nlogn)

def merge_sort(arr: list):
    size = len(arr)   
    if size > 1:
        mid = size // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the two halves back into arr.
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

