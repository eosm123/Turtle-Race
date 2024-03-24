from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.up()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=-100 + turtle_index * 40)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} is the winner!")
            else:
                print(f"You've lost! The {winning_color} is the winner!")
        rand_dist = random.randint(0,10)
        turtle.forward(rand_dist)

screen.exitonclick()




#
# def move_forward():
#     tim.forward(10)
#
# def move_back():
#     tim.backward(10)
#
# def rot_left():
#     tim.left(10)
#
# def rot_right():
#     tim.right(10)
#
# def clear():
#     tim.penup()
#     tim.clear()
#     tim.home()
#     tim.pendown()
#
#
# screen.listen()
# screen.onkey(key="w", fun=move_forward)
# #or screen.onkey(move_forward, "w")
# screen.onkey(key="s", fun=move_back)
# screen.onkey(key="a", fun=rot_left)
# screen.onkey(key="d", fun=rot_right)
# screen.onkey(key="c", fun=clear)

# screen.exitonclick()

#when using a function as an argument, i.e. move_forward(), being passed into another function,
#we dont add parenthesis at the end

#function being used as an input -> function that can work with other functions, AKA higher
#order functions

#for using methods that we havent created ourselves, better to use keyword > positional
#arguments, i.e. my_function(c=3, b=2, a=1) > my_function(1,2,3)

#objects created from the same classes are separate instances -> function indept of each other
#diff objects from the same class, i.e. timmy and tommy turtle objects, can have diff
#attributes and diff methods, AKA state of timmy color attribute is green, and tommy is purple