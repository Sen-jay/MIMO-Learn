def is_multiplayer(players):
    print(len(players) == 2)

players = ["Amy", "Jay"]
is_multiplayer(players)

def display_programme(movies):
    print(f"Alring tonight: {movies}")

movie_list = ["Alien", "Moon"]
display_programme(movie_list)

def display_programme(movies):
    print("Airing tonight:")
    print(movies)

movie_list = ["Alien", "Moon"]
display_programme(movie_list)

def display_programme(movies):
    print("Airing tonight")
    print(movies)

movie_list = ["Alien", "Moon"]
display_programme(movie_list)

def count_passengers(passengers):
    print(len(passengers))

passengers = ["June" , "Sam" , "Lee"]
count_passengers(passengers)

def is_booked(passengers):
    print(len(passengers) > 4)

passengers = ["June", "Sam" , "Lee"]
is_booked(passengers)

def get_winner(top_players):
    winner = top_players[0]
    print(f"Game winner: {winner}")

top_players = ["Jay, Meg ,Cy"]
get_winner(top_players)

def update_first_place(leadefboard,player):
    leadefboard[0] = player
    return leadefboard

leaderboard = ["Jay", "Meg" , "Cy"]
leaderboard = update_first_place(leaderboard,"Lena")
print(leaderboard)

def get_middle_name(names):
    return names[1]


name_list = ["Thomas" , "Stearns" , "Elliot"]
get_middle_name(name_list)

def set_intials(names, initial):
    names[0] = initial
    print(names)

author_names = ["Francis", "Scott", "Fitzgerald"]
set_intials(author_names, "F.")

def update_first_place(leadefboard,player):
    leadefboard[0] = player
    return leadefboard

leaderboard = ["Jay", "Meg" ,"Cy"]
leaderboard = update_first_place(leaderboard,"Lena")
print(leaderboard)

def display_specials(specials):
    print(f"Today's specials:{specials}")

specials_list = ["Pizza" , "risotto"]
display_specials(specials_list)

def display_specials(specials):
    print("Today's specials:")
    print(specials)

specials_list = ["pizza","rissoto"]
display_programme(specials_list)

def count_items(basket):
    print(len(basket))

basket_items = ["t-shirt", "jeans", "sweater"]
count_items(basket_items)

def has_two_for_one(basket):
    print(len(basket) >= 2)

basket_items = ["t-shirt", "jeans" , "jeans"]
has_two_for_one(basket_items)

def get_newest_values(values):
    print(values[0])

humidity_percent = [50,43,49]
get_newest_values(humidity_percent)

def set_initials(names, initial):
    names[0] = initial
    print(names)

author_names = ["Francis","Scott","Fitzgerald"]
set_initials(author_names, "F.")

def set_initials(names, initial):
    names[0] = initial
    return(names)

author_names = ["Francis", "Scott", "Fitzgenard"]
author_names =set_initials(author_names,"F.")
print(author_names)
