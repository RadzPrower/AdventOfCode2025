def main(data):
    return part1(data) + part2(data)


# Bespoke solution for part 1
def part1(data):
    values = []
    total_sum = 0
    for line in data:
        if '+' in line or '*' in line:
            values.append((line.split()))
        else:
            values.append([int(x) for x in line.split()])
    for i in range(len(values[-1])):
        current_value = 0
        current_index = len(values) - 1
        if values[current_index][i] == '+':
            addition = True
        else:
            addition = False
        while current_index > 0:
            current_index -= 1
            if addition:
                current_value += values[current_index][i]
            elif current_value == 0:
                current_value = values[current_index][i]
            else:
                current_value *= values[current_index][i]
        total_sum += current_value
    return "The total sum of all the human answers is " + str(total_sum) + ".\n"


# Bespoke solution for part 2
def part2(data):
    total_sum = 0
    parsed_data = cephalopod_parse(data)
    for j in reversed(range(len(parsed_data[0]))):
        values = []
        for i in range(len(parsed_data)):
            if '+' in parsed_data[i][j]:
                total_sum += cephalopod_math(values)
            elif '*' in parsed_data[i][j]:
                total_sum += cephalopod_math(values, False)
            else:
                values.append(parsed_data[i][j])
    return "The total sum of all the cephalopod answers is " + str(total_sum) + ".\n"

# This does the basic cephalopod math with a flag for addition/multiplication since the bulk of the parsing
# needed is identical, but to pull that shared functionality out was messier than simply introducing a flag
def cephalopod_math(values, addition=True):
    result = 0
    for j in reversed(range(len(values[0]))):
        number = ''
        for i in range(len(values)):
            number += values[i][j]
        if addition:
            result += int(number)
        elif result == 0:
            result = int(number)
        else:
            result *= int(number)
    return result


# Parse data in a cephalopod-friendly way
def cephalopod_parse(data):
    j = 0
    max_string_length = 0
    segment_start = 0
    cephalopod_data = []
    for x in range(len(data)):
        cephalopod_data.append([])
        if len(data[x]) > max_string_length:
            max_string_length = len(data[x])
    for x in range(len(data)):
        data[x] = data[x].ljust(max_string_length)
    done = False
    while not done:
        char_set = set()
        for i in range(len(data)):
            char_set.add(data[i][j])
        if char_set == {' '}:
            cephalopod_data, segment_start = add_to_dataset(cephalopod_data, data, j, segment_start)
        j += 1
        if j >= max_string_length:
            cephalopod_data, segment_start = add_to_dataset(cephalopod_data, data, j, segment_start)
            done = True
    return cephalopod_data


# Parse and format the data out such that it maintains its spacing when broken up into individual "columns"
def add_to_dataset(cephalopod_data, data, j, segment_start):
    for i in range(len(data)):
        cephalopod_data[i].append(data[i][segment_start:j])
    return cephalopod_data, j + 1