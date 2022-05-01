
from time import sleep
import turtle as tr

#start creating star with turtle

def draw_star():
    t= tr.Turtle()
    t.penup()
    t.goto(-50,-50)
    t.pendown()
    t.color("green")
    t.width(5)
    t.left(36)
    for i in range(5):
        t.forward(200)
        t.left(144)
    t.penup()
    t.goto(0,0)
    t.pendown()


#draw square
def draw_square():
    t= tr.Turtle()
    t.penup()
    t.goto(-300,-300)
    t.pendown()
    t.fillcolor("red")
    t.begin_fill()
    t.color("red")
    t.width(4)
    
    for i in range(5):
        t.forward(600)
        t.left(90)
    t.end_fill()
    t.penup()
    t.goto(0,0)
    t.pendown()




draw_square()
draw_star()
sleep(5)