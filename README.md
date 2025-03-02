# Sorting Algorithms Analysis

---
### Purpose
Sorting algorithms are fundamental to computer science. I designed this project to deepen my understanding of these algorithms, their time complexities, and memory usage. These algorithms are essential in my field, and this project serves as a growing resource and reference for the future.

### Project Overview
This project examines several popular sorting algorithms, including:
- Bubble Sort
- Insertion Sort
- Selection Sort
- Merge Sort
- Quick Sort

---

### Clone and setup project
```bash
git clone https://github.com/rettag/sorting-algorithms.git
pip install -r requirements.txt
pip install -e .
```

---
### Results
![Time Results Image](TimeResults.png)

---

### Sorting Algorithms Overview

| Algorithm         | Best Case       | Average Case    | Worst Case       | Memory Usage  |
|-------------------|-----------------|-----------------|------------------|---------------|
| **Bubble Sort**   | O(n)            | O(n²)           | O(n²)            | O(1)          |
| **Insertion Sort**| O(n)            | O(n²)           | O(n²)            | O(1)          |
| **Selection Sort**| O(n²)           | O(n²)           | O(n²)            | O(1)          |
| **Merge Sort**    | O(n log n)      | O(n log n)      | O(n log n)       | O(n)          |
| **Quick Sort**    | O(n log n)      | O(n log n)      | O(n²)            | O(log n)*     |

---

### Bubble Sort
**Description:**  
Bubble Sort repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. This process continues until the list is sorted.

**Complexity:**  
- **Worst Case:** O(n²)
- **Average Case:** O(n²)  
- **Best Case:** O(n)
  - When the list is already sorted    
- **Memory Usage:** O(1)

---

### Insertion Sort
**Description:**  
Insertion Sort builds the final sorted array one element at a time by taking an element from the unsorted portion and inserting it into the correct position within the sorted portion.

**Complexity:**
- **Worst Case:** O(n²)
- **Average Case:** O(n²)
- **Best Case:** O(n)
  - When the array is already sorted    
- **Memory Usage:** O(1)

---

### Selection Sort
**Description:**  
Selection Sort divides the list into a sorted and an unsorted part. It repeatedly selects the smallest (or largest) element from the unsorted portion and moves it to the end of the sorted portion.

**Complexity:**  
- **Worst Case:** O(n²)
- **Average Case:** O(n²)
- **Best Case:** O(n²)
- **Memory Usage:** O(1)

---

### Merge Sort
**Description:**  
Merge Sort is a divide-and-conquer algorithm. It recursively divides the array into halves, sorts each half, and then merges the sorted halves back together.

**Complexity:**  
- **Worst Case:** O(nlogn)
- **Average Case:** O(nlogn)
- **Best Case:** O(nlogn)  
- **Memory Usage:** O(n)

---

### Quick Sort
**Description:**  
Quick Sort selects a pivot element and partitions the array into two sub-arrays: one with elements less than the pivot and one with elements greater. It then recursively sorts the sub-arrays.

**Complexity:**  
- **Best and Average Case:** O(n log n)  
- **Worst Case:** O(n²)
  - If a poor pivot is consistently chosen 
- **Memory Usage:** O(log n)
  - On average due to recursion

---



**Study Guides & Resourses**
- https://www.techinterviewhandbook.org/algorithms/sorting-searching/
