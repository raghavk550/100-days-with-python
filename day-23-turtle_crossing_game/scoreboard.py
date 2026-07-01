from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.level = 1
        self.penup()
        self.hideturtle()
        self.color("black")
        self.setposition(-220, 260)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Level: {self.level}", False, align="center", font=FONT)

    def increase_score(self):
        self.level += 1
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", False, align="center", font=FONT)
