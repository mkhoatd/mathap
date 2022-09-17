import random
random.seed(0)
points = [(random.randint(0, 100), random.randint(0, 100)) for i in range(50)]
convex_hull = []
points.sort(key=lambda x: [x[0], x[1]])
start = points.pop(0)

def slope(p1, p2):
    if p1[0] == p2[0]:
        return float('inf')
    else:
        return 1.0*(p1[1]-p2[1])/(p1[0]-p2[0])

points.sort(key=lambda p: (slope(p, start), -p[1], p[0]))


def cross_product(p1, p2, p3):
    return ((p2[0] - p1[0])*(p3[1] - p1[1])) - ((p2[1] - p1[1])*(p3[0] - p1[0]))

convex_hull.append(start)
for point in points:
    convex_hull.append(point)
    while len(convex_hull) > 2 and cross_product(convex_hull[-3], convex_hull[-2], convex_hull[-1]) < 0:
        convex_hull.pop(-2)

print("points:", points,'\n\n')
print("convex hull:", convex_hull)