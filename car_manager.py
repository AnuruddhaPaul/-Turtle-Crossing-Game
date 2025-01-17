from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car = []
        self.car_speed=STARTING_MOVE_DISTANCE

    def car_creation(self):
        if random.randint(1, 6) == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            ran = random.randint(-250, 250)
            new_car.goto(400, ran)
            self.car.append(new_car)

    def movement(self):
        for cars in self.car:
            cars.backward(self.car_speed)

    def speed_increase(self):
        self.car_speed+=MOVE_INCREMENT
