def main(data):
    result = ""
    # Create all our 3D points and circuits
    circuits = []
    points_list = []
    for i, line in enumerate(data):
        x, y, z = map(int, line.split(','))
        points_list.append(Point(x, y, z))
        circuits.append({line})
    # Determine distances between each of our 3D points
    pairs_dict = {}
    for point_2 in points_list:
        for point_1 in points_list:
            if point_1 != point_2:
                key_a = (str(point_1), str(point_2))
                key_b = (str(point_2), str(point_1))
                if key_a not in pairs_dict and key_b not in pairs_dict:
                    pairs_dict[(str(point_1), str(point_2))] = point_1.distance(point_2)
    # Sort our dictionary by the distance value
    pairs_dict = {key: value for key, value in sorted(pairs_dict.items(), key=lambda item: item[1])}
    # Place our junctions into circuits
    count = 0
    done = False
    if len(data) > 30:
        pair_count = 1000
    else:
        pair_count = 10
    for pair in pairs_dict:
        count += 1
        # Once we've hit our expected connections count we will find the product
        if count > pair_count and not done:
            product = 1
            for i in range(3):
                product *= len(circuits[i])
                done = True
            result = "The three largest circuits' product is " + str(product) + ".\n"
        if not circuits:
            circuits.append({pair[0], pair[1]})
            continue
        found = False
        for circuit in circuits:
            if pair[0] in circuit or pair[1] in circuit:
                circuit.add(pair[0])
                circuit.add(pair[1])
                found = True
        if not found:
            circuits.append({pair[0], pair[1]})
        circuits = consolidate_circuits(circuits)
        if len(circuits) == 1: break
    junction_1 = int(pair[0].split(',')[0])
    junction_2 = int(pair[1].split(',')[0])
    final_connection_product = junction_1 * junction_2
    result += "The product of the final connection is " + str(final_connection_product) + ".\n"
    return result


def consolidate_circuits(circuits):
    consolidated_circuits = []
    for circuit in circuits:
        if not consolidated_circuits:
            consolidated_circuits.append(circuit)
        else:
            found = False
            for new_circuit in consolidated_circuits:
                if len(circuit.intersection(new_circuit)) > 0:
                    new_circuit.update(circuit)
                    found = True
            if not found:
                consolidated_circuits.append(circuit)
    overlap = False
    for circuit_1 in consolidated_circuits:
        for circuit_2 in consolidated_circuits:
            if circuit_1 != circuit_2:
                if len(circuit_1.intersection(circuit_2)):
                    overlap = True
    if overlap:
        return consolidate_circuits(consolidated_circuits)
    else:
        consolidated_circuits.sort(key=len, reverse=True)
        return consolidated_circuits


# A 3D point class
class Point:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'{self.x},{self.y},{self.z}'

    def distance(self, point):
        square_x = (self.x - point.x)**2
        square_y = (self.y - point.y)**2
        square_z = (self.z - point.z)**2
        return (square_x + square_y + square_z)**.5