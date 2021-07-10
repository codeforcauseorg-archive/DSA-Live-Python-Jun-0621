n = int(input("Enter num = "))

result = 0

while n > 0:
    last = n % 10
    result = result * 10 + last
    n = n // 10

print(result)