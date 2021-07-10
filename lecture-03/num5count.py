n = int(input("Enter num = "))
count = 0

while n > 0:
    last = n % 10
    if last == 5:
        count = count + 1
    n = n // 10

print(count)

