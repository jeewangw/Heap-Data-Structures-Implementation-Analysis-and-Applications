class Task:
    def __init__(self, task_id, priority):
        self.task_id = task_id
        self.priority = priority

    def __str__(self):
        return f"Task ID: {self.task_id}, Priority: {self.priority}"

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, task):
        self.heap.append(task)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()  # Move last to root
        self._heapify_down(0)
        return root

    def increase_key(self, index, new_priority):
        if new_priority < self.heap[index].priority:
            raise ValueError("New priority must be greater than current priority")
        self.heap[index].priority = new_priority
        self._heapify_up(index)

    def is_empty(self):
        return len(self.heap) == 0

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index].priority > self.heap[parent].priority:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def _heapify_down(self, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left].priority > self.heap[largest].priority:
            largest = left
        if right < len(self.heap) and self.heap[right].priority > self.heap[largest].priority:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

# Example usage
pq = PriorityQueue()
pq.insert(Task(1, 5))
pq.insert(Task(2, 3))
pq.insert(Task(3, 10))

print("Top priority task:", pq.extract_max())