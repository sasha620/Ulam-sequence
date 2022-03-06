# read Ulam seq from a file
# build addend usage sequences
# plot approximate slopes on histogram

# importing the library
import numpy as np
import matplotlib.pyplot as plt
import FileNames
import math
import os

# input Ulam sequence file
file_index = 7 #TODO 8,9,10 for storage outside of Dropbox
file_suffix = FileNames.get_file_name_suffix(file_index)
ulam_file_name = "C:/ulam_data/addend-" + file_suffix + ".log"
last_number = FileNames.get_last_number(file_index)
n_lines_limit = round(math.sqrt(last_number))
data_folder = "Data-" + file_suffix
print(ulam_file_name, last_number, n_lines_limit)

# Generates abridged Ulam sequence from file
with open (ulam_file_name) as ulam_file:
    abridged_ulam_seq = [1,2]
    n_lines = 0
    for line in ulam_file:
        if n_lines == n_lines_limit:
            break
        n_lines += 1
        res = [int(i) for i in line.split()]
        abridged_ulam_seq.append(res[0])


    # create directory called Data-file_suffix; create count and slopes file called AddendSlopes
    if not os.path.isdir(data_folder):
        os.mkdir(data_folder)
    addend_slope_file_name = data_folder + "/AddendSlopes.tsv"
    with open (addend_slope_file_name, "w") as addend_slope_file:
        addend_slope_file.writelines("number_to_find" "\t" "slope" "\t" "count" "\n")

        # compute Ulam addend usage sequences (counts)
        for number_to_find in abridged_ulam_seq:
            counts = []
            count = 0
            ulam_file.seek(0)
            for line in ulam_file:
                res = [int(i) for i in line.split()]
                if number_to_find == res[1] or number_to_find == res[0]-res[1]:
                    count += 1
                counts.append(count)

            # record last number and slope
            slope = count / len(counts)
            addend_slope_file.write(str(number_to_find) +"\t"+ str(slope) +"\t"+ str(count) +"\n")

            # if this seqeunce flat?
            if count <= 10:
                # no need to record flat sequences
                continue
            # put non-flat sequences in files
            addend_usage_seq_file_name = data_folder + f"/AddendUsageSeq{number_to_find}.txt"
            with open (addend_usage_seq_file_name, "w") as addend_usage_seq_file:
                for elem in counts:
                    addend_usage_seq_file.writelines(str(elem) + "\n")


print("done")