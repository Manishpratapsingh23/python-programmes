n = int(input())
ar1 = []
ar2 = []
for i in range(n):
    a1 = input()
    a2 = input()
    ar1.append(a1)
    ar2.append(a2)
count = 0
for i in range(n):
    for j in range(n):
        if sorted(ar1[i])==sorted(ar2[j]):
            count +=1
print(count)
