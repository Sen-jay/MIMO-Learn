def get_scores_data(scores_list):
    highest_score = max(scores_list)
    lowest_score = min(scores_list)
    return highest_score, lowest_score

scores = [31, 17, 80]
data = get_scores_data(scores)
print(data)

highest = data[0]
smallest = data[1]
print(f"smallest score: {smallest}")
print(f"highest score: {highest}")

def get_top_three(players):
    return players[0], players[1], players[2]

players = ["Sue", "Ed", "Ann" "Ty"]
top_three = get_top_three(players)
print(f"First: {top_three[0]}")
print(f"Second: {top_three[1]}")
print(f"Third: {top_three[2]}")

def form_team(players):
    team = []
    team.append(players[0])
    team.append(players[2])
    return team

players = ["Sue","Ed","Ann", "Ty"]
team = form_team(players)
team[0] = "Chole"
print(team)

def check_age(age):
    can_drive = age >= 18
    return age, can_drive
driving_age = check_age(17)
print(driving_age)

def analyze_profit(gains, expenses):
    profit = gains - expenses
    after_taxes = 0.85 * profit
    above_mean = profit > 1000
    return profit, after_taxes,above_mean

insights = analyze_profit(3000, 1200)
print(f"profit: {insights[0]}")
print(f"above mean: {insights[2]}")

