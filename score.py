from turtle import Turtle

SC=0
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.lsc=0
        self.rsc=0
        self.upd()
    def upd(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.lsc,align="center",font=("courier",60,"normal"))
        self.goto(100,200)
        self.write(self.rsc,align="center",font=("courier",60,"normal"))
    def lpoin(self):
        self.lsc+=1
        self.upd()
    def rpoin(self):
        self.rsc+=1
        self.upd()