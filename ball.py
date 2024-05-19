from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        # self.shapesize(0,0)
        self.penup()
        # self.move()
        self.xm=10
        self.ym=10
        self.msp=0.1






    def move(self):
        self.goto(x=self.xcor()+self.xm,y=self.ycor()+self.ym)

    def bouncey(self):
        self.ym*=-1

    def bouncex(self):
        self.xm*=-1
        self.msp*=0.9

    def resetp(self):
        self.goto(0,0)
        self.msp=0.1
        self.bouncex()
