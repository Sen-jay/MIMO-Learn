def display(first_name):
    print(first_name)
    
display("Alex")

def display(first, last):
    print(first + " " + last)
    
display("Alex", "Morgan")

def display(first, last):
    print(first + " " + last)

display("Alex", "Morgan")

def show_winners(first, second, third):
    print("First place: " + first)     
    print("second place: " + second)
    print("Third place: " + third)
    
show_winners("kim", "lee", "ava")

def mix(first, second,third):
    return first + second + third

result = mix("big", "bad","wolf")
print(result)

def create_email(name, year):
    return name + year + "@hutmail.com"

email = create_email("jo", "1998")
print(email)

def add_prefix(prefix , word):
    return prefix + word

new_word = add_prefix("re", "do")
print(new_word)

def show_queue(current, up_next):
    print("now playing: " + current)
    print("up next: " + up_next)

show_queue("Hey Joe", "Purple Haze")

def mix(first, second, third):
    print(first + second + third)

mix("peter", "Piper","Picked")
