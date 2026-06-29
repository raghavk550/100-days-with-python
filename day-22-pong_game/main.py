from turtle import Turtle, Screen
import time

from ball import Ball
from centre_line import CenterLine
from paddle import Paddle
from score import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Center line
center_line = CenterLine(600)

# Ball
ball = Ball()

# Paddle
left_pong = Paddle(-360)
right_pong = Paddle(350)

# Scoreboard
left_score = Score(-100)
right_score = Score(100)

screen.update()

screen.listen()

screen.onkey(left_pong.move_up, "w")
screen.onkey(left_pong.move_down, "s")
screen.onkey(right_pong.move_up, "Up")
screen.onkey(right_pong.move_down, "Down")

is_game_on = True

while is_game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    if ((ball.distance(right_pong) < 50 and ball.xcor() > 320)
            or (ball.distance(left_pong) < 50 and ball.xcor() < -330)):
        ball.strike()
    if ball.pos()[0] > 370:
        left_score.increase_score()
        ball.reset_ball()
    elif ball.pos()[0] < -380:
        right_score.increase_score()
        ball.reset_ball()


screen.exitonclick()