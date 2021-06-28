actor_bio = {
    "name": "Bill Murray",
    "known for": ["Lost in Translation","Rushmore"]
}

print(actor_bio["name"])

player_score = {
    "ann": 13,
    "michael": 20,
    "ava": 34
}
for player in player_score:
    print(player_score[player])

ticket = {
    "seat no.": 25,
    "first class": False
}
ticket["first class"] = True
print(ticket)

print(" do we access a value associated with a certain key in a dictionary")
print("By the name of its key")

print("Where do we code the key name when accessing a value?")
print("After the dictionary's name, between square brackets[]")

print("How can we reuse the value associated with a key after accessing it ?")
print("By storing it in a variable")

print("HOW can we loop through all keys in the dictionary?")
print("With a for loop")

winner_scores = {
    "first": ("Ted", 50),
    "second": ("Jess", 47)
}

for winner in winner_scores:
    print(winner_scores[winner])

print("It's displaying the tuple value associated with the key stored in the winner variable")

print("Accessing the current value associated with the key")

participants = {
    "Meg": True,
    "KIm": False,
}

participants["KIm"] = True

print(" It updates the value associated with the key Kim to True")

air = {
    "nitrogen": "78%",
    "oxygen": "21%",
    "argon": "0.93%",
    "carbon dioxide": "0.04%",
    "other": "0.03%"
}

print(air["argon"])
print(air["oxygen"])

participants = {
    "Meg": True,
    "Kim": False,
    "Luis":True,
    "Luis M.": False
}

meg = participants["Meg"]
print(meg)

contents = {
    "ch. 1": "A long-expected party",
    "ch. 2": "The shadow of the past",
    "ch. 3": "Three is company"
}

contents["ch. 4"] = "A Short Cut to Mushrooms"

print(contents)

for chapter in contents:
    print(contents[chapter])

toppings = {
    "olives": True,
    "anchovies": False,
    "extra chess": False
}

toppings["extra chess"] = True
print(toppings)

toppings["olives"] = False
print(toppings)

ticket = {
    "seat no.": 25
}

ticket["window"] = True
print(ticket)

winner_scores = {
    "first": ("Ted", 50),
    "second": ("Jess", 47)
}

winner_scores["third"] = ("Jo", 30)

print(winner_scores)

