def main(data):
    data = trim_data(data)
    result = part1(data)
    result += part2(data)
    return result


# Not really a necessity, but I pre-screen the data to clear out empty lines in a single pass
def trim_data(data):
    trimmed_data = []
    for x in range(0, len(data), 2):
        trimmed_data.append(data[x])
    return trimmed_data


# My own solution to part 1, though it may be slightly different from the original version which gave
# me the correct answer as I have been tweaking it here and there to try and solve part 2 before
# cutting it all out to try and work on a separate solution.
def part1(data):
    split_count = 0
    beams = []
    for line in data:
        if '^' in line:
            splitter_indices = [i for i, value in enumerate(line) if value == '^']
            for splitter in splitter_indices:
                if splitter in beams:
                    while splitter in beams:
                        beams.remove(splitter)
                    beams.append(splitter - 1)
                    beams.append(splitter + 1)
                    split_count += 1
        elif 'S' in line:
            beams.append(line.find('S'))
        continue
    return "The beam would be split " + str(split_count) + " times.\n"


# Lightly modified version of Tony B from resetera's solution for part 2 as I was just up against
# a wall. It is fundamentally identical, but was rewritten a line at a time in a style more my own
# despite the logic being the same. Not trying to hide that it's not my code, but I still wanted it
# to be stylistically consistent with my own code.
def part2(data):
    beams_timeline = {data[0].find('S'): 1}
    row = 1
    while True:
        next_beams_timeline = {}
        for beam, timelines in beams_timeline.items():
            if data[row][beam] == ".":
                next_beams_timeline[beam] = next_beams_timeline.get(beam, 0) + timelines
            else:
                left = beam - 1
                right = beam + 1
                next_beams_timeline[left] = next_beams_timeline.get(left, 0) + timelines
                next_beams_timeline[right] = next_beams_timeline.get(right, 0) + timelines
        beams_timeline = next_beams_timeline
        row += 1
        if row >= len(data):
            break
    return "The beam would result in " + str(sum(beams_timeline.values())) + " timelines.\n"