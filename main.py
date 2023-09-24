import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()

screen.onkeypress(player.moving_forward, "Up")

game_is_on = True
while game_is_on:
    scoreboard.update_scoring()
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.car_move()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish():
        player.go_to_start()
        scoreboard.scoring_point()
        car_manager.level_up()

screen.exitonclick()
