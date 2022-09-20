def f(x):
    return 3 * x + 1


print(f(5))
lambda x: 3 * x + 1
test = lambda x: 3 * x + 1
test(2)
print(test(2))
"""
full_name = lambda fn, ln: fn.strip().title + " " + ln.strip().title()
print(full_name("  khaled", "alghaish"))
"""


def build_quadraatuc_fun(a, b, c):
    """reurns the function f(x) =ax^2 + bx +c"""
    return lambda x: a*x**2 + b*x + c
f = build_quadraatuc_fun(2,3,-5)
print(f(1))

