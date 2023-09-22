# import colorgram
import turtle
import random

# rgb_colors = []
# colors = colorgram.extract("image.jpg.png", 21)
#
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
#remove 2 colors because it generates white.
turtle.colormode(255)
color_list = [(198, 11, 36), (246, 234, 238), (207, 13, 11), (233, 228, 5), (195, 67, 21), (239, 147, 30), (45, 210, 59), (30, 91, 187), (34, 32, 153), (17, 25, 54), (245, 38, 143), (68, 10, 52), (224, 249, 240), (61, 205, 231), (14, 203, 220), (247, 43, 12), (64, 25, 11), (223, 20, 102), (14, 150, 30)]

shin = turtle.Turtle()
shin.speed("fastest")
shin.penup()
shin.hideturtle()
shin.setheading(220)
shin.forward(300)
shin.setheading(0)
number_of_dots = 100


for dot_count in range(1, number_of_dots + 1):
    shin.dot(20, random.choice(color_list))
    shin.forward(50)

    if dot_count % 10 == 0:
        shin.setheading(90)
        shin.forward(50)
        shin.setheading(180)
        shin.forward(500)
        shin.setheading(0)












screen = turtle.Screen()
screen.exitonclick()
