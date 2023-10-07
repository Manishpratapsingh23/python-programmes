#ship teams
team = eval(input())
name = list(team.keys())
age = list(team.values())
team1 = []
team2 = []
for i in range(len(age)):
    if age[i]>40 or age[i]<20:
        team1.append(name[i])
    elif age[i]>=20 and age[i]<=40:
        team2.append(name[i])
team1.sort()
team2.sort()
print('[\n',' ',team1,',\n',' ',team2,
      '\n]',sep='')
