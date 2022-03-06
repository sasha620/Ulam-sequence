# read Ulam seq from a file
# build addend usage sequences
# plot approximate slopes on histogram

# importing the library
import numpy as np
import matplotlib.pyplot as plt
import FileNames
import math

# hey Sasha. this is how to use FileNames. Thanks Dad. :)
file_index = 7
file_name = "C:/ulam_data/addend-" + FileNames.get_file_name_suffix(file_index) + ".log"
last_number = FileNames.get_last_number(file_index)
n_lines_limit = round(math.sqrt(last_number))
print(file_name, last_number, n_lines_limit)


# Generates the Ulam sequence from file
with open (file_name) as file:
    file.seek(0)
    abridged_ulam_seq = [1,2]
    n_lines = 0
    for line in file:
        if n_lines == n_lines_limit:
            break
        n_lines += 1
        res = [int(i) for i in line.split()]
        abridged_ulam_seq.append(res[0])

Lambda = 2.44344296778474
slopes_inverse = []
slopes_regular = []

with open(file_name) as file:
    for number_to_find in abridged_ulam_seq:
            counts = []
            count = 0
            file.seek(0)
            for line in file:
                res = [int(i) for i in line.split()]
                if number_to_find == res[1] or number_to_find == res[0]-res[1]:
                    count += 1
                counts.append(count)
            if count > 10:
                x = range(len(counts))
                # For linearly growing numbers,
                slope = np.polyfit(x, counts, 1)[0]
                inverse_slope = np.reciprocal(slope)
                slopes_inverse.append(inverse_slope)
                slopes_regular.append(slope)

print(slopes_inverse)
print(slopes_regular)

plt.hist(slopes_inverse, bins = 20)
plt.savefig('slopes_inverse_of_linears_' + FileNames.get_file_name_suffix(file_index) + '.png')
plt.close()

plt.hist(slopes_regular, bins = 20)
plt.savefig('slopes_of_linears_' + FileNames.get_file_name_suffix(file_index) + '.png')
plt.close()

print("done")