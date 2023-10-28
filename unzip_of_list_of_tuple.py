#unzip  of list of tuple
lt = [(1,2),(3,4),(5,6),(7,8)]
l1 = []
l2 = []
for i in lt:
    l1.append(i[0])
    l2.append(i[1])
print(l1)
print(l2)
