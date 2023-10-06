#prime sort
n = eval(input())

count = 0
prime_string = ""
non_prime_string = ""
prime = ""
for i in n:
    for j in range(1,int(i)):
        if int(i)%j == 0:
            count = count + 1
    if count == 1:
        prime_string += i
    else:
        non_prime_string += i

    count = 0


# Sorting Section

#Insertion Sort


prime_string = sorted(prime_string)
for i in prime_string:
    prime += i
print(f'"{prime}{non_prime_string}"')

