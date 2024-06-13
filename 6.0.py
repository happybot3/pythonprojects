from turtle import *
tracer(0)
k = 30
lt(90)
for i in range(5):
    fd(9*k)
    rt(120)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*k, y*k)
        dot(4, 'blue')
exitonclick()    
update()