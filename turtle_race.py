from turtle  import Turtle, Screen
from random import choice

colors = [
    "red", "blue", "green", "yellow", "orange", "purple",
    "pink", "brown", "black", "gray", "cyan", "magenta",
    "gold", "navy", "turquoise", "violet", "indigo",
    "lime", "maroon", "olive"
]

speed = ["fastest", "fast", "normal", "slow", "slowest"]

step_size = [5,10,15,20]

n_racing_turtles = 6

class Race:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=600, height=400)
        self.make_turtles()
        
        while (1):
            self.user_bet = self.screen.textinput(title="Make your bet !", prompt="Which turtle do you think will win the race?").lower()
            if self.user_bet in colors:
                break
        
        self.start_race()
        self.screen.exitonclick()

    def make_turtles(self):
        self.racing_turtles = []
        for i in range(n_racing_turtles):
            t = Turtle(shape="turtle")
            t.color(choice(colors))
            t.penup()
            t.goto(-200, -100 + i*40)
            self.racing_turtles.append(t)

    def is_turtle_finish(self, turtle):
        x_position = turtle.pos()[0]
        return x_position >= 200

    def is_user_winner(self, winner_turtle):
        return winner_turtle.color() == self.user_bet
        
    
    def start_race(self):
        still_race = True
        while(still_race):
            for i in range(n_racing_turtles):
                self.racing_turtles[i].forward(choice(step_size))
                
                if self.is_turtle_finish(self.racing_turtles[i]):
                    if self.is_user_winner(self.racing_turtles[i]):
                        print("You win !")
                    else:
                        print ("You loose")
                    still_race = False




race = Race()