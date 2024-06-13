from turtle import *
screensize(100000, 100000)
tracer(0)
lt(90)
k = 45

for i in range(10):
    fd(10*k)
    rt(60)
    fd(10*k)
    rt(120)

up()
for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x*k, y*k)
        dot(3, 'blue')

exitonclick()
update()