import turtle
color = ""
length = 0
angle = 0
repeat = 0
counter = 0

color = input("What color do you choose? ")
length = float(input("What is the length of the line? "))
angle = float(input("What is the angle? "))
repeat = float(input("How many repetitions? "))

while counter < repeat:
    turtle.color(color)
    turtle.forward(length)
    turtle.right(angle)
    counter = counter+1