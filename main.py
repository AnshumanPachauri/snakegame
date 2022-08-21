import turtle
from turtle import Turtle,Screen
t=Turtle()
scr=Screen()
def fn1():
    t.forward(10)
def fn2():
    t.backward(10)
def fn3():
    new=t.heading()+5
    t.setheading(new)
def fn4():
    new=t.heading()-5
    t.setheading(new)
def fn5():
    t.circle(50)
def fn6():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

scr.listen()
scr.onkey(fn1,'Up')
scr.onkey(fn2,'Down')
scr.onkey(fn3,'Right')
scr.onkey(fn4,'Left')
scr.onkey(fn5,'space')
scr.onkey(fn6,'c')
scr.mainloop()