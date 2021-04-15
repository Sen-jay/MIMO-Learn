# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def age_label(age):
    label = "User age: " + age
    return label

result = age_label("29")
print(result)

print("how do we store the return in value in a variable?")

print("we call the function and store it in a variable")

def giveMeTen():
    return 10

print(giveMeTen())

def add_greeting(user):
    greeting = "Greeting " + user
    return greeting

result = add_greeting("Saoirse")
print(result)

def half_twice(number):
    half = number / 2
    half_again = half / 2
    return half_again

result = half_twice(12)
print(result)

def add_ten(number):
    sum = 10 + number
    return sum

print(add_ten(20))

def sign_up(user):
    status = user + "signed up"
    return status

result = sign_up("Desmond")
print(result)

def update(user):
    update = "No Emails: " + user

result = update("Ann")
print(result)