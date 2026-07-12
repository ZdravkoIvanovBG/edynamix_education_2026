from edynamix_education_2026.oop.project_food_fruit.food import Food


class Fruit(Food):
    def __init__(self, name, expiration_date):
        super().__init__(expiration_date)
        self.name = name

fruit = Fruit("Apple", "2023-05-10")
print(fruit.expiration_date)