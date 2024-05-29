import turtle
import winsound

win = turtle.Screen()
win.title("ping pong by Yash")
win.bgcolor("white")
win.setup(width=800, height=600)
win.tracer(0)


#score

score1 = 0
score2 = 0

#paddle A
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("blue")
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.penup()
paddle1.goto(-350, 0)


#paddle B
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("red")
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.penup()
paddle2.goto(350, 0)


#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = -0.1


#score 
pen = turtle.Turtle()
pen.speed(0)
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B = 0", align="center", font=("teko",24,"normal"))



# functions to move paddle

def paddle1_up():
    y = paddle1.ycor()
    y += 20
    paddle1.sety(y)

def paddle1_down():
    y = paddle1.ycor()
    y -= 20
    paddle1.sety(y)


def paddle2_up():
    y = paddle2.ycor()
    y += 20
    paddle2.sety(y)

def paddle2_down():
    y = paddle2.ycor()
    y -= 20
    paddle2.sety(y)

#keyboard binding
win.listen()
win.onkeypress(paddle1_up, "w")
win.onkeypress(paddle1_down, "s")
win.onkeypress(paddle2_up, "Up")
win.onkeypress(paddle2_down, "Down")


#main loop

while True:
    win.update()


    #moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    #border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("wave.mp3", winsound.SND_ASYNC )


    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("wave.mp3", winsound.SND_ASYNC )

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        pen.clear()
        pen.write("Player A: {} Player B = {}".format(score1, score2), align="center", font=("teko",24,"normal"))


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        pen.clear()
        pen.write("Player A: {} Player B = {}".format(score1, score2), align="center", font=("teko",24,"normal"))

    # paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350 )and (ball.ycor() < paddle2.ycor() + 40 and ball.ycor() > paddle2.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("wave.mp3", winsound.SND_ASYNC )

    
    if (ball.xcor() < -340 and ball.xcor() > -350 )and (ball.ycor() < paddle1.ycor() + 40 and ball.ycor() > paddle1.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("wave.mp3", winsound.SND_ASYNC )
    

