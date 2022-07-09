"""
    Step 5: Create a scoreboard that keeps track of which level
    the user is on. Every time the turtle player does a
    successful crossing, the level should increase. When
    the turtle hits a car, GAME OVER should be displayed
    in the centre. If you get stuck, check the video
    walk through in Step 7.
"""

from turtle import Turtle
FONT = ("Arial Bold", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-260, 260)
        self.level = 1
        self.hideturtle()
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.level}", False, "left", FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", FONT)
