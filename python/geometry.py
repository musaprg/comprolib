import math

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.eps = 1e-10

    def abs(self):
        return math.sqrt(self.norm())

    def norm(self):
        return self.x**2 + self.y**2

    def __add__(self, other):
        if not isinstance(other, __class__):
            raise TypeError
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if not isinstance(other, __class__):
            raise TypeError
        return Point(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        if not isinstance(other, __class__):
            raise TypeError
        return Point(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        if not isinstance(other, __class__):
            raise TypeError
        return Point(self.x / other.x, self.y / other.y)

    def __floordiv__(self, other):
        if not isinstance(other, __class__):
            raise TypeError
        return Point(self.x // other.x, self.y // other.y)

    def __lt__(self, other):
        return self.x < other.x if self.x != other.x else self.y < other.y

    def __eq__(self, other):
        return abs(self.x - other.x) < self.eps and abs(self.y - other.y) < self.eps

    def __str__(self):
        return "".join(["(", str(self.x), ",", str(self.y), ")"])

    __repr__ = __str__


class Segment:
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2


def dot(a: Vector, b: Vector):
    return a.x * b.x + a.y * b.y

def cross(a: Vector, b: Vector):
    return a.x * b.y - a.y * b.x

def ccw(p0: Point, p1: Point, p2: Point):
    eps = 1e-10
    a = p1 - p0
    b = p2 - p0

    if cross(a, b) > eps:
        return 1 # COUNTER_CLOCKWISE
    if cross(a,b) < eps:
        return -1 # CLOCKWISE
    if dot(a,b) < -eps:
        return 2 # ONLINE_BACK
    if a.norm() < b.norm():
        return -2 # ONLINE_FRONT

    return 0 # ON_SEGMENT


def intersect_p(p1: Point, p2: Point, p3: Point, p4: Point):
    return ( ccw(p1, p2, p3) * ccw(p1, p2, p4) <= 0 and ccw(p3, p4, p1) * ccw(p3, p4, p2) <= 0)

def intersect_s(s1: Segment, s2: Segment):
    return intersect_p(s1.p1, s1.p2, s2.p1, s2.p2)

def get_distance(a: Point, b: Point):
    return abs(a - b)

def get_distance_lp(l: Segment, p: Point):
    return abs( cross(l.p2 - l.p1, p - l.p1) / abs(l.p2 - l.p1))

def get_distance_sp(s: Segment, p: Point):
    if dot(s.p2 - s.p1, p - s.p1) < 0.0:
        return abs(p - s.p1)
    if dot(s.p1 - s.p2, p - s.p2) < 0.0:
        return abs(p - s.p2)
    return get_distance_p(s, p)

def get_distance(s1: Segment, s2: Segment):
    if intersect_s(s1, s2):
        return 0.0
    return min(min(get_distance_sp(s1, s2.p1), get_distance_sp(s1, s2.p2),
               min(get_distance_sp(s2, s1.p1), get_distance_sp(s2, s1.p2)))
