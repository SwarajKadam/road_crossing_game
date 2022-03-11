from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        
        self.shape("square")
        self.shapesize(stretch_wid=1,stretch_len=2)
        self.penup()
        self.setheading(180)
        self.color(random.choice(COLORS))
        self.reset_car_position()

        
    def reset_car_position(self):      
        self.goto(random.randrange(300,800,10),random.randrange(-240,240,30))      
        
        
    def speed_of_car(self):
        self.forward(STARTING_MOVE_DISTANCE)
        
        
    def increase_carspeed(self):
        global MOVE_INCREMENT,STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE +=MOVE_INCREMENT
        