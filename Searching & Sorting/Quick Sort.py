arr = [6, 4, 8, 2, 1, 9, 7, 10]


def quicksort(arr, left, right):
    if left < right:
        pivot_pos = partition(arr, left, right)

        quicksort(arr, left, pivot_pos - 1)
        quicksort(arr, pivot_pos + 1, right)


def partition(arr, left, right):
    pivot_index = left
    pivot = arr[pivot_index]
    while left < right:
        while left < len(arr) and pivot >= arr[left]:
            left += 1
        while arr[right] > pivot:
            right -= 1

        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]

    return right


quicksort(arr, 0, len(arr) - 1)
print(arr)