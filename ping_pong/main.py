from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from score import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Noor : ping pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

default_sleep = 0.1
MIN_SLEEP = 0.02

game_on = True
while game_on:
    screen.update()
    time.sleep(default_sleep)

    # تحريك الكرة
    ball.goto(ball.xcor() + ball.x_move, ball.ycor() + ball.y_move)

    # تصادم مع الحائط العلوي والسفلي
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.y_move *= -1

    # تصادم مع المضارب (التصحيح هنا)
    if (ball.xcor() > 330 and ball.distance(r_paddle) <= 50) or \
       (ball.xcor() < -330 and ball.distance(l_paddle) <= 50):
        ball.x_move *= -1
        default_sleep *= 0.9          # ❗ بدل += 0.9
        if default_sleep < MIN_SLEEP:
            default_sleep = MIN_SLEEP

    # خرجت من جهة اليمين
    if ball.xcor() > 400:
        ball.goto(0, 0)
        ball.x_move *= -1             # ❗ بدل += -1
        default_sleep = 0.1
        scoreboard.l_point()

    # خرجت من جهة اليسار
    if ball.xcor() < -400:
        ball.goto(0, 0)
        ball.x_move *= -1
        default_sleep = 0.1
        scoreboard.r_point()

     

screen.exitonclick()