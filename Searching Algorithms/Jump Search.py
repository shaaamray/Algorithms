import math

def jump(arr, size, key):
    start = 0
    block_size = math.isqrt(size)
    end = block_size

    #finding the corresponding block
    while arr[end-1] <= key and end < size:
        start = end
        end += block_size
        if end > size - 1:
            end = size

    #find the key in the block
    for i in range(start, end):
        if arr[i] == key:
            return i

    return -1


arr = [1, 3, 5, 6, 8, 9, 10]
size = 7
key = 1
j = jump(arr, size, key)
print(j)
