def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

my_array = [19, 3, 57, 12, 88, 41, 6, 73, 25, 99]
target_value = 41
result = linear_search(my_array, target_value)


if result != -1:
    print(f"Element {target_value} found at index: {result}")
    
else:   
    print(f"Element {target_value} not found in the array.")