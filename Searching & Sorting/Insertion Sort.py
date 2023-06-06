def insertion(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:  #till j not reaches 0 index and key is less than arr[j]
            arr[j+1] = arr[j]  # shift value of j to j+1 means in right as the value is bigger than key value
            j -= 1  # decrement by 1
        arr[j+1] = key

    print(arr)


arr = [6, 4, 8, 2, 1, 9, 7, 10]
insertion(arr)

