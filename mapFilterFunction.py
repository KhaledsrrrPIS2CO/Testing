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

pnl_data = [-12, 16, 15, -30, -15, 35, 11, -18, 27, -8, -26, 137, 12, 8, 15, 19, 51]
pnl_avg = statistics.mean(pnl_data)
print("my avg pnl since 26.08.22:",pnl_avg)
green_days = [pnl for pnl in pnl_data if pnl > 0]
print("since 26.08.22")
print("theeee greeen days:::",green_days)
red_days = [pnl for pnl in pnl_data if pnl < 0]
print("urrr red days are: ", red_days)

# sorting
KSYZ_Capital = ["khaled", "shaima", "Yahya", "Zakarria"]
print("the list in reverse order:", KSYZ_Capital.sort(reverse=False))
print("this the sorted:", sorted(KSYZ_Capital))

#files
#text files e.g. plain text XML JSON Source code
#bianary files
ksyz_teaam= ["khaled", "shaima", "yahya","Zak"]
with open("names.txt", "w") as f:
    for name in ksyz_teaam:
        f.write(name)
        f.write("\n")

with open("daily pnl", "w") as f:
    for pnl in pnl_data:
        f.write(str(pnl))
        f.write("\n")
    f.write("Haha")
print(property)


