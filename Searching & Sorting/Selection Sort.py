def selection(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                arr[min_index], arr[j] = arr[j], arr[min_index]

    print(arr)


arr = [6, 4, 8, 2, 1, 9, 7, 10]
selection(arr)
