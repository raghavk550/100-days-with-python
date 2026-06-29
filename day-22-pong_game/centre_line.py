from turtle import Turtle


class CenterLine(Turtle):
    def __init__(self, yCor: int, xCor: int = 0):
        super().__init__()

        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(xCor, -yCor)
        self.setheading(90)
        while self.ycor() < yCor:
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)