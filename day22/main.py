# create the screen
# create and move a paddle
# create another paddle
# create the ball and make it move
# detect collision with wall and bounce
# detect collision with paddle
# detect when paddle misses
# keep score
import time
import turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
time_speed = 0.1

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up_key, "Up")
screen.onkey(r_paddle.down_key, "Down")
screen.onkey(l_paddle.up_key, "w")
screen.onkey(l_paddle.down_key, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # detect collision with wall
    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.bounce_y()

    # detect collision with either paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect r paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    # Detect l paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()