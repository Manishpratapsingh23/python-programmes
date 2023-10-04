st = input()
c = 0
s1 = ''
s2 = ''
x = st.split()
print(x)
for i in st:
    n = int(i)
    for j in range(1,n,1):
        if n%j==0:
            c +=1
    if c==1:
        s1 += i
    else:
        s2 += i
    c = 0
t = 0
for i in range(len(s1)-1):
    a = int(s1[i])
    b = int(s2[i+1])
    if a>b:
        t = a
        a = b
        b = a
    s1[i] = str(a)
    s1[i+1] = str(b)
    
print(s1+s2)
'''

st = input()
c = 0
s1 = ''
s2 = ''
for i in st:
    n = int(i)
    for j in range(1,n,1):
        if n%j==0:
            c +=1
    if c==1:
        s1 += i
    else:
        s2 += i
    c = 0
lst1 = list(s1)
lst2 = list(s2)
lst1.sort()
lst = lst1 + lst2
for i in lst:
    print(i,end="")

'''
