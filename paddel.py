from turtle import Turtle

class Pad(Turtle):
    def __init__(self,cord):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(cord)


    def up(self):
        self.y=self.ycor()+20
        self.goto(self.xcor(),self.y)


    def down(self):
        self.y=self.ycor()-20
        self.goto(self.xcor(),self.y)
    