class Human:

    population = 0

    def __init__(self, name):
        self.name = name
        self.hands = 2
        Human.population += 1

    def __repr__(self):
        return "Name: {}, Hands: {}".format(self.name, self.hands)


# anuj = Human()
# print(anuj.hands)
print(Human.population)

popu = []

anuj = Human("Anuj")
# print(anu)
popu.append(anuj)

ravi = Human("Ravi")
popu.append(ravi)

print(popu)
