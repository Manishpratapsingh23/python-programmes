#PYTHON CALCULATOR GAME
def add(x,y):
    print(x+y)
def sub(x,y):
    print(x-y)
def multi(x,y):
    print(x*y)
def div(x,y):
    print(x/y)
print("WELCOME TO CALCULATOR GAME: ")
print("PRESS 0 TO EXIT \nPRESS 1 TO CONTINUE")
n = int(input("ENTER YOUR CHOICE: "))
while n!='0':
    print("ENTER NUMBER AND OPERATION YOU WANT TO PERFORM:")
    x = eval(input("ENTER FIRST NUMBER: "))
    y = eval(input("ENTER SECOND NUMBER: "))
    op = input("ENTER OPERATION: ")
    n = op
    
    if op == '+':
        add(x,y)
    elif op == '-':
        sub(x,y)
    elif op == '*':
        multi(x,y)
    elif op == '/':
        div(x,y)
else:
    print("<<<<<YOU LEFT THE GAME>>>>>")
