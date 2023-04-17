# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

from turtle import *
shape("turtle")
color("green")
speed(5)

bgcolor("lightskyblue")
penup()
goto(0,-300)
pendown()
color("white")
begin_fill()
circle(140)
end_fill()

penup()
goto(0,-80)
pendown()
color("white")
begin_fill()
circle(110)
end_fill()

#hlava
penup()
goto(0,115)
pendown()
color("white")
begin_fill()
circle(80)
end_fill()

#prava ruka
penup()
goto(130,0)
pendown()
color("white")
begin_fill()
circle(55)
end_fill()

#leva ruka
penup()
goto(-130,0)
pendown()
color("white")
begin_fill()
circle(55)
end_fill()





#funkce pro knofliky

def eye():
    color("black")
    begin_fill()
    circle(10, steps=8)
    end_fill()

#oci
x=-30
for i in range(2):
    penup()
    goto(x, 205)
    pendown()
    eye()
    x=x+60

#knofliky

def button():
    color("black")
    begin_fill()
    circle(10, steps=6)
    end_fill()

y=50
for j in range(5):
 penup()
 goto(0,y)
 pendown()
 button()
 y=y-50





#nos

penup()
goto(0,200)
pendown()
color("orange")
begin_fill()
right(20)
forward(60)
left(200)
forward(60)
end_fill()

#pusa

def rmouth():
    color("black")
    begin_fill()
    circle(6, steps=8)
    end_fill()

x=30
y=162
for k in range(2):
 penup()
 goto(x,y)
 pendown()
 rmouth()
 x=x-10
 y=y-10

penup()
goto(5,148)
pendown()
color("black")
begin_fill()
circle(6,steps=8)
end_fill()

def lmouth():
    color("black")
    begin_fill()
    circle(6, steps=8)
    end_fill()

x=-10
y=152
for t in range(2):
 penup()
 goto(x,y)
 pendown()
 lmouth()
 x=x-10
 y=y+10





#klobouk

penup()
goto(0,250)
pendown()
color("blue4")
begin_fill()
right(180)
width(8)
forward(80)
backward(160)
end_fill()

penup()
goto(-60,330)
pendown()
color("blue4")
begin_fill()
right(90)
width(8)
forward(80)
left(90)
forward(120)
left(90)
forward(80)
end_fill()






#koste

penup()
goto(-160,15)
pendown()
right(180)
color("green")
width(6)
begin_fill()
forward(160)
end_fill()

penup()
goto(-160,250)
pendown()
color("green")
width(6)
begin_fill()
forward(155)
end_fill()



def ball():
    color("pink")
    begin_fill()
    circle(12)
    end_fill()

def ball2():
    color("white")
    begin_fill()
    circle(9)
    end_fill()

def centre():
 color("yellow")
 begin_fill()
 circle(10)
 end_fill()

speed(0)

def broom():
    goto(-160, 265)
    centre()
    color("green")
    begin_fill()
    width(4)
    left(10)
    forward(70)
    ball()
    color("green")
    backward(20)
    ball2()
    color("brown")
    backward(30)
    color("yellow")
    backward(20)
    end_fill()

for h in range(29):
    penup()
    right(60)
    goto(-160, 255)
    pendown()
    broom()



#vlocky
from random import randint

def snowflake():
    color("white")
    forward(2)
    backward(4)
    backward(2)
    right(90)
    forward(2)
    backward(4)
    right(90)
    forward(2)
    backward(4)
    right(90)
    forward(2)
    backward(4)


for h in range(1000):
    penup()
    goto(randint(-600, 600), randint(-600, 500))
    pendown()
    snowflake()

penup()
goto(-400,-400)





mainloop()