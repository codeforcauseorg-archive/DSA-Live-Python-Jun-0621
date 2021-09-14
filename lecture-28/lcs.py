# def lcs(first, second, flen, slen):
#
#     if (flen == 0) or (slen == 0):
#         return 0
#
#     if first[flen-1] == second[slen-1]:
#         return 1 + lcs(first, second, flen-1, slen-1)
#
#     left = lcs(first, second, flen-1, slen)
#     right = lcs(first, second, flen, slen-1)
#     return max(left, right)


def lcs(first, second, flen, slen, memory):

    if (flen == 0) or (slen == 0):
        return 0

    if (flen, slen) in memory:
        return memory[(flen, slen)]

    if first[flen-1] == second[slen-1]:
        sol = 1 + lcs(first, second, flen-1, slen-1, memory)
    else:
        left = lcs(first, second, flen-1, slen, memory)
        right = lcs(first, second, flen, slen-1, memory)
        sol = max(left, right)

    memory[(flen, slen)] = sol
    return sol


def lcsItr(first, second):

    memory = {}

    for flen in range(len(first) + 1):
        for slen in range(len(second) + 1):

            if (flen == 0) or (slen == 0):
                memory[(flen, slen)] = 0
            else:
                if first[flen - 1] == second[slen - 1]:
                    sol = 1 + memory[(flen - 1, slen - 1)]
                else:
                    left = memory[(flen - 1, slen)]
                    right = memory[(flen, slen - 1)]
                    sol = max(left, right)
                memory[(flen, slen)] = sol

    return memory[(len(first), len(second))]


def lcsItr(first, second):

    memory = [0] * (len(second) + 1)

    for flen in range(1, len(first) + 1):
        temp = [0] * (len(second) + 1)

        for slen in range(len(second) + 1):
            if slen == 0:
                temp[slen] = 0
            else:
                if first[flen - 1] == second[slen - 1]:
                    sol = 1 + memory[slen - 1]
                else:
                    left = memory[slen]
                    right = temp[slen-1]
                    sol = max(left, right)
                temp[slen] = sol

        memory = temp

    return memory[len(second)]


f = "aman"
s = "manan"

print(lcsItr(f, s))