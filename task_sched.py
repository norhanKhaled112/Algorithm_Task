
import random
import time


class Task:
    def __init__(self, name, priority, arrival_time):
        self.name = name
        self.priority = priority
        self.arrival_time = arrival_time

    def __str__(self):
        return (
            f"Task: {self.name} | "
            f"Priority: {self.priority} | "
            f"Arrival: {self.arrival_time}"
        )


class TaskScheduler:
    def __init__(self):
        self.heap = []

    def insert(self, task):
        # Add the task at the end
        self.heap.append(task)

     
        i = len(self.heap) - 1

        while i > 0:
            parent = (i - 1) // 2

            if self.heap[i].priority <= self.heap[parent].priority:
                break

            self.heap[i], self.heap[parent] = (
                self.heap[parent],
                self.heap[i]
            )

            i = parent

    def extract_max(self):
        if not self.heap:
            return None


        highest = self.heap[0]

        last = self.heap.pop()

        if self.heap:
            self.heap[0] = last
            self._heapify(0)

        return highest

    def _heapify(self, i):
        size = len(self.heap)

        while True:
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if (
                left < size
                and self.heap[left].priority
                > self.heap[largest].priority
            ):
                largest = left

            if (
                right < size
                and self.heap[right].priority
                > self.heap[largest].priority
            ):
                largest = right

            if largest == i:
                break

            self.heap[i], self.heap[largest] = (
                self.heap[largest],
                self.heap[i]
            )

            i = largest

    def show_tasks(self):
        if not self.heap:
            print("No tasks available.")
            return

        print("\nTasks currently in the scheduler:")
        for task in self.heap:
            print(task)


def main():
    scheduler = TaskScheduler()


    tasks = [
        Task("A", 3, 1),
        Task("B", 9, 2),
        Task("C", 5, 3),
        Task("D", 7, 4)
    ]

    print("=== Task Scheduler ===")


    for task in tasks:
        scheduler.insert(task)
        print(f"Added: {task.name}")

    scheduler.show_tasks()

   
    print("\n=== Executing Tasks ===")

    while scheduler.heap:
        task = scheduler.extract_max()
        print(f"Executing: {task}")


if __name__ == "__main__":
    main()
