import re   # Regex magic

enabled = True  # switch to determine if we skip or process results.
result = 0

with open("day_3_input.txt", "r") as txt:

    # read each line of the file
    next_line = txt.readline()

    while next_line:
        # Regex to pull out all matching results into an array
        # "mul(##,##)" or "do()" or "don't()"
        this_line_list = re.findall(r"mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)", next_line)

        # Process the current line and add the results to result
        for entry in this_line_list:
            if entry == "do()":
                enabled = True
            elif entry == "don't()":
                enabled = False
            elif enabled:
                numbers = entry.strip("mul()")
                split_numbers = numbers.split(",")
                result += int(split_numbers[0]) * int(split_numbers[1])

        # Get the next line to continue
        next_line = txt.readline()

print(result)
