def main(data):
    # Generate list of points
    points = []
    for line in data:
        x, y = map(int, line.split(','))
        points.append(Point(x, y))
    # Create all possible Point pairs
    pairs = []
    for point_1 in points:
        for point_2 in points:
            if point_1 != point_2:
                pairs.append(frozenset([point_1, point_2]))
    # Find largest rectangle
    rect_sizes = {}
    for pair in pairs:
        rect_sizes[pair]=rectangle_size(pair)
    return f"The largest rectangle possible is {max(rect_sizes.values())} tiles."


def rectangle_size(pair):
    x = []
    y = []
    for point in pair:
        x.append(point.x)
        y.append(point.y)
    width = abs(x[0] - x[1]) + 1
    height = abs(y[0] - y[1]) + 1
    return width * height

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x},{self.y})'