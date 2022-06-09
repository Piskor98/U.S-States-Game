import turtle
from turtle import Turtle

class Title(Turtle):
    def __init__(self):
        super(Title, self).__init__()
        self.penup()
        self.hideturtle()
        self.color('Blue')
        self.setposition(0,270)
        self.write('U.S. States Game',align='center',font=('Arial',28,'normal'))