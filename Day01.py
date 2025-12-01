def main(data):
    dial = 50
    basic_password = 0
    complex_password = 0
    for line in data:
        direction = line[:1]
        distance = int(line[1:])
        if distance > 99:
            complex_password += distance//100
            distance = distance%100
        if direction == 'L':
            dial -= distance
        else:
            dial += distance
        if dial > 99:
            dial = abs(dial)%100
            if dial != 0:
                complex_password += 1
        elif dial < 0:
            dial += 100
            if dial != 0 and dial + distance != 100:
                complex_password += 1
        if dial == 0:
            basic_password += 1
            complex_password += 1
    result = "The basic password is " + str(basic_password) + ".\n"
    result += "The 0x434C49434B password is " + str(complex_password) + ".\n"
    return result