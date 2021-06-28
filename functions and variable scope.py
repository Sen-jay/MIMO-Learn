def add_bonus(salary):
    bonus = 100
    print(salary + bonus)

add_bonus(1900)

def add_bonus(salary):
    bonus = 100
    bonus = 200
    print(salary + bonus)

add_bonus(1900)

def add_bonus(salary):
    bonus = 100
    print(salary + bonus)

add_bonus(1900)
print("print(bonus)")

print("error")

print("does a variable have a local scope")
print("when we create it inside of a function's block")


def apply_discount(price):
    discount = 20
    return price - discount


final_price = apply_discount(50)
print(final_price)


def apply_discount(price):
    discount = 20
    discount = 10
    return price - discount


final_price = apply_discount(50)
print(final_price)


def greet_user(name):
    greeting = "Hi"
    print(f"{greeting} {user}!")


user = "Amy"
print(user)
greet_user(user)

shipping = 10


def calculate_total(cart):
    print(cart + shipping)

calculate_total(54)

single_player = True

if single_player:
    player_1 = "Mario"

print(f"Player 1: {player_1}")

character = "Mario"
print(character)

rent = 1000

def calculate_spendings(groceries):
    print(f"Rent {rent + groceries}")

print(f"Rent {rent}")
calculate_spendings(300)

price = 100

for i in range(2):
    discount = 10
    price = price - discount

print(f"Discount: {discount}")

trise_left = 2
print(trise_left)
