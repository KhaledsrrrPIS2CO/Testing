import xml.etree.ElementTree as ET

class User:
    pass


# user 1 is an instance of User class, khaled is also an object
user_1 = User()
user_1.first_name = "khaled"
user_1.last_name = "Alghaish"

# data attachhed tpoo an obkect are filedls
print(user_1.first_name)
print(user_1.last_name)

# dont captilze the field s

first_name = "Shaima"
last_name = "Garman"
print(first_name, last_name)
print(user_1.first_name, user_1.last_name)
user2 = User()
user2.first_name = "Nassim"
user2.last_name = "Taleb"
print(user2.first_name, user2.last_name)
print(type(user_1.first_name))
user_1.age = 30
user_1.favorite_book = "Antifraagility"
print(user_1.first_name, user_1.last_name, user_1.age, user_1.favorite_book)


# a function inside a class is called a method iniit methd,m imnslazation or constructor
# a function insoide a cvlass is called aa method
class User1:
    """a memeber of KSYZ. for now we sttore them by name and by the quality of the day"""

    def __init__(self, full_name, birthday, day_quality):
        self.name = full_name
        self.birthday = birthday
        self.day_quality = day_quality

        # exctract first and last name
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]


user10 = User1("Khaled Alghaish", "19940229", "4")
print(user10.name)
print(user10.birthday)
print()
print(user10.name)
print(user10.birthday)
print(user10.first_name)
print(user10.last_name)
print("the quality of the day:", user10.day_quality)
print(help(User1))


def is_prime_v1(n):
    """the functions returns yes if n is price & no otherweise"""
    for d in range(2, n):
        if n % d == 0:
            return False
        return True

#test function
for n in range(1,21):
    print(n, is_prime_v1(n))

pnl_list = [72, 78, 78]
pnl_list_to_set = set(pnl_list)
print(pnl_list_to_set)


# documentation party
#mind

print("pow",pow(2,3))
print(2**3)

#XML
#extended marlnle langauge
# store data that machines and humans unbdertaansds
#emelment treee api
print(dir(ET))



