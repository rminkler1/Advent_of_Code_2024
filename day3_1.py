import re

mult_list = []
result = 0

with open("day_3_input.txt", "r") as txt:
    next_line = txt.readline()

    while next_line:
        this_line_list = re.findall(r"mul\([0-9]+,[0-9]+\)", next_line)
        mult_list.extend(this_line_list)
        next_line = txt.readline()

for entry in mult_list:
    numbers = entry.strip("mul()")
    split_numbers = numbers.split(",")

    result += int(split_numbers[0]) * int(split_numbers[1])

print(result)


