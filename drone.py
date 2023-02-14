EAST_DIRECTION = "EAST"
WEST_DIRECTION = "WEST"
NORTH_DIRECTION = "NORTH"
SOUTH_DIRECTION = "SOUTH"


class Drone:
    def __init__(self, speed, name, start_location, direction):
        self.speed = speed
        self.name = name
        self.start_location = start_location
        self.direction = direction

    def status(self):
        msg = f"Drone {self.name}  with a speed {self.speed}km/h is flying to" \
              f" {self.direction} from {self.start_location}"
        print(msg)

    def gas(self):
        self.speed +=20

    def broke(self):
        self.speed -=10

    def change_direction(self, new_direction):
        self.direction = new_direction

    def go_to_start(self):
        self.direction = self.start_location

    def south(self):
        self.direction = SOUTH_DIRECTION

    def north(self):
        self.direction = NORTH_DIRECTION

    def west(self):
        self.direction = WEST_DIRECTION

    def east(self):
        self.direction = EAST_DIRECTION

drone = Drone(200, "FlyMoon", "Kyiv",  WEST_DIRECTION)
drone.status()

drone.gas()
drone.status()

drone.broke()
drone.status()

drone.change_direction(NORTH_DIRECTION)
drone.status()

drone.go_to_start()
drone.status()

drone.south()
drone.status()

drone.north()
drone.status()

drone.west()
drone.status()

drone.east()
drone.status()