from turtle import Turtle,Screen
import random
window=Screen()
sam=Turtle()
window.setup(width=800,height=800)
user_name=window.textinput("لحظة من فضلك","احزر من هو الفائز(الاحمر ام الاخصر ام الازرق)")

speeds=(100,200,300,400,500,600,700) 

sam.shape("turtle")
sam.color("red")
sam.penup()
sam.goto(-380,200)
sam.forward(740)

tom=Turtle()
tom.shape("turtle")
tom.color("green")
tom.penup()
tom.goto(-380,0)
tom.forward(740)


jac=Turtle()
jac.shape("turtle")
jac.color("blue")
jac.penup()
jac.goto(-380,-200)
jac.forward(740)
jac,tom,sam.speed(random.choice(speeds))




window.exitonclick()
