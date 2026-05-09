team = {}

for i in range(11):
    name = input("Enter player name: ")
    height = float(input("Enter height (in cm): "))
    team[name] = height

captain = max(team, key=team.get)

print("Captain of the team is:", captain)
print("Height:", team[captain], "cm")
print (team)