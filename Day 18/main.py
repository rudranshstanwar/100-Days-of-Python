# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     my_tuple = (r,g,b)
#     rgb_colors.append(my_tuple)
import turtle as t
import random

rgb_colors = [(236, 35, 108), (145, 28, 66), (230, 237, 232), (239, 75, 35), (7, 148, 95), (220, 171, 45), (183, 158, 47), (45, 191, 232), (28, 127, 194), (254, 223, 0), (125, 192, 78), (85, 27, 91), (243, 218, 56), (178, 40, 98), (44, 170, 114), (211, 132, 166), (206, 57, 35), (239, 162, 193), (145, 27, 25), (243, 167, 156), (163, 211, 178), (26, 187, 225), (6, 116, 54), (138, 210, 232), (74, 135, 184), (170, 191, 221), (114, 10, 8)]

jack = t.Turtle()
current_position = jack.heading()
t.colormode(255)
jack.setheading(225)
jack.pu()
jack.fd(300)
jack.setheading(0)

def paint():
    jack.speed(0)
    for _ in range(10):
        jack.dot(20, random.choice(rgb_colors))
        jack.forward(50)
for _ in range(10):
    paint()
    jack.setheading(90)
    jack.forward(50)
    jack.setheading(180)
    jack.forward(500)
    jack.setheading(0)



screen = t.Screen()
screen.exitonclick()
