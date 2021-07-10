line = "this fox is very happy"

freq = {}

for ch in line:
    if ch not in freq:
        freq[ch] = 1
    else:
        freq[ch] += 1

# print(freq)

print(list(freq.items()))

