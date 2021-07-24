import random
import turtle
import time
from random import randint

wd = turtle.Screen()
wd.setup(height=580, width=580) #borders are at 290
wd.bgcolor("yellow")
wd.tracer(0)

# Snake Head
snake_head = turtle.Turtle()
snake_head.shape("square")
snake_head.color("black")
snake_head.penup()
snake_head.direction = "stop"

# Food
food = turtle.Turtle()
food.penup()
food.color("red")
food.shape("circle")
food.goto(60, 20)

# Texts
texts = turtle.Turtle()
texts.penup()
texts.color("black")
texts.speed(0)
texts.hideturtle()
texts.goto(0, 200)
texts.write("Score: 0   Best: 0", align="center", font=("Courier", 18, "normal"))

# Segments (snake body)
segments = []
score = 0

# Snake Functions
def stop():
    snake_head.direction = "stop"
    score = 0
    texts.clear()
    texts.write("Score: 0   Best: 0", align="center", font=("Courier", 18, "normal"))
    
def goUp():
    if snake_head.direction != "down":
        snake_head.direction = "up"

def goDown():
    if snake_head.direction != "up":
        snake_head.direction = "down"

def goLeft():
    if snake_head.direction != "right":
        snake_head.direction = "left"

def goRight():
    if snake_head.direction != "left":
        snake_head.direction = "right"

def move():
    if snake_head.direction == "up":
        y = snake_head.ycor()
        snake_head.sety(y + 20)
        time.sleep(0.1)
    if snake_head.direction == "down":
        y = snake_head.ycor()
        snake_head.sety(y - 20)
        time.sleep(0.1)
    if snake_head.direction == "right":
        x = snake_head.xcor()
        snake_head.setx(x + 20)
        time.sleep(0.1)
    if snake_head.direction == "left":
        x = snake_head.xcor()
        snake_head.setx(x - 20)
        time.sleep(0.1)

# Keyboard Binding
wd.listen()
wd.onkeypress(goUp, "Up")
wd.onkeypress(goDown, "Down")
wd.onkeypress(goLeft, "Left")
wd.onkeypress(goRight, "Right")

# Game Main Loop
while True:
    wd.update()
    move()


    # Border
    if snake_head.ycor() >= 290:
        snake_head.sety(0)
        snake_head.setx(0)
        stop()
        
        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()
    if snake_head.ycor() <= -290:
        snake_head.sety(0)
        snake_head.setx(0)
        stop()

        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()


    if snake_head.xcor() >= 290:
        snake_head.setx(0)
        snake_head.sety(0)
        stop()
        
        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()

    if snake_head.xcor() <= -290:
        snake_head.setx(0)
        snake_head.sety(0)
        stop()
        
        
        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()
    # Check if Snake eat food
    if snake_head.ycor() == food.ycor() and snake_head.xcor() == food.xcor():
        y = random.randint(-13, 13) * 20
        x = random.randint(-13, 13) * 20
        print(y, x)
        food.goto(y, x) 
        score += 1
        texts.clear()
        texts.write("Score: {}   Best: 0".format(score), align="center", font=("Courier", 18, "normal"))

        # Snake Body
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.penup()
        new_segment.shape("square")
        new_segment.color("grey")
        segments.append(new_segment)
        
    # move last segment location to 2nd last and 2d last to 3d last and so on
    for index in range(len(segments)-1, 0, -1): #counts from end to first
        y = segments[index - 1].ycor()
        x = segments[index - 1].xcor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        y = snake_head.ycor()
        x = snake_head.xcor()
        segments[0].goto(x, y)
