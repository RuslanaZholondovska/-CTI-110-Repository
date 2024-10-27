import turtle          
win = turtle.Screen()  
t = turtle.Turtle()


#1 display option given in turtle8_polygon
#2 square
#3 reposition
#4 triangle

# 1
t.pensize(4)            # increase pensize (takes integer)
t.pencolor("red")     # set pencolor (takes string)
t.shape("turtle")

#square
for _ in range(4):
    t.forward(80)  
    t.right(90)
#reposition    
t.penup()
t.left(90)
t.forward(10)
t.pendown()
#triangle
for _ in range(3):
    t.forward(80)  
    t.right(120)     
