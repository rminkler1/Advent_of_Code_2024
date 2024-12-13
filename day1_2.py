from collections import Counter

right_list = []
left_list = []


with open("day1_1_input", "r") as file:

    line_of_file = file.readline()

    while line_of_file:

        split_file = line_of_file.split()

        left_list.append(split_file[0])
        right_list.append(split_file[1])

        line_of_file = file.readline()

right_list_counter = Counter(right_list)


similarity_score = 0

for key in left_list:
    if key in right_list_counter:
        similarity_score += int(key) * right_list_counter.get(key)

print(similarity_score)
# 28786472