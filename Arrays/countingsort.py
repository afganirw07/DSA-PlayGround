import matplotlib.pyplot as plt

def countingSort(arr):
    if arr is None or len(arr) == 0:
        return arr
    
    max_val = max(arr)
    count = [0] * (max_val + 1)
    
    for num in arr:
        count[num] += 1
    
    arr[:] = []
    
    for num, freq in enumerate(count):
        arr.extend([num] * freq)
        plt.title("Counting Sort")
        plt.bar(range(len(arr)), arr, align='center', color='red' )
        plt.pause(0.5)
        plt.clf()
        
    return arr

my_array = [19, 3, 57, 12, 88, 41, 6, 73, 25, 99]
countingSort(my_array)
print(my_array)
plt.title("Counting Sort")
plt.bar(range(len(my_array)), my_array, align='center', color='red' )
plt.show()