def binary_search(sorted_data, item):
    low = 0
    high = len(sorted_data) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_data[mid] < item:
            low = mid + 1
        elif sorted_data[mid] > item:
            high = mid - 1
        else:
            return mid
    return -1
