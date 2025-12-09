import shapely
from shapely import polygons,box

def main(data):
    # Generate list of points
    points = []
    polygon_points = []
    for line in data:
        x, y = map(int, line.split(','))
        points.append(Point(x, y))
        polygon_points.append([x, y])
    # Use polygon_points to create a shapely polygon
    green_tiles = polygons(polygon_points)
    # Create all possible Point pairs
    pairs = []
    green_pairs = []
    for point_1 in points:
        for point_2 in points:
            if point_1 != point_2:
                pairs.append(frozenset([point_1, point_2]))
                square = box(point_1.x, point_1.y, point_2.x, point_2.y)
                if green_tiles.contains(square):
                    green_pairs.append(frozenset([point_1, point_2]))
    # Find largest rectangle
    rect_sizes = {}
    green_rect_sizes = {}
    for pair in pairs:
        rect_sizes[pair]=rectangle_size(pair)
        if pair in green_pairs:
            green_rect_sizes[pair]=rectangle_size(pair)
    result = f"The largest rectangle possible is {max(rect_sizes.values())} tiles.\n"
    result += (f"The largest rectangle possible with only green and red tiles is "
               f"{max(green_rect_sizes.values())} tiles.\n")
    return result


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