number_to_find = 2

with open("UlamData_1_2_1000.txt") as file:
    count = 0
    for line in file:
        res = [int(i) for i in line.split()]
        if len(res) > 2:
            if number_to_find == res[1] or number_to_find == res[2]:
                count += 1
        print(count)
