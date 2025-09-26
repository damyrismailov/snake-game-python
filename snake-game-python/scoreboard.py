from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as f:
            self.high_score = int(f.read())
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()
    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)
    def reset_score(self):
        if self.score > self.high_score:
           self.high_score = self.score
           with open("data.txt","a") as new:
               new.write(f"{self.high_score}")

        self.score = 0
        self.update_score()


    def increase_score(self):
        self.score += 1
        self.update_score()