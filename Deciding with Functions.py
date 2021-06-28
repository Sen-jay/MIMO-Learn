def add_shipping(cart):
    if cart < 100:
        print(f"Total: {cart + 10}")
    else:
        print(f"Total: {cart}")

add_shipping(45)
add_shipping(200)

def add_shipping(cart):
    if cart < 100:
        pqewqrewqerwewrrqerwqwrwerewrreqerwrqeewrqwerqwerwqrwerweqqqqqqqqqwqqweewrrwerwqrwqwerqwerqwerqwerrint(f"Total: {cart + 10}")
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

def calculate(operator, x, y):
    if operator == "+":
        print(x + y)
    else:
        print(f"unknown: {operator}")

calculate("-", 30, 10)

def calculate(operator, x, y):
    if operator == "+":
        print(x + y)
    elif operator == "-":
        print(x - y)
    else:
        print(f"unknown: {operator}")

calculate("-", 30, 10)

def show_progress(points):
    if points > 1000:
        print("New highest score")
    print("Ready for the next level?")

show_progress(900)

def show_status(inbox):
    if inbox > 1000:
        print("Inbox full!")
    print("You have new messages!")

show_status(900)

def show_status(inbox):
    if inbox > 1000:
        print("Inbox full!")
    print("You have new messeges!")

show_status(1200)

def show_notifications(score):
    if score < 30:
        print("Score too low")
    else:
        print("Onto the next level!")

show_notifications(40)

def show_score(score):
    if score < 30:
        print("Score too low")
    elif score == 100:
        print("Top score1")
    else:
        print("Onto the next level!")

show_score(100)
