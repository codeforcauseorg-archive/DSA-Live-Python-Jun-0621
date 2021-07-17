def power(x, y):
    if y == 0:
        return 1

    output = x * power(x, y-1)
    return output


def power_better(x, y):
    if y == 0:
        return 1

    output = power_better(x, y//2)
    output = output * output
    if y % 2 == 1:
        output = output * x
    return output


power_better(1, 76599777777888877)
