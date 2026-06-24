from turtle import Turtle,Screen
import time
import random
window=Screen()
window.setup(width=800,height=800)
window.bgcolor("Black")
#استخدم تريسر حتى راس الثعبان ما يفتر وضروري اخلي بنهايه الكود وندو ابديت
window.tracer(0)
position=[(-40,0),(-20,0),(0,0),(20,0),(40,0),(60,0),(80,0)]
angles=(90,0,0,0)
turtles=[]
for i in range(len(position)):
    new_turtle=Turtle("square")
    new_turtle.color("white")
    new_turtle.penup()
    new_turtle.goto(position[i])
    turtles.append(new_turtle)

game_on=True
while game_on:

   for i in range(len(turtles)-1) :    
       turtles[i].goto(turtles[i+1].pos())
   turtles[-1].forward(20)
   turtles[-1].left(random.choice(angles))
   window.update()
   time.sleep(0.1)
    

window.exitonclick()