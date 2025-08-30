from turtle  import Turtle, Screen

colors = [
    "red", "blue", "green", "yellow", "orange", "purple",
    "pink", "brown", "black", "gray", "cyan", "magenta",
    "gold", "navy", "turquoise", "violet", "indigo",
    "lime", "maroon", "olive"
]

directions = [0,90,180,270]
step_size = 20
angle_size = 15

class Drawer:
    def __init__(self):
        self.turtle = Turtle()
        self.turtle.shape("arrow")
        self.turtle.home()
        self.screen = Screen()
        self.listen()
        self.screen.exitonclick()

    def listen(self):
        self.screen.listen()
        self.screen.onkey(fun=self.draw_forwards, key='w')
        self.screen.onkey(fun=self.draw_backwards, key='s')
        self.screen.onkey(fun=self.head_counter_clockwise, key='a')
        self.screen.onkey(fun=self.head_clockwise, key='d')
        self.screen.onkey(fun=self.clear, key='c')

    def draw_forwards(self):
        self.turtle.forward(step_size)

    def draw_backwards(self):
        self.turtle.backward(step_size)

    def head_counter_clockwise(self):
        self.turtle.left(angle_size)

    def head_clockwise(self):
        self.turtle.right(angle_size)

    def clear(self):
        self.turtle.clear()
        self.turtle.penup()
        self.turtle.home()
        self.turtle.pendown()

draw = Drawer()
