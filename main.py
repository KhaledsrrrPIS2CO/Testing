help(hex)
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


