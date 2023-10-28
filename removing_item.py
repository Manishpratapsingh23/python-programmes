#removing an item from a tuple
t = (1,2,3,4,5,6,7,8,9,10,1,3,7,8,5)
lst = list(t)
n = int(input("enter item you want to remove: "))
lst.remove(n)
print(lst)
