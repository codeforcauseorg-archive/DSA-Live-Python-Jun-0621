def sumtill(n):

    if n == 0:
        return 0

    output = n + sumtill(n-1)
    return output