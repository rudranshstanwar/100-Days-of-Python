import turtle

jack = turtle.Turtle()

def move_forwards():
    jack.fd(10)

def move_backwards():
    jack.bk(10)

def move_clockwise():
    jack.right(15)

def move_counter_clockwise():
    jack.left(15)

def clear():
    jack.clear()
    jack.pu()
    jack.home()
    jack.pd()

screen = turtle.Screen()

screen.listen()
screen.onkey(fun = move_forwards, key = "w")
screen.onkey(fun = move_backwards, key = "s")
screen.onkey(fun = move_clockwise, key = "d")
screen.onkey(fun = move_counter_clockwise, key = "a")
screen.onkey(fun = clear, key = "c")
screen.exitonclick()