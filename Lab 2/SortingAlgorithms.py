import time
import matplotlib.pyplot as plt
import random


arr_small_range = []
arr_small_range2 = []
arr_small_range3 = []
arr_small_range4 = []
arr_small_range5 = []
arr_large_range = []
arr_large_range2 = []
arr_large_range3 = []
arr_large_range4 = []
arr_large_range5 = []

for i in range(50000):
    arr_small_range.append(random.randint(0, 100))
    arr_small_range2.append(random.randint(0, 100))
    arr_small_range3.append(random.randint(0, 100))
    arr_small_range4.append(random.randint(0, 100))
    arr_small_range5.append(random.randint(0, 100))
    arr_large_range.append(random.randint(0, 1000000))
    arr_large_range2.append(random.randint(0, 1000000))
    arr_large_range3.append(random.randint(0, 1000000))
    arr_large_range4.append(random.randint(0, 1000000))
    arr_large_range5.append(random.randint(0, 1000000))


def heap_sort(arr):
    n = len(arr)
    # Build a max heap from the input array
    build_max_heap(arr, n)
    # Extract elements from the heap one by one and place them at the end of the array
    for i in range(n - 1, 0, -1):
        # Swap the root node with the last node
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)  # Heapify the reduced heap
    return arr


def build_max_heap(arr, n):
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)


def heapify(arr, n, i):
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child
    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr


def quick_sort(arr, low, high):
    if low < high:
        partition_index = partition(arr, low, high)
        quick_sort(arr, low, partition_index - 1)
        quick_sort(arr, partition_index + 1, high)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def counting_sort(arr):
    max_element = int(max(arr))
    count = [0 for _ in range(max_element + 1)]
    for i in arr:
        count[i] += 1
    temp = 0
    for i in range(max_element + 1):
        for j in range(count[i]):
            arr[temp] = i
            temp += 1
    return arr


results = []
temp = []

start = time.time()
temp = quick_sort(arr_small_range.copy(), 0, len(arr_small_range) - 1)
temp = quick_sort(arr_small_range2.copy(), 0, len(arr_small_range2) - 1)
temp = quick_sort(arr_small_range3.copy(), 0, len(arr_small_range3) - 1)
temp = quick_sort(arr_small_range4.copy(), 0, len(arr_small_range4) - 1)
temp = quick_sort(arr_small_range5.copy(), 0, len(arr_small_range5) - 1)
end = time.time()
results.append(round(end - start, 8) / 5)

start = time.time()
temp = merge_sort(arr_small_range.copy())
temp = merge_sort(arr_small_range2.copy())
temp = merge_sort(arr_small_range3.copy())
temp = merge_sort(arr_small_range4.copy())
temp = merge_sort(arr_small_range5.copy())
end = time.time()
results.append(round(end - start, 8)/5)

start = time.time()
temp = heap_sort(arr_small_range.copy())
temp = heap_sort(arr_small_range2.copy())
temp = heap_sort(arr_small_range3.copy())
temp = heap_sort(arr_small_range4.copy())
temp = heap_sort(arr_small_range5.copy())
end = time.time()
results.append(round(end - start, 8)/5)

start = time.time()
temp = counting_sort(arr_small_range.copy())
temp = counting_sort(arr_small_range2.copy())
temp = counting_sort(arr_small_range3.copy())
temp = counting_sort(arr_small_range4.copy())
temp = counting_sort(arr_small_range5.copy())
end = time.time()
results.append(round(end - start, 8))

plt.figure(1)
plt.bar(['Quick sort', 'Merge sort', 'Heap sort',
        'Counting sort'], results, color='red')
plt.title('Sorting array of 50000 elements with small range (values 0 to 100)')
plt.xlabel('Algorithms')
plt.ylabel('Time in seconds')


results = []
temp = []

start = time.time()
temp = quick_sort(arr_large_range.copy(), 0, len(arr_large_range) - 1)
temp = quick_sort(arr_large_range2.copy(), 0, len(arr_large_range2) - 1)
temp = quick_sort(arr_large_range3.copy(), 0, len(arr_large_range3) - 1)
temp = quick_sort(arr_large_range4.copy(), 0, len(arr_large_range4) - 1)
temp = quick_sort(arr_large_range5.copy(), 0, len(arr_large_range5) - 1)
end = time.time()
results.append(round(end - start, 8) / 5)

start = time.time()
temp = merge_sort(arr_large_range.copy())
temp = merge_sort(arr_large_range2.copy())
temp = merge_sort(arr_large_range3.copy())
temp = merge_sort(arr_large_range4.copy())
temp = merge_sort(arr_large_range5.copy())
end = time.time()
results.append(round(end - start, 8)/5)

start = time.time()
temp = heap_sort(arr_large_range.copy())
temp = heap_sort(arr_large_range2.copy())
temp = heap_sort(arr_large_range3.copy())
temp = heap_sort(arr_large_range4.copy())
temp = heap_sort(arr_large_range5.copy())
end = time.time()
results.append(round(end - start, 8)/5)

start = time.time()
temp = counting_sort(arr_large_range.copy())
temp = counting_sort(arr_large_range2.copy())
temp = counting_sort(arr_large_range3.copy())
temp = counting_sort(arr_large_range4.copy())
temp = counting_sort(arr_large_range5.copy())
end = time.time()
results.append(round(end - start, 8))

plt.figure(2)
plt.bar(['Quick sort', 'Merge sort', 'Heap sort',
        'Counting sort'], results, color='green')
plt.title('Sorting array of 50000 elements with large range (values 0 to 100000)')
plt.xlabel('Algorithms')
plt.ylabel('Time in seconds')
plt.show()
