# 1. Car information
class Car:
  def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0


car = Car("ABC-123", 142)
print(car.registration_number)
print(car.max_speed)
print(car.current_speed)
print(car.travelled_distance)


# Car speed status

class Car:
    def __init__(self, reg, max_speed):
        self.reg = reg
        self.max_speed = max_speed
        self.speed = 0

    def accelerate(self, change):
        self.speed = self.speed + change

        if self.speed > self.max_speed:
            self.speed = self.max_speed

        if self.speed < 0:
            self.speed = 0

car = Car("ABC-123", 142)
car.accelerate(30)
car.accelerate(70)
car.accelerate(50)

print("=== Car Speed Status ===")
print("Speed now:", car.speed, "km/h")
car.accelerate(-200)
print("Final speed:", car.speed, "km/h")


# 3. Car travel information

class Car:
    def __init__(self, reg, max_speed):
        self.reg = reg
        self.max_speed = max_speed
        self.speed = 0
        self.distance = 0

    def accelerate(self, change):
        self.speed = self.speed + change

        if self.speed > self.max_speed:
            self.speed = self.max_speed
        if self.speed < 0:
            self.speed = 0

    def drive(self, hours):
        self.distance = self.distance + self.speed * hours


car = Car("ABC-123", 142)
car.accelerate(60)
car.drive(1.5)

print("== Car Travel Information ==")
print("Speed:", car.speed, "km/h")
print("Distance:", car.distance, "km")


# 4. Race result

import random

class Car:
    def __init__(self, reg, max_speed):
        self.reg = reg
        self.max_speed = max_speed
        self.speed = 0
        self.distance = 0

    def accelerate(self, change):
        self.speed += change

        if self.speed > self.max_speed:
            self.speed = self.max_speed
        if self.speed < 0:
            self.speed = 0

    def drive(self, hours):
        self.distance += self.speed * hours

cars = []
for i in range(1, 11):
    reg = "ABC-" + str(i)
    max_speed = random.randint(100, 200)
    cars.append(Car(reg, max_speed))

race_on = True

while race_on:
    for car in cars:
        change = random.randint(-10, 15)
        car.accelerate(change)
        car.drive(1)

        if car.distance >= 10000:
            race_on = False

print("== Race Results ==")
print("Reg\tMax\tSpeed\tDistance")

for car in cars:
    print(car.reg, "\t", car.max_speed, "\t", car.speed, "\t", int(car.distance))