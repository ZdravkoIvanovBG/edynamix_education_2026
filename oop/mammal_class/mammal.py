class Mammal:
    def __init__(self, name, type, sound):
        self.name = name
        self.type = type
        self.sound = sound
        self.__kingdom = "animals"

    def make_sound(self):
        print(f"{self.name} makes {self.sound}")

    def get_kingdom(self):
        print(self.__kingdom)

    def info(self):
        print(f"{self.name} is of type {self.type}")

mammal = Mammal("Dog", "Domestic", "Bark")
mammal.make_sound()
mammal.get_kingdom()
mammal.info()