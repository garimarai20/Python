from turtle import *
speed('fastest')
bgcolor('blue')
pencolor('white')
penup()
setpos(-180,200)
pendown()
for i in range(200,0,-3):
    forward(i)
    left(90)
    pencolor('white')

penup()
setpos(200,-200)
pendown()
for i in range(200,0,-3):
    forward(i)
    left(90)
    pencolor('white')

penup()
setpos(-200,-200)
pendown()
for i in range(200,0,-3):
    forward(i)
    left(90)
    pencolor('white')

penup()
setpos(200,200)
pendown()
for i in range(200,0,-3):
    forward(i)
    left(90)
    pencolor('white')
mainloop()