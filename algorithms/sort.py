def bubble_sort(data):
    length = len(data) - 1
    for i in range(length):
        for j in range(length - i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]


def selection_sort(data):
    for i in range(len(data) - 1):
        min_index = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_index]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]


def merge_sort(data):
    length = len(data)

    if length > 1:
        midpoint = length // 2
        left = data[:midpoint]
        right = data[midpoint:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                data[k] = left[i]
                i = i + 1
            else:
                data[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):
            data[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            data[k] = right[j]
            j = j + 1
            k = k + 1


def quick_sort(data, left, right):
    if left < right:
        p = left + (right - left) // 2
        pivot = data[p]
        i = left
        j = right
        while True:
            while data[i] < pivot:
                i = i + 1
            while data[j] > pivot:
                j = j - 1
            if i >= j:
                p = j
                break
            data[i], data[j] = data[j], data[i]
        quick_sort(data, left, p)
        quick_sort(data, p + 1, right)
