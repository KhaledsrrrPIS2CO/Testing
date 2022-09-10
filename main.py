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


print(test_required_argu(5, 3))

# list, tuple, dictionaries, sets
# set of pp
example = set()
example.add(-18)
example.add(False)
example.add(math.pi)
example.add("was OTM -> ATM -> ITM")
print("this is your set:", example)

example.add(-18)
print("this is the second print:", example)
print(len(example))
example.remove(-18)
print("the set after remocal:", example)
print(len(example))

evens = set([2, 4, 6, 8, 10])
odds = set([1, 3, 5, 7, 9])

print(odds)
print(evens)
print(odds.union(evens))
print("intersectin of O and E:", odds.intersection(evens))
print(2 in evens)
print(9 not in evens)

# lists
list_list = [1, 2, 3, 4, 5, 6, 7, 8]
list_list.append(14)
print(list_list)
print(type(list_list))
print(type(evens))
set11 = {"hi", "hello"}
print(set11)
set11.add(1)
print(set11)
print(type(set11))
print(list_list[0])
print(list_list[-1])

user_id = 209
message = "Hi"
language = "English"
date = "today"
location = (44.222, -14.232)

post_dictiomary = {"user_id": 209, "message": "hi", "date": "todya", "langauge:": "english", "location": "new york"}
print(type(post_dictiomary))
print(post_dictiomary)
print(post_dictiomary["message"])

if "strike_price" in post_dictiomary:
    print(post_dictiomary["strike_price"])
else:
    print("Strikeprice is not available")
print()

for key in post_dictiomary.keys():
    value = post_dictiomary[key]

    print(key, "=", value)

# tplesu tuples
# code
# print
# lis vs tuple
# List []
# tuple

import sys

print("dir of sys:", dir(sys))

tulpe_names = ("t1", "t2")
list_names = {"l1", "l2"}
print()
print("the size of T:", sys.getsizeof(tulpe_names))
print("the size of L:", sys.getsizeof(list_names))
import timeit

list_time_test = timeit.timeit(stmt="[1992, 1994, 1998, 1998]", number=1000000)
print("list time: ", list_time_test)
print()
tuple_time_test = timeit.timeit(stmt="(1992, 1994, 1998, 1998)", number=1000000)
print("tuple time: ", list_time_test)
print(type(list_time_test))

"""
# (age, country< knows_py)
survey = (30, "Ye", True)
age = survey[0]
country = survey[1]
knows_py = survey[2]
print("Age:", age)
print("Country:", country)
print("Knows py:", knows_py)
"""

survey_2 = (25, "DE", False)
age, country, knows_py = survey_2
print("Age:", age)
print("Country:", country)
print("Knows py:", knows_py)

import logging

# create and configure logger
LOG_FORMAT = "%(levelname)s %(asctime)s- %(message)s"
logging.basicConfig(filename="/Users/khaled/Documents/Loggertest.log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode="w")
logger = logging.getLogger()
# test the logger
logger.debug("debug")
logger.info("Hi 1st message")
logger.info("ingo")
logger.warning("warning")
logger.error("error")
logger.critical("criticsl")

print("The logger level is: ", logger.level)

import math

logger.info("now running the quadtatic func")
def quadratic_formula(a, b, c):
    """return the solutions tio the equation ax^2 + bx +c = 0"""
    logger.info("quadratic_formula({0}, {1}, {2})".format(a, b, c))

    # compute the discriminant
    logger.debug("# Compute the discriminant")
    disc = b ** 2 - 4 * a * c

    # compute the two roots
    logger.debug("# Compute the two roots")
    root1 = (-b + math.sqrt(disc)) / (2 * a)
    root2 = (-b - math.sqrt(disc)) / (2 * a)

    # return the roots
    logger.debug("# Return the roots")
    return (root1, root2)


roots = quadratic_formula(1, 0, -4)
print(roots)
