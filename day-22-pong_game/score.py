from turtle import Turtle


class Score(Turtle):
    def __init__(self, x: int, y: int = 250):
        super().__init__()

        self.score = 0

        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x, y)
        self.write_score()

    def write_score(self):
        self.write(self.score, font=("Courier", 40, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write_score()