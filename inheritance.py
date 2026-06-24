class Human():
    def __init__(self):
        self.energy=100

    def walk(self):
        print("i am now walking")


class Athlete(Human):
    def __init__(self):
        super().__init__()

    def run(self):
        print("i am now running fast")


runner=Athlete()
runner.walk()
runner.run()