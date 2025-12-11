def main(data):
    result = ""
    result += part1(data)
    result += part2(data)
    return result


devices = {}
def part2(data):
    for line in data:
        label, outputs = line.split(': ')
        outputs = outputs.split()
        devices[label] = set(outputs)
    return f'Thera are {simplified_pathing('svr')} problematic paths.\n'


memory = {}
def simplified_pathing(device, dac=False, fft=False):
    if (device, dac, fft) in memory:
        return memory[(device, dac, fft)]
    if device == 'out':
        return dac and fft
    dac = dac or device == 'dac'
    fft = fft or device == 'fft'
    result = sum(simplified_pathing(output, dac=dac, fft=fft) for output in devices[device])
    memory[(device, dac, fft)] = result
    return result


def part1(data):
    devices_part1 = {}
    for line in data:
        label = line.split(': ')[0]
        devices_part1[label] = Device(label)
    devices_part1["out"] = Device("out")
    for line in data:
        label, outputs = line.split(': ')
        outputs = outputs.split()
        for output in outputs:
            devices_part1[label].outputs.append(devices_part1[output])
    paths = find_all_paths(devices_part1, "you", "out")
    result = f'There are {len(paths)} paths from \'you\' to \'out\'.\n'
    return result


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