from turtle import Turtle


class ScoreBord(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.color("white")
        self.goto(0, 280)
        self.write(arg=f"score : {self.score}", align="center", font=('Courier', 14, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over!", align="center", font=('Courier', 14, 'normal'))

    def score_increase(self):
        self.clear()

        self.score += 1
        self.write(arg=f"score : {self.score}", align="center", font=('Arial', 14, 'normal'))
