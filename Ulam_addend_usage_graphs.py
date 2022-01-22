# read Ulam seq from a file
# build addend usage sequences
# create graphs, dividing the addend usage sequences by frequency of usage

# importing the library
import numpy as np
import matplotlib.pyplot as plt

file_name = r"C:\ulam_data\addend-02-10,000,000.log" # 740,366 lines, last number 9,999,999
n_lines_limit = 300

# Initialise the subplot function using number of rows and columns
figure, axes = plt.subplots(2,2)

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

histogram_residue_growing_numbs = []
histgrm_residue_horz = []
Lambda = 2.44344296778474
slopes_inverse = []

with open(file_name) as file:
    for number_to_find in abridged_ulam_seq:
            counts = []
            count = 0
            file.seek(0)
            for line in file:
                res = [int(i) for i in line.split()]
                # if len(res) > 2:
                if number_to_find == res[1] or number_to_find == res[0]-res[1]:
                    count += 1
                counts.append(count)
            if count > 10:
                x = range(len(counts))
                # For linearly growing numbers,
                axes[0, 0].plot(x,counts, label=f"{number_to_find}")
                axes[0, 0].set_title("Linear-growing")
                model = np.polyfit(x, counts, 1)
                predict = np.poly1d(model)
                y_lin_reg = predict(x)
                axes[0,0].plot(x, y_lin_reg, color = 'black')
                slopes_inverse.append(1/model[0])

                # plot results these number_to_find mod (%) lambda                
                histogram_residue_growing_numbs.append((number_to_find % Lambda)/Lambda)
                # axes[1,0].set_title("Numbers mod lambda divided by lambda")
            else:
                # For other horizontal ones
                axes[0, 1].plot(counts)
                axes[0, 1].set_title("Horizontal")  
                histgrm_residue_horz.append((number_to_find % Lambda)/Lambda)
    # print(f"Results for finding {number_to_find}:\n{counts}.")

axes[1,0].hist(histogram_residue_growing_numbs, bins = 60)
axes[1,1].hist(histgrm_residue_horz, bins = 60)
# axes[0,0].legend(loc='best')

axes[1,0].set_xticks([0,1/3,2/3,1])
axes[1,1].set_xticks([0,1/3,2/3,1])

axes[1,0].grid(axis='x')
axes[1,1].grid(axis='x')
plt.savefig('ulam_general_graph_10,000,000.png')
plt.show()
plt.close()

plt.hist(histogram_residue_growing_numbs, bins = 10, label = 'outliers linearly growing')
plt.hist(histgrm_residue_horz, bins = 10, color = 'red', label = 'regular flats')
plt.legend()
plt.savefig('ulam_residues_10,000,000.png')
plt.close()

plt.hist(slopes_inverse, bins = 200)
plt.savefig('slopes_inverse_of_linears_10,000,000.png')
plt.close()

print("done")
# IMPORTANT: do linear regression and find slope + closeness to linear functions on the linear growing numbers.
# to do: add FileNames to this code too.