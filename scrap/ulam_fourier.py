import matplotlib.pyplot as plt
import numpy as np

file_name = r"C:\ulam_data\addend-02-1000000000.log" #73,976,840 lines, 999,999,993 last number
n_lines_limit = np.sqrt(80000000)

# Generates the Ulam sequence from file
with open (file_name) as file:
    file.seek(0)
    ulam_seq = [1,2]
    n_lines = 0
    for line in file:
        if n_lines >= n_lines_limit:
            break
        n_lines += 1
        res = [int(i) for i in line.split()]
        ulam_seq.append(res[0])

seq_normals = []
seq_outliers = []
ulam_numbers = []

with open(file_name) as file:
    for number_to_find in ulam_seq:
            counts = []
            count = 0
            file.seek(0)
            for line in file:
                res = [int(i) for i in line.split()]
                # if len(res) > 2:
                if number_to_find == res[1] or number_to_find == res[0]-res[1]:
                    count += 1
                counts.append(count)
            ulam_numbers.append(number_to_find)
            if count < 10:
                seq_normals.append(number_to_find)
            else:
                seq_outliers.append(number_to_find)

x = np.linspace(0,2*np.pi)
normal = 0
outlier = 0
ulam_number = 0

for elem in seq_normals:
    normal += np.cos(elem*x)


for i in seq_outliers:
    outlier += np.cos(i*x)


for number in ulam_numbers:
    ulam_number += np.cos(number*x)

z = 20*np.cos(x)


plt.plot(x,normal, color = 'blue', label='normals')
plt.plot(x,z, label='20*cos(x)')
plt.plot(x,outlier, color = 'green', label= 'outliers')
plt.plot(x,ulam_number, color= 'black', label = 'ulam numbers')

plt.legend()
plt.savefig('fourier_cosines.png')
plt.show()
