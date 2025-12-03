def main(data):
    return "The total output joltage is " + str(calculate_joltage(data, False)) + " with safeties overridden.\n"

def calculate_joltage(data, safeties=True):
    joltage = 0
    for line in data:
        indices = []
        last_index = -1
        digits = []
        joltage_string = ""
        if safeties: length = 2
        else: length = 12
        for i in range(0, 10):
            indices.append([pos for pos, char in enumerate(line) if char == str(i)])
        for i in reversed(range(0, 10)):
            if indices[i] != [] and (len(line) - indices[i][0]) >= length:
                digits.append(i)
                last_index = indices[i][0]
                break
        while len(digits) < length:
            digit_added = False
            for i in reversed(range(0, 10)):
                if digit_added: break
                if indices[i]:
                    for j, index in enumerate(indices[i]):
                        if digit_added: break
                        if index > last_index and (len(line) - index) >= (length - len(digits)):
                            digits.append(i)
                            last_index = indices[i][j]
                            digit_added = True
        for digit in digits:
            joltage_string += str(digit)
        joltage += int(joltage_string)
    return joltage