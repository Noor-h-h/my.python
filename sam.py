from turtle import Turtle,Screen
import random
window=Screen()
window.setup(width=1000,height=800)
window.bgcolor("black")

sam=Turtle()
sam.shape("turtle")
sam.color("white")
sam.pensize(3)
sam.speed("fastest")

def draw_circle():
    
    for _ in range(20):
        sam.penup()
        sam.goto(-300,-200)
        sam.pendown()
        sam.circle(50)
        sam.left(360/20)

def draw_sqeures():

   for _ in range(40):  
        sam.penup()
        sam.goto(0,0)
        sam.pendown()        
        for _ in range(4):
         sam.forward(100)
         sam.left(90)
        sam.left(10) 
        

def draw_trangles():
    for _ in range(20):
        sam.penup()
        sam.goto(300,200)
        sam.pendown()
        for _ in range(3):
            sam.forward(100)
            sam.left(120)
        sam.left(20)
        
        




draw_circle()
draw_sqeures()
draw_trangles()
window.exitonclick()