def fibo(n):

    if n <= 1:
        return n

    left = fibo(n-1)
    right = fibo(n-2)
    output = left + right
    return output

fibo(4)