import turtle
import random 

# Function to move the turtle to a specific position (x, y)
def jump(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# Funktion för att rita rektangel
def rectangle(t, x, y, w, h, color):
    jump(t, x, y)
    t.fillcolor(color)
    t.begin_fill()
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
    t.end_fill()
    t.fillcolor('')

# Funktion för slumpmässig förflyttning
def move_random(t):
    t.left(random.randint(-45, 45))         # Turn left or right randomly
    t.forward(random.randint(0, 25))        # Move forward by a random distance
    if abs(t.xcor()) > 250 or abs(t.ycor()) > 250:
        t.setheading(t.towards(0, 0))

# Function to create a turtle with a specific color
def create_turtle(color, low=-100, high=100):
    t = turtle.Turtle()
    t.shape('turtle')
    jump(t, random.randint(low, high), random.randint(low, high))  # Place at random position
    t.setheading(random.randint(0, 359))      # Set a random initial direction
    t.speed(0)
    t.color(color)
    return t

#Skapa bakgrunden
t = turtle.Turtle()
t.speed(0)
rectangle(t, -250, -250, 500, 500, 'lightblue')
t.hideturtle() 

#Skapa 2 paddor
turtles = []
turtles.append(create_turtle('red'))
turtles.append(create_turtle('green'))

c = 0
for i in range(500):
    for t in turtles:
        move_random(t)
        if turtles[0].distance(turtles[1]) < 50:
            turtles[0].write('close')
            c = c + 1  # Räknar hur många close
print(c, 'close')

turtle.done()