from turtle import Turtle
l=[(0,0),(22,0),(44,0)]

move_distance=20
UP=90
DOWN=270
LEFT=0
RIGHT=180
class Snake():
    def __init__(self):
        self.l2 = []
        self.create_snake()
        self.head=self.l2[0]

    def create_snake(self):
        for position in l:
            self.add_segment(position)


    def add_segment(self,position):
        segment = Turtle()
        segment.shape('square')
        segment.color('white')
        segment.penup()
        segment.goto(position)
        self.l2.append(segment)

    def extend_snake(self):
        self.add_segment(self.l2[-1].position())


    def move(self):
        for i in range(len(self.l2)-1,0,-1):
            self.new_x=self.l2[i-1].xcor()
            self.new_y = self.l2[i - 1].ycor()
            self.l2[i].goto(self.new_x,self.new_y)
        self.l2[0].forward(20)

    def left(self):
        if self.head.heading()==UP:
            self.head.setheading(RIGHT)

        if self.head.heading()==DOWN:
            self.head.setheading(RIGHT)

    def right(self):

        if self.head.heading() == UP:
            self.head.setheading(LEFT)

        if self.head.heading() == DOWN:
            self.head.setheading(LEFT)

    def up(self):

        if self.head.heading() == RIGHT:
            self.head.setheading(UP)

        if self.head.heading() == LEFT:
            self.head.setheading(UP)


    def down(self):

        if self.head.heading() == RIGHT:
            self.head.setheading(DOWN)

        if self.head.heading() == LEFT:
            self.head.setheading(DOWN)

