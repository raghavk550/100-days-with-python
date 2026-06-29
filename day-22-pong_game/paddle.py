from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,x,y = 0):
        super().__init__()

        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x, y)

    def move_up(self, y_cor: int = 250):
        if self.pos()[1] < y_cor:
            self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self, y_cor: int = 230):
        if self.pos()[1] > -y_cor:
            self.goto(self.xcor(), self.ycor() - 20)