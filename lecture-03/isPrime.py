value = int(input())

n = 2
prime = True

while n*n <= value:
    if value % n == 0:
        prime = False
        break
    n = n+1

if prime:
    print("This is a prime number")
else:
    print("Not a prime")




