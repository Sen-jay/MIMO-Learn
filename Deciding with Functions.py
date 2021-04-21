def add_shipping(cart):
    if cart < 100:
        print(f"Total: {cart + 10}")
    else:
        print(f"Total: {cart}")

add_shipping(45)
add_shipping(200)

def add_shipping(cart):
    if cart < 100:
        print(f"Total: {cart + 10}")
    else:
        print(f"Total: {cart}")

add_shipping(45)
add_shipping(200)

def add_shipping(cart):
    if cart < 100:
        print(f"Total: {cart + 10}")

add_shipping(80)

print("what does nesting a conditional inside a function mean?")

print("indenting the conditional so that it's part of the fucntion code block")

def can_drive(age):
    if age >= 18:
        print("Yes they can!")

can_drive(19)

def has_low_battery(level):
    if level <= 20:
        print("Low battery!")

has_low_battery(15)

def has_low_battery(level):
    if level == 100:
        print("Full battery!")

has_low_battery(100)

def get_watting_list(signups):
    if signups > 200:
        print(f"Wating list: {signups - 200}")

get_watting_list(100)

