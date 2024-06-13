from turtle import *
tracer(0)
screensize(10000, 10000)
lt(90)
k = 40

for i in range(10):
    fd(5*k)
    rt(60)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*k, y*k)
        dot(4, 'blue')

update()
exitonclick()