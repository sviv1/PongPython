import turtle
import time

# score
pts_a = 0
pts_b = 0

wn = turtle.Screen()
wn.title("Pong by Viv1")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(1)

# paddle_A

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("blue")
paddle_a.penup()   # no drawing when moving
paddle_a.goto(-350, 0)

# paddle_B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("yellow")
paddle_b.penup()   # no drawing when moving
paddle_b.goto(350, 0)

# ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()   # no drawing when moving
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# scorecard

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


# Functions

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard interaction

wn.listen()
wn.onkeypress(paddle_a_up, "s")
wn.onkeypress(paddle_a_down, "d")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# Function to display the winner and terminate after 5 seconds
def display_winner(winner):
    pen.clear()
    pen.write("{} wins!".format(winner), align="center", font=("Courier", 24, "normal"))
    time.sleep(5)  # Delay for 5 seconds
    wn.bye()  # Terminate the game


while True:
    wn.update()
    # make the ball move
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Taking Care of the Boundary
    if ball.ycor() > 290:  # upper boundary check
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:  # upper boundary check
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        pts_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {} ".format(pts_a, pts_b), align="center", font=("Courier", 24, "normal"))

        if pts_a >= 10:
            display_winner("Player A")

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        pts_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {} ".format(pts_a, pts_b), align="center", font=("Courier", 24, "normal"))

        if pts_b >= 10:
            display_winner("Player B")

    # paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
