from turtle import Turtle

#نسوي الكلاس الخاص بلعبة سناك ونسوي ميثود تنشئ جسم الثعبان وتضيف الاجزاء للسته
class Snake:
    #هنا كلمة سيلف باعتبار كلمة سام لان ربطنا ملف ماين دون بي واي ويا سناك دوت بي واي
    #من استوردنا الكلاس في ماين دوت بي واي هنا راح يشتغل كلمه سيلف كانما كلما سام
    def __init__(self):
        self.turtles=[]
        self.postion=[(-40,0),(-20,0),(0,0)]
        #نخلي الانت ميثود تنادي على الميثود مال الانشاء اللي هي كرييت سناك
        self.create_snake()
        #انشاء متغير لراس الثعبان
        self.head=self.turtles[-1]

    def create_snake(self):
        for i in range(len(self.postion)):
            new_turtle=Turtle("square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(self.postion[i])
            self.turtles.append(new_turtle)

    def move(self):
        for i in range(len(self.turtles)-1):
            self.turtles[i].goto(self.turtles[i+1].pos())

        self.head.forward(20)

    def extend(self):
        new_segment=Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(self.turtles[0].pos())
        self.turtles.insert(0,new_segment)

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def right(self):
        self.head.setheading(0)

    def left(self):
        self.head.setheading(180)


    
