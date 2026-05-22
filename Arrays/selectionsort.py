import matplotlib.pyplot as plt
my_array = [19, 3, 57, 12, 88, 41, 6, 73, 25, 99]

n = len(my_array)
for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
        if my_array[j] < my_array[min_index]:
            min_index = j
    min_value = my_array.pop(min_index)
    my_array.insert(i, min_value)
    plt.title("Selection Sort")
    plt.bar(range(len(my_array)), my_array, align='center', color='red' )
    plt.pause(0.8)
    plt.clf()

plt.title("Selection Sort")
plt.bar(range(len(my_array)), my_array, align='center', color='red' )
plt.show()
print(my_array)