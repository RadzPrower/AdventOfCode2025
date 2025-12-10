import copy
import itertools
from scipy.optimize import linprog
import numpy as np


def main(data):
    results = ""
    machine_list = []
    for line in data:
        machine_list.append(Machine(line))
    results += part1(machine_list)
    print(results)
    results += part2(machine_list)
    return results


def part1(machine_list):
    shortest_indicators = []
    for machine in machine_list:
        indicator_presses = machine.find_shortest_sequences()
        shortest_indicators.append(indicator_presses)
    return f"The fewest button presses required to configure indicator lights is {sum(shortest_indicators)}.\n"


def part2(machine_list):
    sum_of_results = 0
    for machine in machine_list:
        sum_of_results += machine.linprog_find_shortest_sequences()
    return f"The fewest button presses required to configure joltage levels is {int(sum_of_results)}.\n"


def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    results = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            results[j][i] = matrix[i][j]
    return results


class Machine:
    def __init__(self, input_line):
        indicator_target = []
        buttons = []
        joltage_target = []
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
                joltage_target = tuple(map(int, item.split(',')))
        self.indicators = [False] * len(indicator_target)
        self.indicator_target = tuple(indicator_target)
        self.buttons = tuple(buttons)
        self.joltage_target = joltage_target

    def press_button(self, button):
        index = self.buttons.index(button)
        for index in self.buttons[index]:
            self.indicators[index] = not self.indicators[index]

    def reset_indicators(self):
        self.indicators = [False] * len(self.indicator_target)

    def check_indicators(self):
        if tuple(self.indicators) == self.indicator_target:
            return True
        else:
            return False

    def linprog_find_shortest_sequences(self):
        obj = np.array([1] * len(self.buttons))
        A_eq = []
        for button in self.buttons:
            change = [0] * len(self.joltage_target)
            for index in button:
                change[index] += 1
            A_eq.append(change)
        A_eq = np.array(A_eq)
        b_eq = self.joltage_target
        integrality = [1] * len(self.buttons)
        results = linprog(obj, A_eq=A_eq.T, b_eq=b_eq, integrality=integrality)
        return np.sum(results.x)

    memory = {}
    def find_shortest_sequences(self):
        max_buttons = 1
        indicator_presses = 0
        press_indicator = True
        indicator_matches = False
        while not indicator_matches:
            combinations = itertools.combinations_with_replacement(self.buttons, r=max_buttons)
            for sequence in combinations:
                indicator_check = self.check_sequence(sequence, max_buttons)
                if indicator_check and press_indicator:
                    indicator_matches = True
                    indicator_presses = max_buttons
                    press_indicator = False
                    break
            max_buttons += 1
        return indicator_presses

    def check_sequence(self, sequence, max_buttons):
        if (sequence, max_buttons) in self.memory:
            return self.memory[(sequence, max_buttons, len(self.indicator_target))][:2]
        elif (sequence[:-1], max_buttons - 1, len(self.indicator_target)) in self.memory:
            previous = (
                self.memory)[sequence[:-1], max_buttons - 1, len(self.indicator_target)]
            indicator_matches = previous[0]
            self.indicators = copy.deepcopy(previous[1])
            self.press_button(sequence[-1])
        else:
            self.reset_indicators()
            indicator_matches = False
            for button in sequence:
                self.press_button(button)
        if self.check_indicators():
            indicator_matches = True
        self.memory[(sequence, max_buttons, len(self.indicator_target))] \
            = indicator_matches, copy.deepcopy(self.indicators)
        return indicator_matches