from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as data:
            self.high_score=int(data.read())

        self.color("white")
        self.penup()
        self.goto(0,270)
        self.update()
        self.hideturtle()

    def update(self):
        self.clear()
        self.write(f"score: {self.score} High Score: {self.high_score}",False,align="center",font=("courier",18,"normal"))
    def inc_score(self):
        self.score+=1
        self.update()

    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("data.txt",mode="w") as data:
                data.write(f"{self.high_score}")
        self.score=0
        self.update()
    #def game_over(self):
    #    self.goto(0,0)
    #   self.write("GAME OVER",align="center",font=("courier",24,"normal"))