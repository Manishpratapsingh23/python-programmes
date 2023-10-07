#Color Combination
ar = eval(input())
while len(ar)>1:
    length = len(ar)
    if length%2!=0:
            s = ar[-1]
            ar = ar[0:len(ar)-1]
    l = len(ar)
    print(ar)
    for i in range(0,l,2):
        
        if ar[i]=='R' and ar[i+1]=='G' or ar[i]=='G' and ar[i+1]=='R':
            ar.append('B')
        elif ar[i]=='R' and ar[i+1]=='B' or ar[i]=='B' and ar[i+1]=='R':
            ar.append('G')
        elif ar[i]=='B' and ar[i+1]=='G' or ar[i]=='G' and ar[i+1]=='B':
            ar.append('R')


    ar = ar[l:]
    if length%2!=0:
        ar.append(s) 
    s = ''
print(ar)
        
'''
ar = ar[l:]
'''
