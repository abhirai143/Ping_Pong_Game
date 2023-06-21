from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from score import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)

paddle = Turtle()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision to wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect the collision to paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # when pass over the right paddle
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    # when pass over the left paddle
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()
screen.exitonclick()
