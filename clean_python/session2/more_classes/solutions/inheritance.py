from scipy.constants import c


class Vehicle:
    def __init__(self):
        self.max_speed = c

    def move(self):
        pass

# TODO create 2-3 subclasses of Vehicle.
# TODO think of which properties you would need to add
# TODO overwrite move()
# TODO do you need other methods?

class Car(Vehicle):

    def __init__(self):
        super().__init__()
        self.max_speed_ms = 50
        self.fuel_amount_liters = 60

    def unlock(self):
        print("Car unlocked")

    def start_engine(self):
        print("Engine started")

    def put_in_gear(self, gear: int):
        print(f"Car in gear {gear}")

    def move(self):
        self.unlock()
        self.start_engine()
        self.put_in_gear(1)
        print("Car moving")

class Bicycle(Vehicle):

    def __init__(self):
        super().__init__()
        self.max_speed_ms = 8

    def unlock(self):
        print("Bicycle unlocked")

    def get_on(self):
        print("You're on the bicycle")

    def move(self):
        self.unlock()
        self.get_on()
        print("Bicycle moving")


car = Car()
bicycle = Bicycle()

vehicles = [car, bicycle]

for elem in vehicles:
    elem.move()
    print("----")




