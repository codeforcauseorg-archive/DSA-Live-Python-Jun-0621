class Engine:

    def __init__(self):
        self.type = "generic"

    def start(self):
        print("start like {} engine".format(self.type))

    def stop(self):
        print("stop like {} engine".format(self.type))


class NitroEngine(Engine):

    def __init__(self):
        super().__init__()
        self.type = "nitro"


class Car:

    def __init__(self):
        self.__engine = Engine()
        self.__state = "stopped"

    def start(self):
        self.__engine.start()
        self.__state = "started"

    def stop(self):
        self.__engine.stop()
        self.__state = "stopped"

    def upgrade(self, engine):
        if self.__state == "stopped":
            self.__engine = engine


mycar = Car()
mycar.start()
mycar.stop()


mynitro = NitroEngine()

mycar.upgrade(mynitro)


mycar.start()
mycar.stop()
