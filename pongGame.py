# A simple pong game in python
# Created by Aayushi Choudhary
# 7/11/2020

import turtle                                                                   # we're using the turtle module for this

wn = turtle.Screen()                                                            # wn is a variable for window
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)                                                                    # helps speed up game by not letting a window update

# -------------------------------------------------------------------------------- Score -------------------------------------------------------------------------------------

score_a = 0
score_b = 0

# --------------------------------------------------------------------------------- Paddle A ---------------------------------------------------------------------------------

paddle_a = turtle.Turtle()                                                      # turtle object
paddle_a.speed(0)                                                               # sets the speed of animation to the max possible
paddle_a.shape("square")                                                        # gives the paddle a shape
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()                                                                # turtles ususally draw a line when they move across the screen
                                                                                # but we don't want lines so we do a penup
paddle_a.goto(-350, 0)                                                          # this is the x-coordinate in the Game
                                                                                # (0,0) is in the middle of the screen

# --------------------------------------------------------------------------------- Paddle B ---------------------------------------------------------------------------------

paddle_b = turtle.Turtle()                                                      # turtle object
paddle_b.speed(0)                                                               # sets the speed of animation to the max possible
paddle_b.shape("square")                                                        # gives the paddle a shape
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()                                                                # turtles ususally draw a line when they move across the screen
                                                                                # but we don't want lines so we do a penup
paddle_b.goto(350, 0)                                                           # this is the x-coordinate in the Game
                                                                                # (0,0) is in the middle of the screen

# --------------------------------------------------------------------------------- Ball -------------------------------------------------------------------------------------

ball = turtle.Turtle()                                                          # turtle object
ball.speed(0)                                                                   # sets the speed of animation to the max possible
ball.shape("square")                                                            # gives the paddle a shape
ball.color("white")
ball.penup()                                                                    # turtles ususally draw a line when they move across the screen
                                                                                # but we don't want lines so we do a penup
ball.goto(0, 0)                                                                 # this is the x-coordinate in the Game
                                                                                # (0,0) is in the middle of the Screen

ball.dx = 0.1                                                                   # represents movement in the x direction
ball.dy = -0.1                                                                  # represents mocvement in the y direction

# --------------------------------------------------------------------------------- Pen --------------------------------------------------------------------------------------

pen = turtle.Turtle()                                                           # small t for the module name and capital T for the class name
pen.speed(0)                                                                    #animation speed
pen.color("white")
pen.penup()                                                                     # because we don't want to draw a line
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align = "center", font = ("Courier", 24, "normal"))

# --------------------------------------------------------------------------------- Function ---------------------------------------------------------------------------------

def paddle_a_up():                                                              # function that moves paddle A up
    y = paddle_a.ycor()                                                         # to move the paddle A up, we need to know the y coordinate
                                                                                # we're storing the value of the ycor in a variable named y
    y += 20                                                                     # will add 20 pixels to the y coordinate
    paddle_a.sety(y)

def paddle_a_down():                                                            # function that moves paddle A down
    y = paddle_a.ycor()                                                         # to move the paddle A down, we need to know the y coordinate
                                                                                # we're storing the value of the ycor in a variable named y
    y -= 20                                                                     # will subtract 20 pixels from the y coordinate
    paddle_a.sety(y)

def paddle_b_up():                                                              # function that moves paddle B up
    y = paddle_b.ycor()                                                         # to move the paddle B up, we need to know the y coordinate
                                                                                # we're storing the value of the ycor in a variable named y
    y += 20                                                                     # will add 20 pixels to the y coordinate
    paddle_b.sety(y)

def paddle_b_down():                                                            # function that moves paddle B down
    y = paddle_b.ycor()                                                         # to move the paddle A down, we need to know the y coordinate
                                                                                # we're storing the value of the ycor in a variable named y
    y -= 20                                                                     # will subtract 20 pixels from the y coordinate
    paddle_b.sety(y)

# --------------------------------------------------------------------------Keyboard binding ---------------------------------------------------------------------------------

wn.listen()                                                                     # tells the window to listen for keyboard input
wn.onkeypress(paddle_a_up, "w")                                                 # when the user presses 'w', call the function paddle_a_up
wn.onkeypress(paddle_a_down, "s")                                               # when the user presses 's', call the function paddle_a_down
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# ----------------------------------------------------------------------------- Main game loop -------------------------------------------------------------------------------

while True:
    wn.update()                                                                 # every time the loop runs, it updates the Screen

    # move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() > 290:                                                       # top border
        ball.sety(290)
        ball.dy *= -1                                                           # reverses the direction of the ball

    if ball.ycor() < -290:                                                      # bottom border
        ball.sety(-290)
        ball.dy *= -1                                                           # reverses the direction of the ball

    if ball.xcor() > 390:                                                       # right border
        ball.goto(0, 0)                                                         # put the ball back to the center
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align = "center", font = ("Courier", 24, "normal"))

    if ball.xcor() < -390:                                                      # left border
        ball.goto(0, 0)                                                         # put the ball back to the center
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align = "center", font = ("Courier", 24, "normal"))

    # paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
