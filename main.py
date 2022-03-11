import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
list_of_cars =[]
for i in range(20):
    car = CarManager()
    list_of_cars.append(car)
    
screen.listen()
screen.onkey(player.move,"Up")

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()
    for j in list_of_cars:
        
        if j.xcor()<-300:
            j.reset_car_position()
        j.speed_of_car()
        
        if player.distance(j)<25:
            scoreboard.game_over()
            game_is_on = False
    
        if player.ycor() > 280 :
            scoreboard.increase_level()
            player.reset_player()
            j.increase_carspeed()
        
        
    
        
        
        
screen.exitonclick()