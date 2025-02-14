

# TODO implement a Toy class that consists of multiple objects such as batteries, lights, loudspeaker, etc.
# TODO your code goes here


class Battery:

    def __init__(self):
        self.capacity_mAh = 1000
        self.charge_percentage = 0

    def charge(self):
        self.charge_percentage = 100
        print("Battery charged!")

class Speaker:

    def __init__(self):
        self.volume = 100

    def play_sound(self):
        print("Speaker is playing an annoying sound")

class Lights:

    def __init__(self):
        self.colour = "blue"

    def shine(self):
        print("Lights are blinking in a weird pattern")


class Toy:
    def __init__(self, battery, speaker, lights):
        self.battery = battery
        self.speaker = speaker
        self.lights = lights

    def play(self):
        self.battery.charge()
        print("Playing with the toy!")
        self.speaker.play_sound()
        self.lights.shine()
        self.battery.capacity_mAh = 0





toy = Toy(Battery(), Speaker(), Lights())
toy.play()