import turtle  

# Flytta pennan till en specifik koordinat utan att rita
def jump(t, x, y):
    t.penup()      
    t.goto(x, y)   
    t.pendown()    

# Skapa en ny padda på en specifik position och sedan få den att återvända till origo
def make_turtle(x, y):
    t = turtle.Turtle()
    jump(t, x, y)        
    return t   

# funktion för stjärnorna
def pentagram(x, y, side):
    t = make_turtle(x, y)
    t.fillcolor('gold')
    t.hideturtle()
    t.begin_fill()
    t.speed(0)             
    t.hideturtle()
    t.setheading(252)
    for i in range(5):
        t.forward(side)
        t.left(144) 
    t.end_fill()        

# 2 rader x 5 stjärnor med startkoordinat (-220, 650)
y = 650
for z in range(2):
    y = 250
    x = -220

    for i in range(5):
        pentagram(x, y, 100)
        x = x + 100
# Funktion för rektangeln
def rectangle(x, y, w, h, color):
    t = make_turtle(x, y)  
    t.speed(0)
    t.hideturtle()         
    t.fillcolor(color)
    t.begin_fill()         
    for dist in [w, h, w, h]:
        t.forward(dist)
        t.left(90)
    t.end_fill()


# Funktion för att skapa flaggan
def tricolore(x, y, h):
    p = ['green', 'white', 'red', ]
    w = h/2  # Förhållande mellan höjd och bredd
    a = 0
    for color in p:
        rectangle(x + a, y, w, h, color)
        a = a + w

tricolore(-150, -100, 200)

turtle.done()  