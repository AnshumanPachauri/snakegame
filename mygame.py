from turtle import Turtle,Screen
import time
from fuud import Food
from game import Snake
from scoreboard import Score
scr=Screen()
scr.setup(600,600)
scr.bgcolor('black')
scr.title('SNAKE GAME')
scr.tracer(0)
scr.listen()
snake=Snake()
food=Food()
score=Score()
scr.onkey(snake.left, 'Left')
scr.onkey(snake.right, 'Right')
scr.onkey(snake.up, 'Up')
scr.onkey(snake.down, 'Down')

game_on=True
while game_on:
    scr.update()
    time.sleep(.1)
    snake.move()
    #detect collision with food

    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend_snake()
        score.increase_score()

    #detect collision with wall

    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>255 or snake.head.ycor()<-280:
        score.game_over()
        game_on=False

 #   for i in snake.l2[1:]:
#      if snake.head.distance(i)<10:
 #           game_on=False
  #          score.game_over()


scr.mainloop()