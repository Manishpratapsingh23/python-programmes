#Print all the duplicates in the input string.
st = input("enter string: ")
reg = ''
final_st = ''
for i in st:
    if i not in reg:
        final_st += i
        reg += i
print("final string is ",final_st)
