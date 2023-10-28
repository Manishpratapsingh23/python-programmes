#repeated item in a tuple
t = (1,2,3,4,5,6,7,8,9,10,1,3,7,8,5)
reg=""
for i in t:
    count = 0
    for j in t:
        if i==j and str(i)not in reg:
            count += 1
    if count>1:
      print(i)
    reg += str(i)
print(reg)

