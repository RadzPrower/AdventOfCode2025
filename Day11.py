from functools import lru_cache


def main(data):
    devices = {}
    for line in data:
        label = line.split(': ')[0]
        devices[label] = Device(label)
    devices["out"] = Device("out")
    for line in data:
        label, outputs = line.split(': ')
        outputs = outputs.split()
        for output in outputs:
            devices[label].outputs.append(devices[output])
    paths = find_all_paths(devices, "you", "out")
    svr_paths = find_all_paths(devices, "svr", "out")
    problem_paths = []
    for path in svr_paths:
        if 'dac' in path and 'fft' in path:
            problem_paths.append(path)
    result = f'There are {len(paths)} paths from \'you\' to \'out\'.\n'
    result += f'There are {len(problem_paths)} two problematic paths.\n'
    return result

memory = {}
def find_all_paths(devices, start, end, path=[]):
    if (start, end, tuple(path)) in memory:
        return memory[(start, end, tuple(path))]
    path = path + [start]
    if start == end:
        return [path]
    if start not in devices:
        return []
    paths = []
    for device in devices[start].outputs:
        if device not in path:
            new_paths = find_all_paths(devices, device.label, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    memory[(start, end, tuple(path))] = paths
    return paths

class Device:
    def __init__(self, label):
        self.label = label
        self.outputs = []

    def __str__(self):
        return f'{self.label}: {self.outputs}'