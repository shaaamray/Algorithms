arr = [4, 2, 5, 6, 1, 10, 3]
target = 10

def linear(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i, arr[i]
    return -1
    
l = linear(arr, target)
print("Index", "\t", "Value")
print(l)
