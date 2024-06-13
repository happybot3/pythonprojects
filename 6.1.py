from turtle import *
tracer(0)
lt(90)
k = 40
for i in range(12):
    rt(60)
    fd(1*k)
    rt(60)
    fd(1*k)
    rt(270)
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*k, y*k)
        dot(4, 'pink')
exitonclick()
update()




