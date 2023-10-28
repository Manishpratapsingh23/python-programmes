#item exist in a tuple
t = (1,2,3,4,5,6,7,8,9,10,1,3,7,8,5)
n = int(input("enter item to be search: "))
for i in t:
    if i==n:
        print("item exist")
        break
else:
    print("item not exist")
