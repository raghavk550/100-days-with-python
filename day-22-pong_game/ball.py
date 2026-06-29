from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.color("white")
        self.shape("circle")
        self.penup()
        self.speed("slowest")
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move(self):
        self.setpos(self.pos()[0] + self.x_move, self.pos()[1] + self.y_move)

    def bounce(self):
        self.y_move *= -1

    def strike(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    def reset_ball(self):
        self.strike()
        self.goto(0, 0)
        self.ball_speed = 0.1