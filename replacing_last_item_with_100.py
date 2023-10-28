#unzip list of tuple----replacing 100 at last element
lt = [(1,2,3),(3,4,5),(5,6,7),(7,8,9)]
nl = []
for i in lt:
    i = list(i)

    i.pop(-1)
    i.append(100)
    i = tuple(i)
    nl.append(i)
print(nl)
