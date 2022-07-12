import turtle
import pandas
from position import Position

position = Position()
screen = turtle.Screen()

image = "blank_states_img.gif"
screen.title("U.S. States Game")
screen.addshape(image)
turtle.shape(image)
states = pandas.read_csv("50_states.csv")

states_list = []
correct_guesses = []
game_over = False

for x in states["state"]:
    states_list.append(x)  # For this, you can also use 'states.state.to_list()'

while not game_over:
    answer = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="What's another state's "
                                                                                        "name?").title()
    if answer in states_list:
        correct_guesses.append(answer)
        a = states[states.state == answer]
        x_pos = int(a.x)
        y_pos = int(a.y)
        position.go_to(pos_x=x_pos, pos_y=y_pos, state_name=answer)
        print(correct_guesses)

    if len(correct_guesses) == 50:
        game_over = True


screen.exitonclick()
