#badminton tournament series
line = input()
x = line.split(',')
reg = ""
count = 0
st = []
    
for i in x:
    c = 0
    if i not in reg:
        for j in x:
            if i==j:
                c += 1
    if c>=count:
        if c==count:
            st.append(i)
        elif c>count:
            del(st)
            st = []
            st.append(i)
            count = c
    reg += i
    c = 0
print(st)
st.sort()
print(st)
print(st[0])
    
    
