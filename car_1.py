class Car:
    def __init__(self, speed):
        self.speed = speed
        print(f" __init__ speed is {speed} km/h")

    def accelerating(self):
        self.speed +=1
        print(f"speed after accelerating is {self.speed} km/h")

    def current_speed(self):
        print(f"current speed is {self.speed} km/h")

    def breaking(self):
        self.speed -=1
        print(f"speed after breaking is {self.speed} km/h")

car_speed = Car(20)
car_speed.accelerating()

for a in range(39):
    car_speed.accelerating()

car_speed.current_speed()

for b in range(50):
    car_speed.breaking()

car_speed.current_speed()





