import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player1 = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player1.move,"Up")

scoreboard.update_scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.createCar()
    car_manager.move_cars()

    for car in car_manager.list_cars():
        if player1.distance(car) < 20:
            player1.reset_player()
            game_is_on = False
    if player1.is_at_finishing_line():
        player1.reset_player()
        car_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick()


