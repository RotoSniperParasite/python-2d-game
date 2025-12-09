import turtle as t
from turtle import *
import tkinter as Tk

t = t.Turtle()
setup(700,700)
window = Screen()
t.penup()


def move_up():
  t.setheading(90)
  t.forward(20)

def move_down():
  t.setheading(270)
  t.forward(20)

def move_left():
  t.setheading(180)
  t.forward(20)

def move_right():
  t.setheading(0)
  t.forward(20)

window.listen()
window.onkey(move_up, "Up")
window.onkey(move_down, "Down")
window.onkey(move_left, "Left")
window.onkey(move_right, "Right")

mainloop()