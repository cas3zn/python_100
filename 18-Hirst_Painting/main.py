color_list = [(226, 231, 236), (59, 105, 147), (224, 201, 112), (224, 235, 231), (235, 227, 207), (132, 85, 60),
              (221, 141, 67), (195, 145, 171), (141, 177, 202), (140, 80, 103), (238, 225, 233), (209, 91, 68),
              (68, 108, 92), (188, 81, 117), (133, 181, 136), (129, 134, 76), (47, 155, 191), (64, 156, 93),
              (183, 191, 201), (216, 177, 191)]

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.hideturtle()
tim.speed('fastest')
tim.penup()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
