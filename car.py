class Car:
    def __init__(self, name, color, speed, direction):
        self.name = name
        self.color = color
        self.speed = speed
        self.direction = direction

    def status(self):
        msg = f"Car: {self.name} is {self.color} has {self.speed} km/h and direction - {self.direction}"
        print(msg)

    def forward(self):
        self.direction = "FORWARD"

    def reverse(self):
        self.direction = "REVERSE"


car = Car("BMW", "white", 180, "FORWARD")
car.status()
car.reverse()
car.status()
car.forward()
car.status()
