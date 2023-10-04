#strange number
n = int(input("enter number: "))

flag = 0
c = 0
ar = []
for i in range(2,n):
    if n%i==0:
       ar.append(i)
print(ar)
for i in range(len(ar)):
    for j in range(1,ar[i]):
        if ar[i]%j==0:
            c += 1
    if c!=1:
        flag = 1
        break
    c = 0

if flag==0:
    ar.sort()
    maxi = ar[-1]
    root = n**0.5
    if maxi>root:
        print("strange number  ", n)
    else:
        print("not a strange number",n)
else:
    print("not a strange number",n)
