class Car:

    def __init__(self):
        self.engine = "normal"
        self.wheels = 4

    def start(self):
        print("Starting like {} car".format(self.engine))

    def stop(self):
        print("Stopping like {} car".format(self.engine))


class Tesla(Car):

    def fly(self):
        print("Fly like tesla")


# mycar = Car()
# mycar.start()
# mycar.stop()

mytesla = Tesla()
mytesla.start()
mytesla.stop()
print(mytesla.engine)
print(mytesla.wheels)
