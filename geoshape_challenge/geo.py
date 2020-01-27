import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Multipolygon:
    def __init__(self, points: [Point]):
        self.points = self.__normalize_polygon(points)

    def __normalize_polygon(self, points: [Point]) -> [Point]:
        points = self.__first_final_points(points)

    def __first_final_points(self, points: [Point]) -> [Point]:
        if points[0] == points[-1]:
            return points
        if __has_equal_points(points):
            
        
    

def distance_points(a: Point, b: Point):
    diff_x = square_difference(a.x, b.x)
    diff_y = square_difference(a.y, b.y)
    return math.sqrt(diff_x + diff_y)

def square_difference(a, b):
    return (a - b)**2

