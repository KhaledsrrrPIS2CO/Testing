class User:
    pass

#user 1 is an instance of User class, khaled is also an object
user_1 = User()
user_1.first_name =  "khaled"
user_1.last_name = "Alghaish"

#data attachhed tpoo an obkect are filedls
print(user_1.first_name)
print(user_1.last_name)

#dont captilze the field s

first_name ="Shaima"
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
class User:
    def __init__(self, full_name,birthday):
        self.n
