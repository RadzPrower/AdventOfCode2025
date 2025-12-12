def main(data):
    results = 0
    regions, presents = parse_data(data)
    for i, region in enumerate(regions):
        region_area = region[0] * region[1]
        presents_area = sum(presents[i]) * 9
        if presents_area <= region_area:
            results += 1
    return f'{results} regions can fit their listed presents.'

def parse_data(data):
    region_list = []
    presents_list = []
    for i in range(30,len(data)):
        region, presents = data[i].split(': ')
        region = tuple(map(int, region.split('x')))
        presents = tuple(map(int, presents.split()))
        region_list.append(region)
        presents_list.append(presents)
    return region_list, presents_list