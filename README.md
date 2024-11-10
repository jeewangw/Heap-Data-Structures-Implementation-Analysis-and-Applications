Heap Data Structures: Heapsort and Priority Queue Implementation
Overview
This project explores the implementation and analysis of heap data structures in Python, focusing on:

Heapsort Algorithm: A sorting algorithm using a max-heap to sort an array.
Priority Queue: A max-heap-based priority queue that simulates a scheduling system for managing tasks by priority.
The repository includes code for both Heapsort and a Priority Queue, along with a report that discusses the design choices, time complexity analysis, and the empirical comparison of Heapsort with Quicksort and Merge Sort.

Features
Heapsort: An in-place sorting algorithm that consistently performs at O(n log n) time complexity.
Priority Queue: Built on a binary heap structure, this queue allows for efficient insertion, extraction of maximum priority tasks, and priority updates.
File Structure
heapsort.py: Contains the Heapsort implementation.
priority_queue.py: Contains the Priority Queue implementation with a Task class.
report.pdf: A detailed report discussing implementation, design choices, and results from the empirical analysis.
README.md: Instructions and overview of the project.
Requirements
Python 3.6 or above.
Getting Started
Cloning the Repository
bash
Copy code
git clone https://github.com/yourusername/heap-data-structures.git
cd heap-data-structures
Running the Code
Heapsort:

Run heapsort.py to execute the Heapsort algorithm on a sample array.
Edit the sample array in heapsort.py as needed to test different cases.
bash
Copy code
python heapsort.py
Priority Queue:

Run priority_queue.py to test the priority queue with task insertion, extraction, and priority update operations.
bash
Copy code
python priority_queue.py
Code Explanation
Heapsort
Heapsort is implemented using a max-heap. Key steps include:

Build a max-heap from the input array.
Extract the maximum element repeatedly and place it at the end of the array, reducing the heap size each time.
The result is a sorted array in ascending order.
Priority Queue
The priority queue uses a binary heap stored as an array. Core operations include:

Insert: Adds a new task with a specified priority.
Extract Max: Removes and returns the task with the highest priority.
Increase Key: Updates a task’s priority and adjusts its position in the heap.
Time Complexity
Heapsort: O(n log n) in all cases.
Priority Queue:
insert: O(log n)
extract_max: O(log n)
increase_key: O(log n)
Results and Findings
Heapsort vs Other Sorting Algorithms: Heapsort performs consistently at O(n log n), though it is often slower than Quicksort and Merge Sort in practice due to cache inefficiency.
Priority Queue in Scheduling: The priority queue effectively prioritizes tasks, demonstrating real-world applications in scheduling where task priorities change dynamically.
Conclusion
This project demonstrates the versatility and efficiency of heaps in sorting and task scheduling applications. Heapsort is robust but generally slower than some other O(n log n) algorithms, while priority queues provide an efficient way to manage tasks by priority.