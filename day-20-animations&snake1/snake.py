from turtle import Turtle

class Snake:
    def __init__(self):
        x_cor = 0
        self.segments = []

        for _ in range(3):
            tim = Turtle()
            tim.penup()
            tim.color("white")
            tim.shape("square")
            tim.goto(x_cor, 0)
            x_cor = x_cor - 20
            self.segments.append(tim)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            second_segment = self.segments[seg_num - 1]
            self.segments[seg_num].goto(second_segment.xcor(), second_segment.ycor())
        self.segments[0].forward(20)

    def increase_segment(self):
        tim = Turtle()
        tim.penup()
        tim.color("white")
        tim.shape("square")
        self.segments.append(tim)
        self.move()

    def move_snake_up(self):
        segment = self.segments[0]
        if segment.heading() == 0 or segment.heading() == 180:
            segment.setheading(90)

    def move_snake_down(self):
        segment = self.segments[0]
        if segment.heading() == 0 or segment.heading() == 180:
            segment.setheading(270)

    def move_snake_left(self):
        segment = self.segments[0]
        if segment.heading() == 90 or segment.heading() == 270:
            segment.setheading(180)

    def move_snake_right(self):
        segment = self.segments[0]
        if segment.heading() == 90 or segment.heading() == 270:
            segment.setheading(0)