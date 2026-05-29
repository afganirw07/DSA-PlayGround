import matplotlib.pyplot as plt

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pivot_index = partition(arr, low, high)          
        plt.title("Quick Sort")
        plt.bar(range(len(arr)), arr, align='center', color='red' )
        plt.pause(0.5)
        plt.clf()
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)

        
my_array = [19, 3, 57, 12, 88, 41, 6, 73, 25, 99]
quicksort(my_array, 0, len(my_array) - 1)
plt.title("Quick Sort")
plt.bar(range(len(my_array)), my_array, align='center', color='red' )
plt.show()