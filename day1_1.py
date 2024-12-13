right_list = []
left_list = []
distance = 0


with open("day1_1_input", "r") as file:

    line_of_file = file.readline()

    while line_of_file:

        split_file = line_of_file.split()

        left_list.append(split_file[0])
        right_list.append(split_file[1])

        line_of_file = file.readline()

right_list.sort()
left_list.sort()


for i, num in enumerate(left_list):
    distance += abs(int(num) - int(right_list[i]))

print(distance)
# 2430334