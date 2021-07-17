def factorial(num):
    if num == 0:
        return 1

    output = num * factorial(num-1)
    return output


print(factorial(3))
