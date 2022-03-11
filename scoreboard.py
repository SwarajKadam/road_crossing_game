from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.lvl = 1
        self.update()
        
    def update(self):
        self.clear()
        self.goto(-250,250)
        self.write(arg = "Level", align="center", font=FONT)
        self.goto(-180,250)       
        self.write(arg = self.lvl, align="center", font=FONT)
        
        
    def increase_level(self):
        self.lvl+=1
        self.update()
        
    def game_over(self):
        self.goto(0,0)
        self.write(arg = "Game Over", align="center", font=FONT)