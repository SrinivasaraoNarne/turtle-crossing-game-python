from turtle import Turtle, Screen
import random

turtles = [Turtle(), Turtle(), Turtle(), Turtle(), Turtle(), Turtle(), Turtle()]
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

for i, turtle in enumerate(turtles):
    turtle.color(colors[i])
    turtle.shape("turtle")

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Pick a Color: ")

for i, turtle in enumerate(turtles):
    turtle.penup()
    turtle.goto(-230, -100 + i * 40)

is_race = False

if user_bet:
    is_race = True

while is_race:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race = False
            winning = turtle.pencolor()
            if winning == user_bet:
                print(f"You've won! The {winning} turtle is the winner!")
            else:
                print(f"You've lost! The {winning} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
