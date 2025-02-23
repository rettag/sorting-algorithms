import matplotlib.pyplot as plt
import timeit
import sort

# Execution time of popular sorting algorithms againt Python's sort() function
bubble_times = []
selection_times = []
insertion_times = []
merge_times = []
quick_times = []
python_times = []

sizes = [1, 10, 100, 250, 500, 1000, 2500, 5000, 7500, 10000, 25000, 50000, 75000, 100000]

for i in sizes:
    print(f'Timing Arrays Of Size {i}')
    test_arr, _ = sort.create_test_arrays(1, 50, i)

    bubble_times.append(timeit.timeit(lambda: sort.bubble_sort(test_arr.copy()), number=1))
    selection_times.append(timeit.timeit(lambda: sort.selection_sort(test_arr.copy()), number=1))
    insertion_times.append(timeit.timeit(lambda: sort.insertion_sort(test_arr.copy()), number=1))
    merge_times.append(timeit.timeit(lambda: sort.merge_sort(test_arr.copy()), number=1))
    quick_times.append(timeit.timeit(lambda: sort.quick_sort(test_arr.copy(), 0, len(test_arr) - 1), number=1))
    python_times.append(timeit.timeit(lambda: sorted(test_arr.copy()), number=1))

plt.figure(figsize=(10, 6))
plt.plot(sizes, bubble_times, marker='o', label='Bubble Sort')
plt.plot(sizes, selection_times, marker='o', label='Selection Sort')
plt.plot(sizes, insertion_times, marker='o', label='Insertion Sort')
plt.plot(sizes, merge_times, marker='o', label='Merge Sort')
plt.plot(sizes, quick_times, marker='o', label='Quick Sort')
plt.plot(sizes, python_times, marker='o', label='Python Sort()')

plt.xlabel('Array Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Sorting Algorithm Execution Times vs Array Size')
plt.legend()
plt.grid(True)
plt.show()


