import turtle


# Create screen
screen = turtle.Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(1000, 1000)


# Left Pad
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.color("white")
left_pad.shape("square")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400, 0)


# Right Pad
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.color("white")
right_pad.shape("square")
right_pad.shapesize(stretch_wid=6, stretch_len=2)
right_pad.penup()
right_pad.goto(400, 0)


# Ball
pong_ball = turtle.Turtle()
pong_ball.speed(40)
pong_ball.color("white")
pong_ball.shape("circle")
pong_ball.penup()
pong_ball.goto(0, 0)
pong_ball.dx = 5
pong_ball.dy = -5


# Initial Scores
left_player = 0
right_player = 0


# Display the score
pen = turtle.Turtle()
pen.color("white")
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Left Player: {left_player}    Right Player: {right_player}",
             align="center", font=("Courier", 24, "normal"))


# Functions for moving paddles
def left_paddle_up():
    y = left_pad.ycor()
    y += 20
    left_pad.sety(y)


def left_paddle_down():
    y = left_pad.ycor()
    y -= 20
    left_pad.sety(y)


def right_paddle_up():
    y = right_pad.ycor()
    y += 20
    right_pad.sety(y)


def right_paddle_down():
    y = right_pad.ycor()
    y -= 20
    right_pad.sety(y)


# Key bindings
screen.listen()
screen.onkeypress(left_paddle_up, "w")
screen.onkeypress(left_paddle_down, "s")
screen.onkeypress(right_paddle_up, "Up")
screen.onkeypress(right_paddle_down, "Down")


# Game
while True:
    screen.update()

    pong_ball.setx(pong_ball.xcor()+pong_ball.dx)
    pong_ball.sety(pong_ball.ycor()+pong_ball.dy)

    # Borders
    match pong_ball:
        case value if pong_ball.ycor() > 350:
            pong_ball.sety(350)
            pong_ball.dy *= -1

        case value if pong_ball.ycor() < -350:
            pong_ball.sety(-350)
            pong_ball.dy *= -1

        case value if pong_ball.xcor() > 500:
            pong_ball.goto(0, 0)
            pong_ball.dy *= -1
            left_player += 1
            pen.clear()
            pen.write(f"Left Player: {left_player}    Right Player: {right_player}",
                      align="center", font=("Courier", 24, "normal"))

        case value if pong_ball.xcor() < -500:
            pong_ball.goto(0, 0)
            pong_ball.dy *= -1
            right_player += 1
            pen.clear()
            pen.write(f"Left Player: {left_player}    Right Player: {right_player}",
                      align="center", font=("Courier", 24, "normal"))


    # Collisions
    match pong_ball:
        case value if (pong_ball.xcor() > 360 and pong_ball.xcor() < 370) and (pong_ball.ycor() < right_pad.ycor()+40 and pong_ball.ycor() > right_pad.ycor()-40):
            pong_ball.setx(360)
            pong_ball.dx*=-1

        case value if (pong_ball.xcor()<-360 and pong_ball.xcor()>-370) and (pong_ball.ycor()<left_pad.ycor()+40 and pong_ball.ycor()>left_pad.ycor()-40):
            pong_ball.setx(-360)
            pong_ball.dx*=-1

