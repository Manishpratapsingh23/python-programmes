#anagram string
x = eval(input())
y = eval(input())
count = 0
for i in range(len(x)):
    for j in range(len(y)):
        if sorted(x[i])==sorted(y[j]):
            count +=1
print(count)
