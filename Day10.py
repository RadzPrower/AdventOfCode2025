import itertools

def main(data):
    machine_list = []
    for line in data:
        machine_list.append(Machine(line))
    shortest_sequences = []
    for machine in machine_list:
        shortest_sequences.append(machine.find_shortest_sequence())
        continue
    return f"The fewest button presses required to configure indicator lights is {sum(shortest_sequences)}."


class Machine:
    def __init__(self, input_line):
        indicator_target = []
        buttons = []
        joltage = []
        input_line = input_line.split()
        for item in input_line:
            if '[' in item:
                for char in item:
                    match char:
                        case '.':
                            indicator_target.append(False)
                        case '#':
                            indicator_target.append(True)
            if '(' in item:
                item = item.replace('(','').replace(')','')
                buttons.append(tuple(map(int, item.split(','))))
            if '{' in item:
                item = item.replace('{','').replace('}','')
                joltage.append(tuple(map(int, item.split(','))))
        self.indicators = [False] * len(indicator_target)
        self.indicator_target = tuple(indicator_target)
        self.buttons = tuple(buttons)
        self.joltage = tuple(joltage)

    def press_button(self, button):
        index = self.buttons.index(button)
        for light in self.buttons[index]:
            self.indicators[light] = not self.indicators[light]

    def reset_indicators(self):
        self.indicators = [False] * len(self.indicator_target)

    def check_indicators(self):
        if tuple(self.indicators) == self.indicator_target:
            return True
        else:
            return False

    def find_shortest_sequence(self):
        max_buttons = 1
        while not self.check_indicators():
            permutations = itertools.permutations(self.buttons, r=max_buttons)
            for sequence in permutations:
                self.reset_indicators()
                for button in sequence:
                    self.press_button(button)
                    if self.check_indicators():
                        return max_buttons
            max_buttons += 1
        return max_buttons