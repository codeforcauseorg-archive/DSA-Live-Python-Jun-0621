import math


def isPowerOfTwo(n: int) -> bool:

    out = math.log2(n)

    rem = out - int(out)

    return rem == 0


print(isPowerOfTwo(1024))
