from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVEMENT = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.class_snake()
        self.head = self.segments[0]

    def class_snake(self):
        for pos in STARTING_POSITION:
            self.add_snake(pos)

    def add_snake(self, pos):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(pos)
        self.segments.append(new_segment)

    def extend_snake(self):
        self.add_snake(self.segments[-1].position())

    def move(self):
        for seg_num in range((len(self.segments) - 1), 0, -1):
            new_segment_pos = self.segments[seg_num - 1].pos()
            self.segments[seg_num].goto(new_segment_pos)

        self.head.forward(MOVEMENT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
