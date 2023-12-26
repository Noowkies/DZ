#Zadanie 1
class Auto:
    def __init__(self, brand, age, color, mark, weight):
        self.brand = brand
        self.age = age
        self.weight = weight
        self.mark = mark
        self.color = color

    def move(self):
        print('Move')

    def weightgain(self):
        self.weight += 1

    def stop(self):
        print('Stop')

#Zadanie 2

import time

class Truck(Auto):
    def __init__(self, brand, age, color, mark, weight, max_load):
        Auto.__init__(self, brand, age, color, mark, weight)
        self.max_load = max_load

    def move(self):
        print('Warning')
        super().move()

    def load(self):
        time.sleep(1)
        print('Load')
        time.sleep(1)

    def __str__(self):
        return f'{self.color} {self.brand} {self.mark}: {self.age} years'\
            f' old.\n Weight: {self.weight}\n Max Load: {self.max_load}'

class Car(Auto):
    def __init__(self, brand, age, color, mark, weight, max_speed):
        Auto.__init__(self, brand, age, color, mark, weight)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f'Max Speed: {self.max_speed} km/h')

    def __str__(self):
        return f'{self.color} {self.brand} {self.mark}: {self.age} years'\
            f' old.\n Weight: {self.weight}'

BMW = Car('BMW', 9, 'Olivia', 'M3', 1500, 240)
print(BMW)
BMW.move()

Opel = Car('Opel', 20, 'Red', 'Astra', 1200, 160)
print(Opel)
Opel.move()

Volvo = Truck('Volvo', 25, 'Green', 'FL7', 4000, 6000)
print(Volvo)
Volvo.load()
Volvo.move()

Scania = Truck('Scania', 13, 'Blue', 'S500', 3000, 9000)
print(Scania)
Scania.load()
Scania.move()
