import math
import statistics


def area(r):
    """Area of a circel with radius r"""
    return math.pi * (r ** 2)


radii = [2, 5, 7.1, 0.3, 10]

areas = []
for r in radii:
    a = area(r)
    areas.append(a)

print(areas)

map(area, radii)
print(map)

list = list(map(area, radii))
print(list)

pnl_data = [16, 15, -30, -15, 35, 11, -18, 27, -8, -26, 137, 12, 8, 15, 19, 51]
pnl_avg = statistics.mean(pnl_data)
print(pnl_avg)

for pnl in pnl_data:
    if pnl>0:
        green_days_counter = []
    red_days= pnl<0
    print(green_days)
    print(red_days)

filter(lambda x: x > pnl_avg, pnl_data)
print(filter(lambda x: x > pnl_avg, pnl_data))

