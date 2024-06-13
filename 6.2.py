from turtle import *
tracer(0)
k = 30
lt(90)

for i in range(4):
    fd(7*k)
    rt(90)
    fd(8*k)
    rt(90)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*k, y*k)
        dot(4, 'purple')

exitonclick()
update()