# Ruslana Zholondovska
# 11/2/2024
# P4LAB1B
# Initials


import turtle          
win = turtle.Screen()  
t = turtle.Turtle()


#1 display option given in turtle8_polygon
#2 R
#3 move
#4 Z

# 1
t.pensize(4)           
t.pencolor("red")    
t.shape("turtle")


#2
t.right(90)
t.forward(200)
t.right(180)
t.forward(200)

for _ in range(3):
    t.right(90)
    t.forward(100)

t.left(120)
t.forward(100)

#3
t.penup()
t.left(60)
t.forward(140)
t.left(90)
t.forward(185)
t.pendown()

#4
t.right(90)
t.forward(150)
t.right(135)
t.forward(230)
t.right(45)
t.right(180)
t.forward(150)
