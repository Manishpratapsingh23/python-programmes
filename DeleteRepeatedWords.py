#. Delete All Repeated Words in String
st = input("enter string: ")
reg = ''
final_st = ''
for i in st:
    if i not in reg:
        final_st += i
        reg += i
print("final string is ",final_st)
