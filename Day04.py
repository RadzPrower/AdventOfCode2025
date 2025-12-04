# Our array of column and row offsets to avoid setting these repeatedly
offset_column = [-1, -1, -1, 0, 0, 1, 1, 1]
offset_row = [-1, 0, 1, -1, 1, -1, 0, 1]

def main(data):
    finished = False
    total_accessible_rolls = 0
    string_to_list(data)
    while not finished:
        removals = []
        accessible_rolls = 0
        for x, line in enumerate(data):
            for y, row in enumerate(data[x]):
                if data[x][y] == '@':
                    if can_access_roll(data,x, y):
                        accessible_rolls += 1
                        removals.append((x, y))
        if accessible_rolls == 0:
            finished = True
            break
        total_accessible_rolls += accessible_rolls
        remove_rolls(data, removals)
    return "There are a total of " + str(total_accessible_rolls) + " accessible rolls."

# Determine if a roll at the provided coordinates in the provided map can be accessed
def can_access_roll(data, x, y):
    roll_count = 0
    for i in range(8):
        a = x + offset_column[i]
        b = y + offset_row[i]
        if 0 <= a < len(data[0]) and 0 <= b < len(data):
            if data[a][b] == '@':
                roll_count += 1
                if roll_count >= 4: return False
    return True

# Remove the provided list of rolls from the wall
def remove_rolls(data, removals):
    for x, y in removals:
        data[x][y] = 'X'
    return

# Convert raw data to list matrix of characters
def string_to_list(data):
    for i, line in enumerate(data):
        data[i] = list(line)
    return