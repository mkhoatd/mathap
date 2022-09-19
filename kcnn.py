import random
import math


def dist(a: 'tuple[int]', b: 'tuple[int]') -> 'float':
    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)


def find(l:)


if __name__=="__main__":
    random.seed(0)
    points = [(random.randint(0, 100), random.randint(0, 100)) for i in range(50)]
    points.sort(key=lambda x: x[0])
