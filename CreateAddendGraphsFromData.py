# Goal: create addend graphs. 
# The addends of growing usage will be on the left and their residues right.

# importing the library
import FileNames
import math
import os
import numpy as np
import matplotlib.pyplot as plt

# First, create the graph space 
figure, axes = plt.subplots(2)
Lambda = 2.44344296778474

# determine the data folder
file_index = 8
file_suffix = FileNames.get_file_name_suffix(file_index)
data_folder = "Data-" + file_suffix
print(data_folder)


# find all files in the folder
path = rf"{data_folder}"
data_files = []
data_files_for_res = []

for root, directories, files in os.walk(path):
	for file in files:
		if(file.endswith(".txt")):
			data_files.append(os.path.join(root,file))
            
# process tsv file
residues = []
residues_growing_addends = []
residues_flat_addends = []
table_file_name = f"{data_folder}" + "/AddendSlopes.tsv"

with open(table_file_name) as table_file:
    n_line = 0
    for line in table_file:
        if n_line == 0:
            n_line += 1
        else:
            row_values = line.split()
            ulam_addend = int(row_values[0])
            count = int(row_values[2])
            residue = (ulam_addend % Lambda)/Lambda
            # residues.append(residue)
            if count > 10:
                residues_growing_addends.append(residue)
            else:
                residues_flat_addends.append(residue)


# process each growing sequence
axes[0].set_title("Growing addend sequences")
for data_file_name in data_files:
    # Second, extract the addend sequences for the given ulam seq length.
    # read the file
    addend_seq = []
    with open (data_file_name) as data_file:
        for line in data_file:
            addend_seq.append(line) #TODO do in one line
    # Determine parameters for graphing
    x = range(len(addend_seq))
    axes[0].plot(x,addend_seq) 

axes[1].set_title("Addend residues")
axes[1].hist(residues_growing_addends, bins = 60, label = 'Growing addends residue')
axes[1].hist(residues_flat_addends, bins = 60, color = 'red', label = 'Flat addends residue')
axes[1].set_xticks([0,1/3,2/3,1])
axes[1].legend()

axes[0].grid(axis='x')
axes[0].set_yticks([0, len(addend_seq)/9, 2*len(addend_seq)/9, len(addend_seq)/3])
plt.savefig(f'{data_folder}/Addend sequences and residues.png')
plt.show()
plt.close()

# print(residues)
# print(residues_growing_addends)
print("done")