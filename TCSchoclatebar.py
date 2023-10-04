'''
Q1. A chocolate distributor unit has installed two new automatic arms for the unloading
the chocolate bars from containers. Arm A has the capacity to unload one chocolate bar
whilst the other arm B unload two bars at a time. In order for any two containers to be
unloaded fully and simultaneously by both arms, the distributors has to choose the correct
chocolate bars quantity (quantity “X” for container unloaded by arm A and quantity “Y”
container unloaded by arm B) in those containers from supplier.
The task to develop a code to identify a pair of container quantities (maximum quantity
5000) such that both arms unload all chocolate bars from those containers fully and
complete their unloading simultaneously so the following containers can be placed for
unloading automatically .
The correct pair identified can be marked as ‘Yes’
And for incorrect pairs as ‘No’.
Example 1:
Input:
100---Value of X
200--- Value of Y
Output:
Yes—Print Yes indicating 100 and 200 chocolate bars can be fully emptied simultaneously
'''
x = int(input("enter choclate bars:"))
y = int(input("enter choclate bars:"))
if y == 2*x:
    print("yes")
else:
    print("no")
