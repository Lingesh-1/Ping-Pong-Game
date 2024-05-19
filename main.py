from turtle import Screen
from paddel import Pad
import time
from ball import Ball
from random import randint as r
from score import Score


m=int(input("Best of?\n"))


myscr=Screen()
myscr.title('Ping Pong 🏓')
myscr.bgcolor('dark blue')
myscr.setup(width=800,height=600)
myscr.tracer(0)



pad1=Pad((350,0))
pad2=Pad((-350,0))
ball= Ball()
score=Score()

myscr.listen()
myscr.onkey(pad1.up,'Up')
myscr.onkey(pad1.down,'Down')
myscr.onkey(pad2.up,'w')
myscr.onkey(pad2.down,'s')


game=True
while game:
    time.sleep(ball.msp)
    myscr.update()
    ball.move()

    #Detect Collision with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bouncey()
    
    #Collision with paddle
    if ball.distance(pad1)<50 and ball.xcor()>320 or ball.distance(pad2)<50 and ball.xcor()<-320:
        ball.bouncex()
    

    #Beyond Right paddel
    if ball.xcor()>380:
        ball.resetp()
        score.lpoin()
        if score.lsc>m:
            print("Right Palyer Won!!!!")
            game= False
    
    #Beyond Left paddel
    if ball.xcor()<-380:
        ball.resetp()
        score.rpoin()
        if score.rsc>m:
            print("Left Palyer Won!!!!")
            game= False
       












































myscr.exitonclick()