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
