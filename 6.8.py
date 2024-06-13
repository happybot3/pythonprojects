from turtle import*
screensize(10000, 10000)
tracer(0)
lt(90)
k = 10

for i in range(9):
    fd(15*k)
    rt(90)
    fd(k*25)
    rt(90)
up()
fd(-10)
rt(90)
down()
for i in range(8):
    fd(15*k)
    lt(90)
    fd(k*25)
    lt(90)
up()
fd(6*k)
lt(90)
down()
for i in range(7):
    fd(15*k)
    rt(90)
    fd(k*25)
    rt(90)
up()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x*k, y*k)
        dot(4, 'blue')

update()
exitonclick()