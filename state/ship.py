
COURSE_EAST = 'EAST'
COURSE_WEST = 'WEST'
COURSE_NORTH = 'NORTH'
COURSE_SOUTH = 'SOUTH'


class Ship:

    def __init__(self, name, speed, course):
        self.name = name
        self.speed = speed
        self.course = course

    def increase_speed(self):
        self.speed += 5

    def decrease_speed(self):
        self.speed -= 5

    def change_course(self, new_course):
        self.course = new_course

    def south_course(self):
        self.course = COURSE_SOUTH

    def describe(self):
        print(f"Ship '{self.name}' is going to {self.course} with speed {self.speed} km/h.")

    def go_down(self):
        print(f"Ship '{self.name}' is going down on course {self.course} with speed {self.speed} km/h")


victoria_ship = Ship('Queen Victoria', 20, COURSE_EAST)
victoria_ship.describe()

victoria_ship.increase_speed()
victoria_ship.describe()

print('I see very ig iceberg')
victoria_ship.decrease_speed()
victoria_ship.decrease_speed()
victoria_ship.decrease_speed()
victoria_ship.describe()

victoria_ship.change_course(COURSE_NORTH)
victoria_ship.describe()

print('I see an enemy battleship')
victoria_ship.south_course()
victoria_ship.describe()

victoria_ship.go_down()