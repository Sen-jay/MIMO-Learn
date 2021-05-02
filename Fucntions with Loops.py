def onboard_passengers(bookings):
    counter = 1
    while counter <= bookings:
        print(f"Passenger {counter} on board")
        counter += 1

onboard_passengers(4)

def display_progress(total_files):
    for i in range(total_files):
        print(f"Downloading file {i} out of {total_files}")

display_progress(3)

def do_countdown(counter):
    while counter > 0:
        print(counter)
        counter -= 1
    print("GO")

do_countdown(3)

def display_stars(rows):
    counter = 0
    while counter < rows:
        print("***")
        counter += 1

display_stars(2)

def show_progress(total):
    for i in range(total):
        print(f"Installing next update")

show_progress(3)

def display_progress():
    for i in range(3):
        print(f"Downloading file {i} out of 3")

display_progress()

def display_progress(total_files):
    for i in range(total_files):
        print(f"Downloading file {i} our of {total_files}")

display_progress(3)

def display_progress(total_files):
    for i in range(total_files):
        print(f"Downloading file {i} out of {total_files}")

display_progress(4)

def show_progress(total):
    for i in range(total):
        print(f'Installing next update')

def repeat_message():
    for i in range(4):
        print("Polly wants a cracker")

repeat_message()

def show_notifications(messages):
    for i in  range(messages):
        print("Failed to send message")

show_notifications(3)

def show_notifications(messages):
    for i in range(messages):
        print("Failed to send message")

show_notifications(2)

def halve_prices(cart):
    for price in cart:
        print(f"New price: {price/2}")

cart_list = [5,20,8]
halve_prices(cart_list)

def halve_prices(cart):
    for price in cart:
        print((f"New price: {price/2}"))

cart_list = [5, 20 ,8]
halve_prices(cart_list)

def halve_prices(cart):
    for price in cart:
        print(f"New price: {price/2}")

cart_list = [5,20,8]
halve_prices(cart_list)

print("how can we reuse a loop that iterates through a lish?")
print("By nesting it inside a function's code block")

def display_players(team):
    number = 1
    for name in team:
        print(f"Player {number}:{name}")

team_1 = ["Kim", "Lee"]
team_2 = ["Meg", "Jo"]
display_players(team_1)

def show_next_track():
    playlist = ["Hey Jude", "Helter Skelter", "Something"]
    for track in playlist:
        print(f"Next up: {track}")

show_next_track()

def show_next_track():
    playlist = ["Hey Jude", "Helter Skelter", "Something"]
    for track in playlist:
        print(f"Next up: {track}")

beatles = ["Hey Jude", "Helter Skelter", "Something"]
beethoven = ["Symphony No. 1 ", "Symphony No. 9"]

show_next_track(beethoven)
show_next_track(beatles)


