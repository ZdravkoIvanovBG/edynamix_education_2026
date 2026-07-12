from edynamix_education_2026.oop.project_animal_dog.animal import Animal


class Dog(Animal):
    @staticmethod
    def bark():
        print("barking...")

dog = Dog()
dog.bark()
dog.eat()