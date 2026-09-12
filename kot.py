import random


class Cat:

    def __init__(self, name):
        self.name = name
        self.satiety = 50
        self.energy = 50

    def eat(self):
        print(f"{self.name} їсть.")
        self.satiety += 20

    def sleep(self):
        print(f"{self.name} спить.")
        self.energy += 20
        self.satiety -= 10

    def play(self):
        print(f"{self.name} грається.")
        self.energy -= 10
        self.satiety -= 10

    def live_day(self, day):
        print(f"\nДень {day}:")
        action = random.randint(1, 3)
        if action == 1:
            self.eat()
        elif action == 2:
            self.sleep()
        else:
            self.play()
        print(f"Ситість: {self.satiety}, Енергія: {self.energy}")


cat = Cat("Мурчик")

for day in range(1, 8):
    cat.live_day(day)