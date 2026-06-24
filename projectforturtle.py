from turtle import Turtle, Screen
import random
import time

window = Screen()
window.setup(width=800, height=800)

user_name=window.textinput("لحظة من فضلك","(red,  green,  blue)احزر من هو الفائز")


speeds = (1, 3, 5, 7, 9)

sam = Turtle()
sam.shape("turtle")
sam.color("red")
sam.penup()
sam.goto(-380, 200)
sam.speed(random.choice(speeds))

tom = Turtle()
tom.shape("turtle")
tom.color("green")
tom.penup()
tom.goto(-380, 0)
tom.speed(random.choice(speeds))

jac = Turtle()
jac.shape("turtle")
jac.color("blue")
jac.penup()
jac.goto(-380, -200)
jac.speed(random.choice(speeds))

# السباق
while sam.xcor() < 380 and tom.xcor() < 380 and jac.xcor() < 380:
    sam.forward(random.randint(1, 10))
    tom.forward(random.randint(1, 10))
    jac.forward(random.randint(1, 10))


winner=""

if sam.xcor()>=380:
    winner="red"
elif tom.xcor()>=380:
    winner="green"
elif jac.xcor()>=380:
    winner="blue"


result = Turtle()
result.hideturtle()
result.penup()
result.goto(0, 0)


window.bgcolor("Green")

if user_name==winner:
    result.write("YOU WIN 🎉", align="center", font=("Arial", 16, "bold"))

else:
    result.write("YOU LOSE ❌", align="center", font=("Arial", 16, "bold")) 

time.sleep(5)
window.clear()
window.bgcolor("grey")

result.write("Press any place to exit",align="center",font=("Arial",25,"bold"))

window.exitonclick()




