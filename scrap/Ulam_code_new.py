
number_to_find = 2

with open("UlamData_1_2_1000.txt") as file:
    count = 0
    for line in file:
        res = [int(i) for i in line.split()]
        if len(res) > 2:
            if number_to_find == res[1] or number_to_find == res[2]:
                count += 1
        print(count)


# importing the library
import numpy as np
import matplotlib.pyplot as plt
 
# data to be plotted
x = np.arange(1, 11)
y = np.array([100, 10, 300, 20, 500, 60, 700, 80, 900, 100])
 
# plotting
plt.title("Line graph")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.plot(x, y, color ="green")
plt.show()
