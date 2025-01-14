import time
from turtle import Screen

import scoreboard
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)
player = Player()
cars = CarManager()
cars.hideturtle()
screen.listen()
scoreboard=Scoreboard()
screen.onkey(player.go_up, "w")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.car_creation()
    cars.movement()
    for c in cars.car:
        if c.distance(player) < 20:
            game_is_on= False
            scoreboard.game_over()

    if player.is_at_finish():
        player.go_to_start()
        cars.speed_increase()
        scoreboard.increase_level()

screen.exitonclick()
