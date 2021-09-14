def fibo(num):
    if num < 2:
        return num

    return fibo(num-1) + fibo(num-2)


def fiboDP(num, memory):
    if num < 2:
        return num

    if num in memory:
        return memory[num]

    memory[num] = fiboDP(num-1, memory) + fiboDP(num-2, memory)
    return memory[num]


def fiboDPIter(number):

    memory = [0] * (number+1)

    for num in range(number+1):
        if num < 2:
            memory[num] = num
        else:
            memory[num] = memory[num-1] + memory[num-2]

    return memory[number]


def fiboDPShort(number):

    if number < 2:
        return number

    memory = [0] * 2

    for num in range(number+1):
        if num < 2:
            memory[num] = num
        else:
            temp = memory[0] + memory[1]
            memory[0] = memory[1]
            memory[1] = temp

    return memory[1]


print(fiboDPShort(900000))