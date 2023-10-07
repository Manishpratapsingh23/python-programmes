#The War
st = input()
ind = st.index('x')
print(ind)
m = int(st[0:ind])
n = int(st[ind+1:])
count = 0
for i in range(0,m):
    for j in range(0,n):
        if (i+j)%2!=0:
            count += 1
print(count)

