class Human:

    population = []

    def __init__(self, name):
        self.alive = True
        self.name = name

        Human.population.append(self)

    def __repr__(self):
        return "{} - {}".format(self.name, self.alive)


class Hitman(Human):

    def __init__(self, name):
        super().__init__(name)
        self.kills = 0

    def __repr__(self):
        return "{} - {} - {}".format(self.name, self.alive, self.kills)

    def kill(self, target):
        if self.alive and target.alive:

            if self is not target:
                self.kills += 1
            target.alive = False


sanjiv = Human("Sanjiv")

ravi = Human("Ravi")
gogo = Hitman("Crime Master")

print(Human.population)


gogo.kill(sanjiv)
gogo.kill(sanjiv)
gogo.kill(sanjiv)
gogo.kill(sanjiv)
gogo.kill(gogo)

print(Human.population)