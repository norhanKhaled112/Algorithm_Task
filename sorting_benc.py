
import random
import time
import matplotlib.pyplot as plt



def insertion_sort(arr):
    arr = arr.copy()

    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = temp

    return arr



def merge_sort(arr):
    if len(arr) <= 1:
        return arr.copy()

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result



def quick_sort(arr):
    if len(arr) <= 1:
        return arr.copy()

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)



def measure_time(sort_function, data):
    start = time.perf_counter()
    result = sort_function(data)
    end = time.perf_counter()

    assert result == sorted(data), "Sorting result is incorrect!"

    return end - start


algorithms = {
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort,
    "Python sorted()": sorted
}

sizes = [1000, 2000, 5000]
data_types = ["Sorted", "Reversed", "Random"]

results = {
    algorithm: {kind: [] for kind in data_types}
    for algorithm in algorithms
}


for n in sizes:
    random_data = [random.randint(0, 10000) for _ in range(n)]

    datasets = {
        "Sorted": sorted(random_data),
        "Reversed": sorted(random_data, reverse=True),
        "Random": random_data
    }

    for kind, data in datasets.items():
        print(f"\nSize: {n} | Type: {kind}")

        for name, function in algorithms.items():
            
            if name == "Insertion Sort" and n > 5000:
                continue

            elapsed = measure_time(function, data)
            results[name][kind].append(elapsed)

            print(f"{name}: {elapsed:.6f} seconds")



for kind in data_types:
    plt.figure(figsize=(9, 5))

    for name in algorithms:
        times = results[name][kind]

        if len(times) == len(sizes):
            plt.plot(sizes, times, marker="o", label=name)

    plt.title(f"Sorting Benchmark - {kind} Data")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Running Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

plt.show()
