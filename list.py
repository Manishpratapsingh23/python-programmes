team = {}
team1 = {}
team2 = {}
n = int(input())
for i in range(n):
    name = input()
    age = int(input())
    team[name] = age
print(team)
for i in team.values():
    if i>=20 and i<=40:
        team2 = team
    else:
        team1 = team
print(team1)
print(team2)
