#Find the Frequency of the Word ‘the’ in a given Sentence
st = input("enter string: ")
st = st+' '
length = len(st)
s = ''
count = 0
for i in range(length):
    if st[i]!=' ':
        s += st[i]
    else:
        if s == "the":
            count += 1
        s = ''
print("frequency of THE in string is ",count)
