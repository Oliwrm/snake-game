from turtle import Turtle

positions = [(0, 0), (-20, 0), (-40, 0)]
class Snake:

    def __init__(self):

        self.x = 0
        self.y = 0
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in positions:
            self.add_segment(position)

    def add_segment(self,position):
        num = Turtle(shape="square")
        num.color("white")
        num.penup()
        num.goto(position)
        self.segments.append(num)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)
    def up(self):
        if self.segments[0].heading()!=270:
            self.segments[0].setheading(90)
    def down(self):
        if self.segments[0].heading()!=90:
            self.segments[0].setheading(270)
    def left(self):
        if self.segments[0].heading()!=0:
            self.segments[0].setheading(180)
    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)