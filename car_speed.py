class Car:
    def __init__(self, speed):
        self.speed = speed
        print('__init__', speed)

    def acceleration(self):
        self.speed += 1

        print(f"acceleration: speed = {self.speed} km/h")

    def braking(self):
        self.speed -= 1
        print(f"braking: speed = {self.speed}")

    def current_speed(self):
        print(f"my current speed: speed = {self.speed} km/h")

normal_car = Car(20)
normal_car.current_speed()

for i in range(40):
    normal_car.acceleration()

normal_car.current_speed()
for b in range(50):
    normal_car.braking()

normal_car.current_speed()
