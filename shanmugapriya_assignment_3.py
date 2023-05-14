import turtle

# Define a function to draw a custom shape using turtle
def draw_custom_shape():
    turtle.speed(0)
    for i in range(5):
        turtle.forward(50)
        turtle.right(144)
    turtle.hideturtle()

# Define a function to draw any shape using turtle
def draw_shape(shape):
    turtle.clear()
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    a = 0
    b = 0
    if shape == "circle":
        turtle.circle(50)
    elif shape == "square":
        for i in range(4):
            turtle.forward(100)
            turtle.right(90)
    elif shape == "triangle":
        for i in range(3):
            turtle.forward(100)
            turtle.right(120)
    elif shape == "rectangle":
        for i in range(2):
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(50)
            turtle.right(90)
    elif shape == "corona":
        turtle.color("red")
        turtle.goto(10, 150)
        for i in range(210):
            turtle.speed(40)
            turtle.forward(a)
            turtle.right(b)
           
            a += 3
            b += 1
    else:
        print("Invalid shape.")

# Ask the user for the shape they want to draw
shape = ""
while shape != "q":
    shape = input("Enter the shape you want to draw (circle, rectangle, corona, square, or triangle), or q to quit: ")
    if shape != "q":
        draw_shape(shape)

turtle.done()
