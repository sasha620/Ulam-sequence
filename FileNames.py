# records for Ulam(2,n) data files
file_data = {
    # power of 10 => [file_name_suffix, last number]
    4:   ["02-00010,000", 9_985],
    5:   ["02-00100,000", 99_933],
    6:   ["02-01,000,000", 1_000_000],
    7:   ["02-10,000,000", 9_999_999],
    8:   ["02-100,000,000", 99_999_999],
    9:   ["02-1,000,000,000", 999_999_993],
    10:  ["02-1849036670", 1_560_575_835],
}
# number of lines:
#     825    addend-02-00010000.log
#    1297    addend-02-00016000.log
#    7582    addend-02-00100000.log
#   11997    addend-02-00160000.log
#   74082    addend-02-01000000.log
#  740366    addend-02-10000000.log
# 7399351    addend-02-100000000.log
# 73976840   addend-02-1000000000.log
# 115439266  addend-02-1849036670.log

def get_file_name_suffix(n):
    return file_data[n][0]

def get_last_number(n):
    return file_data[n][1]

# simple test
if __name__ == '__main__':
    # print(file_data)
    for n in range(4,9):
        print(f"power: {n}: suffix: {get_file_name_suffix(n)}, last number: {get_last_number(n)}")


