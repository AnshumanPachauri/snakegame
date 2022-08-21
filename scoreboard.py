from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.update_screen()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=('Courier', 24, 'normal'))


    def update_screen(self):
        self.write(f'SCORE:{self.score}', align='center', font=('Courier', 24, 'normal'))

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_screen()
