import turtle
import  time
pencil = turtle.Turtle()
def curve():
    for i in range(200):
        pencil.right(1)
        pencil.forward(1)
def heart():
    pencil.fillcolor("red")
    pencil.begin_fill()
    pencil.left(140)
    pencil.forward(113)
    curve()
    pencil.left(120)
    curve()
    pencil.forward(112)
    pencil.end_fill()
def txt():
    pencil.up()
    pencil.setpos(-68,95)
    pencil.down()
    pencil.color("lightgreen")
    pencil.write("I LOVE PYTHON")
heart()
txt()
time.sleep(10)
pencil.ht()