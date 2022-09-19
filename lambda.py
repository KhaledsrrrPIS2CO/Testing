def f(x):
    return 3 * x + 1


print(f(5))
lambda x: 3 * x + 1
test = lambda x: 3 * x + 1
test(2)
print(test(2))

full_name = lambda fn, ln: fn.strip().title + " " + ln.strip().tiitle()
print(full_name("  khaled", "alghaish"))
