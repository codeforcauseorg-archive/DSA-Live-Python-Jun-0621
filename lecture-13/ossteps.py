import os
# print(os.path.exists("happy.txt"))

# li = ["apple", "mango", "banana", "pie"]
#
# os.makedirs("/".join(li))

# path = os.path.abspath("../../happy.txt")
#
# print(path)

# f = open(path)
#
# print(f.read())
#
# f.close()

# os.open("./salary_nego_raw.mp4")

sent = "1-45-98"

out = list(map(int, sent.split("-")))

print(out)

