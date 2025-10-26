import turtle

screen = turtle.Screen()

screen.bgcolor("blue")

screen.setup(500,600)
polygon = turtle.Turtle()


sides = 50
length = 6
angle = 360/sides
for i in range(sides):
    polygon.forward(length)
    polygon.right(angle)

turtle.done()

