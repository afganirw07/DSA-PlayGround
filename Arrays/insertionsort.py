import matplotlib.pyplot as plt
my_array = [19, 3, 57, 12, 88, 41, 6, 73, 25, 99]

n = len(my_array)
for i in range(1, n):
    insert_index = i
    currect_value = my_array.pop(i)
    for j in range(i-1, -1, -1):
        if my_array[j] > currect_value:
            insert_index = j
            plt.title("Insertion Sort")
            plt.bar(range(len(my_array)), my_array, align='center', color='red' )
            plt.pause(0.5)
    my_array.insert(insert_index, currect_value)
    
    
# print(my_array)
plt.title("Insertion Sort")
plt.bar(range(len(my_array)), my_array, align='center', color='red' )
plt.show()