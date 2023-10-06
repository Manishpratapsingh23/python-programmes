x = eval(input())
result = []
l = len(x)
for i in range(l):
    print(type(x[i]))
    st = x[i]    
    flag = True
    for j in range(len(st)):
        if st[j]==' ':
            if st[j+1].isupper():
                flag = True
            else:
                flag = False
                break
        elif j==0:
            if st[j].isupper():
                flag = True
            else:
                flag = False
                break
    result.append(flag)
    st = ""
    flag = ""

print(result)
