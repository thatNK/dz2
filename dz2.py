import random

class Student:
    amoung_of_students = 0

    def __init__(self, name ="Adolf Hitler", height=160):
        Student.amoung_of_students += 1
        self.height = height
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True
        self.money = 50
        #print("I am alive")

    def to_study(self):
        self.progress += 0.12
        self.gladness -= 0.2

    def to_sleep(self):
        self.gladness += 3

    def to_chill(self):
        self.gladness += 5
        self.progress -= 0.1
        self.money -= 50

    def to_work(self):
        self.money += 100
        self.gladness -= 0.2

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out")
            self.alive = False
        elif self.gladness < 0:
            print("Depression")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally...")
            self.alive = False
        elif self.money <5:
            print("Died from hunger")
            self.alive = False

    def end_of_day(self):
        print(f"progress {round(self.progress)}, gladness {self.gladness}, money{self.money}")

    def live(self):
        life_cube = random.randint(1,3)
        if life_cube == 1:
            self.to_study()
        elif life_cube == 2:
            self.to_chill()
        elif life_cube == 3:
            self.to_sleep()
        self.end_of_day()
        self.is_alive()
        if self.money <= 50:
            self.to_work()

    def __str__(self):
        return f"This is Student with {self.height} cm"

    def __bool__(self):
        return True

    def __len__(self):
        return Student.amoung_of_students

    def printer(self):
        print(self.height)

    def grow(self, height=1):
        self.height = self.height + height


vasia = Student(name="Vasia")

while vasia.alive:
    vasia.live()

print("Game over")