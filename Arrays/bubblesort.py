import matplotlib.pyplot as plt
my_array = [19, 3, 57, 12, 88, 41, 6, 73, 25, 99]


n = len(my_array)
for i in range(n-1):
    for j in range(n-i-1):
        if my_array[j] > my_array[j+1]:
            plt.title("Bubble Sort")
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]

            plt.bar(range(len(my_array)), my_array, align='center', color='red' )
            plt.pause(0.5)
            plt.clf()
            
plt.title("Bubble Sort")
plt.bar(range(len(my_array)), my_array, align='center', color='red' )
plt.show()