from turtle import Turtle,Screen
import random
scr=Screen()
scr.setup(1400,400)
l=['red','blue','green','pink','cyan']
l2=[-50,-20,10,40,70]
l3=[]
bet=scr.textinput(title="Make your bet",prompt='which turtle will win the race??...enter a color:')
for i in range(5):
    t = Turtle(shape='turtle')
    t.penup()
    t.goto(-680,l2[i])
    t.color(l[i])
    l3.append(t)
if bet:
    race_on=True
while race_on:
    for t in l3:
        if t.xcor()>650:
            race_on=False
            if bet==t.color()[0]:
                print('Wow....you win')
            else:
                print('you loose...HaHaHaHa')
                print(t.color()[0],'Wins....HaHaHaHaHaHa')
        else:
            x=random.randrange(0,50)
            t.forward(x)

scr.mainloop()