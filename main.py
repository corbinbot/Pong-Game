from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

puji = Turtle()
screen = Screen()

screen.title("PONG GAME")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

scoreboard = Scoreboard()
speed = 1
pooja = Ball()
pooja.penup()
pooja.speed(speed)


screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True


while game_is_on:
    time.sleep(pooja.move_speed)
    pooja.start_move_up()
    screen.update()
    if pooja.ycor() > 280 or pooja.ycor() < -280:
        pooja.bounce_y()

    if pooja.distance(r_paddle) < 50 and pooja.xcor() > 320 or pooja.distance(l_paddle) < 50 and pooja.xcor() < -320:
        pooja.bounce_x()
        speed += 1

    if pooja.xcor() > 380:

        pooja.reverse()
        scoreboard.l_point()

    if pooja.xcor() < -380:

        pooja.reverse()
        scoreboard.r_point()


# while not game_is_on:
#
#     # if pooja.ycor()  280 and pooja.xcor() != 380:
#         screen.tracer(1)
#         pooja.start_move_down()
#         screen.update()



screen.exitonclick()
r_paddle.go_up()
r_paddle.go_down()
