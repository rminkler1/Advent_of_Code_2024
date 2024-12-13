safe_reports_count = 0


with open("day2_1_input", "r") as file:

    line_of_file = file.readline()

    while line_of_file:

        # default values
        this_line_safe = True

        # read the next line
        split_levels = line_of_file.split()

        # are the first two numbers in the line increasing or decreasing
        is_increasing = int(split_levels[0]) < int(split_levels[1])

        for i in range(len(split_levels) - 1):
            # calculate the difference of i and i+1
            difference = int(split_levels[i]) - int(split_levels[i + 1])
            if not ((is_increasing and -4 < difference < 0) or (not is_increasing and 0 < difference < 4)):
                this_line_safe = False
                break

        # if still safe after all values processed, add to safe count
        if this_line_safe:
            safe_reports_count += 1

        # read next line of file
        line_of_file = file.readline()


print(safe_reports_count)
