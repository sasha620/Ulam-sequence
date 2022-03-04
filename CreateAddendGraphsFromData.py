# Goal: create addend graphs. 
# The addends of growing usage will be on the left and their residues right.

# importing the library
# TODO import the data (ex: Data-02-00010,000 --> AddendUsageSeq#.txt)
import FileNames
import math
import os
import numpy as np
import matplotlib.pyplot as plt

# First, create the graph space 
figure, axes = plt.subplots(2)
Lambda = 2.44344296778474

# determine the data folder
file_index = 4
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
            
# process each file
residues = []
residues_growing_addends = []
table_file_name = f"{data_folder}" + "/AddendSlopes.tsv"

with open(table_file_name) as table_file:
    n_line = 0
    for line in table_file:
        if n_line == 0:
            n_line += 1
        else:
            l=line.split('\t')
            res = [str(i) for i in line.split()]
            ulam_addends = int(res[0])
            count = int(res[2])
            residues.append((ulam_addends % Lambda)/Lambda)
            if count > 10:
                residues_growing_addends.append((ulam_addends % Lambda)/Lambda)


for data_file_name in data_files:
    # Second, extract the addend sequences for the given ulam seq length.
    # read the file
    addend_seq = []
    with open (data_file_name) as data_file:
        for line in data_file:
            addend_seq.append(line) #TODO do in one line
    # Determine parameters for graphing
    x = range(len(addend_seq))
    axes[0].plot(x,addend_seq) #TODO fix ticks for y-axis
    axes[0].set_title(f"Addend sequences for Ulam sequence length {len(addend_seq)}") #TODO

axes[1].hist(residues_growing_addends, bins = 60)
axes[1].set_xticks([0,1/3,2/3,1])

axes[0].grid(axis='x')
plt.savefig(f'Addend sequences for Ulam sequence length {len(addend_seq)}.png') #TODO
plt.show()
plt.close()

print(residues)
print(residues_growing_addends)