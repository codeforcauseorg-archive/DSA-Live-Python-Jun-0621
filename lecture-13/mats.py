n = int(input())

print()

while n > 0:
    score = int(input().strip())

    if score < 38:
        print(score)
    elif (score % 5) >= 3:
        print(score + (5 - (score % 5)))
    else:
        print(score)

    n -= 1

