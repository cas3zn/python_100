from turtle import Turtle
FONT = ("Arial", 10, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.new_high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.new_high_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.new_high_score:
            self.new_high_score = self.score
            with open("data.txt", mode="w") as high_score:
                high_score.write(str(self.new_high_score))
        self.score = 0
        self.update_scoreboard()