line = "say hello."

# iterable indexable immutable

# print(type(line[0]))

# print(chr(ord("a") + 1))

# print(line.upper())

result = []

a_ord, z_ord, A_ord = ord('a'), ord('z'), ord("A")

for ch in line:
    ch_ord = ord(ch)
    if (ch_ord >= a_ord) and (ch_ord <= z_ord):
        item_index = ch_ord - a_ord
        res = chr(A_ord + item_index)
        result.append(res)
    else:
        result.append(ch)

print("".join(result))
