from turtle import Turtle,Screen
import time
scr=Screen()
scr.setup(1200,700)
scr.bgcolor('black')
scr.title('SNAKE GAME')
scr.tracer(0)


l=[0,22,44]
l2=[]

for i in range(3):
    t = Turtle()
    t.shape('square')
    t.color('white')
    t.penup()
    t.goto(i-l[i],0)
    l2.append(t)

def left():
    l2[0].left(90)
def right():
    l2[0].right(90)

def up():
        l2[0].forward(20)

def down():
        l2[0].backward(20)

game_on=True
scr.listen()
while game_on:
    scr.update()
    time.sleep(.1)
    for i in range(2,0,-1):
        previous=l2[i-1].position()
        l2[i].goto(previous)

    l2[0].forward(20)
    scr.onkey(left, 'Left')
    scr.onkey(right,'Right')
    scr.onkey(up, 'Up')
    scr.onkey(down,'Down')


scr.mainloop()