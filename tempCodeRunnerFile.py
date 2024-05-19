#Detect Collision with wall
    # if ball.ycor()>280 or ball.ycor()<-280:
    #     ball.bouncey()
    
    # #Collision with paddle
    # if ball.distance(pad1)<50 and ball.xcor()>320 or ball.distance(pad2)<50 and ball.xcor()<-320:
    #     ball.bouncex()
    

    # #Beyond Right paddel
    # if ball.xcor()>380:
    #     ball.resetp()
    #     score.lpoin()
    #     if score.lsc>m:
    #         print("Right Palyer Won!!!!")
    #         game= False
    
    # #Beyond Left paddel
    # if ball.xcor()<-380:
    #     ball.resetp()
    #     score.rpoin()
    #     if score.rsc>m:
    #         print("Left Palyer Won!!!!")
    #         game= False