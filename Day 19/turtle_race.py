from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ")

if user_bet:
    is_race_on = True

def start_coordinate(turtle, color, position):
    turtle.shape("turtle")
    turtle.color(color)
    turtle.pu()
    turtle.setposition(-200, position)
    turtle.pd()

turtle_1 = Turtle()
start_coordinate(turtle_1,"violet", 150)

turtle_2 = Turtle()
start_coordinate(turtle_2,"blue", 100)

turtle_3 = Turtle()
start_coordinate(turtle_3, "green", 50)

turtle_4 = Turtle()
start_coordinate(turtle_4, "yellow", 0)

turtle_5 = Turtle()
start_coordinate(turtle_5, "orange", -50)

turtle_6 = Turtle()
start_coordinate(turtle_6, "red", -100)

turtle_list = [turtle_1, turtle_2, turtle_3, turtle_4, turtle_5, turtle_6]

while is_race_on:
    for turtle in turtle_list:

        if turtle.xcor() > 200:
            is_race_on = False

            if turtle.pencolor() == user_bet:
                print("Congratulations! You've won")
            else:
                print(f"{turtle.pencolor()} wins the race. You've lost")

        else:
            random_step = random.randint(0, 10)
            turtle.fd(random_step)


screen.exitonclick()