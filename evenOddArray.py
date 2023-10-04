n = int(input())
ar = []
for i in range(n):
    a = int(input())
    ar.append(a)
for i in range(n):
    if ar[i]%2==0:
        ar[i]=0
    else:
        ar[i]=1
for i in range(n):
    print(ar[i],end='')
