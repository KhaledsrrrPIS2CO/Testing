"""help(hex)
print(hex(10))

a  = 5
b = 4
c = a == b
print(c)

print("wow")
import datetime

khaled = datetime.date(1992, 2, 29)
Shaima = datetime.date(1994, 11, 12)


print(khaled.strftime("%A, %B %d, %Y"))
print(Shaima.strftime("%A, %B %d, %Y"))
shaimaDay = (Shaima.strftime("%A"))
khaledDay = (khaled.strftime("%A"))
print("Khaled's day is", khaledDay)
print("Shaimaa's day is", shaimaDay)

if shaimaDay == khaledDay:
    print("wow")
"""


# functions

def f():
    pass


f()


# real fun
def ping():
    return "Ping!"


ping()
x = ping()
print(x)

import math

pi = math.pi
print("the pi is:", pi)


def volume(r):
    """the fun retrusn volume of sphere radius with r"""
    v = (4.0 / 3.0) * pi * r ** 3
    return v


print("the volume is:", volume(2))


def triangle_area(b, h):
    """returns the area of a triangle with b base and h height."""
    return 0.5 * b * h


print("the triangle area is", triangle_area(3, 6))


def cm(feet=0, inches=0):
    """converts length from feet and inches to cm"""
    inches_to_cm = inches * 2.54
    feet_to_cm = feet * 12 * 2.54
    return inches_to_cm + feet_to_cm


cm(feet=5)
print("feet to cm:", cm(5))
cm(inches=70)
print("inches to cm", cm(70))


def test_required_argu(y, x=1):
    return x + y

print(test_required_argu(5,3))
