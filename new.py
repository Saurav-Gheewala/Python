from turtle import *

colors = ["red", "cyan", "green", "yellow", "white", "orange"]
colors1 = ["red", "white"]
bgcolor("black")
speed(0)
for x in range(200):
    pencolor(colors[x % 6])
    width((x/200)+1)
    forward(x)
    left(59)
for y in range(180):
    pencolor(colors1[y % 2])
    width((y/47)+7)
    backward(y)
    right(78)
for y in range(180):
    pencolor(colors1[y % 2])
    width((y/47)+7)
    backward(y)
    right(88)
for y in range(180):
    pencolor(colors1[y % 2])
    width((y/47)+7)
    backward(y)
    right(98)
for y in range(180):
    pencolor(colors1[y % 2])
    width((y/47)+7)
    backward(y)
    right(108)
hideturtle()

done()
