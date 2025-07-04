
import turtle
import time
import random

delay = 0.1

score = 0

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("grey")
wn.setup(width=600, height=600)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(50,50)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

def speed_up():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 50)
        wn.bgcolor("blue")
        head.color("green")

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 50)
        wn.bgcolor("blue")
        head.color("green")

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 50)
        wn.bgcolor("blue")
        head.color("green")

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 50)
        wn.bgcolor("blue")
        head.color("green")
        

def go_up():
    if head.direction != "down":
        head.direction = "up"
        wn.bgcolor("grey")
        head.color("white")

def go_down():
    if head.direction != "up":
        head.direction = "down"
        wn.bgcolor("grey")
        head.color("white")

def go_left():
    if head.direction != "right":
        head.direction = "left"
        wn.bgcolor("grey")
        head.color("white")

def go_right():
    if head.direction != "left":
        head.direction = "right"
        wn.bgcolor("grey")
        head.color("white")

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 5)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 5)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 5)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 5)
        
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
wn.onkeypress(speed_up, "x")

while True:
    wn.update()

    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        for segment in segments:
            segment.goto(1000, 1000)
        
        segments.clear()

    if head.distance(food) < 20:

        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()    

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(x,y)
            head.direction = "stop"
        
            for segment in segments:
                segment.goto(1000, 1000)
        
            segments.clear()

    time.sleep(delay)
    
wn.mainloop()
