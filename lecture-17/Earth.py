# singleton

class Earth:

    __instance = None

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Earth()

        return Earth.__instance


e1 = Earth.get_instance()
e2 = Earth.get_instance()

print(e1 is e2)

