#converting_a_tuple_into_string
t = (1,2,3,4,5)
s = ""
for i in t:
    s += str(i)
st = "".join(map(str,t))
print(st)
print(f'{s}')
print(str(t))
