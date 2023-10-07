#Non Repeating Character
st = input()
length = len(st)
st = st.lower()
s = ""
flag = 0
for i in range(length):
    if 'a'<=st[i]<='z':
        ch = st[i]
        s = st[0:i]+st[i+1:length]
        if ch not in s:
            print(ch)
            flag = 1
            break
 if flag == 0:
     print("None")
