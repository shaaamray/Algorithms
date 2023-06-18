arr = [3, 4, 5, 6, 8, 9, 10]
target = 9

#array has to be sorted to implement binary search
#find mid using left & right pointers, then compare and update pointer till getting the target element, else return -1 if not found

def binary(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = left + (right-left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1
    
b = binary(arr, target)
print(b)
    
