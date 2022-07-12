import turtle


class Position(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def go_to(self, pos_x, pos_y, state_name):

        self.goto(pos_x, pos_y)
        self.write(state_name, False, "center", ("Arial", 8, "normal"))
        # You could also write this in line 29 in main.py as object.write(a.state.item())
