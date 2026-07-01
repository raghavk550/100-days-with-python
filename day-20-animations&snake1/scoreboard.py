from turtle import Turtle

FILE_NAME = "high_score.txt"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.speed("fastest")
        self.read_high_score()
        self.write_score()

    def increase_score(self):
        self.score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(-120, 270)
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))
        self.goto(120, 270)
        self.write(f"High Score: {self.high_score}", align="center", font=("Courier", 24, "normal"))

    def reset_score(self):
        self.high_score = self.score if self.score > self.high_score else self.high_score
        self.write_high_score()
        self.score = 0
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Courier", 24, "normal"))

    def write_high_score(self):
        with open(FILE_NAME, "w") as file:
            file.write(str(self.high_score))

    def read_high_score(self):
        try:
            with open(FILE_NAME, "r") as file:
                file_score = file.read()
                print(file_score)
                self.high_score = int(file_score)
                print(self.high_score)
        except:
            self.high_score = 0