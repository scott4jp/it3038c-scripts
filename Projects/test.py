# Creating Game for first time
# Snake Game

import turtle
import time
import random

delay = 0.1

#Setup the screen
wn = turtle.Screen()
wn.title('Snake Game by @PythoCoadingProjects')
wn.bgcolor('yellow')
wn.setup(width=600, height=600)
wn.tracer(0)

#snake head
head = turtle.Turtle()
head.speed(0)
head.shape('circle')
head.color('black')
head.penup()
head.goto(0,0)
head.direction = "stop"

#khaana saanp kaa khaana
food = turtle.Turtle()
food.speed(0)
food.shape('square')
food.color('red')
food.penup()
food.goto(0,100)

segments = []



#functions
def go_up():
    head.direction = "up"
def go_down():
    head.direction = "down"

def go_left():
    head.direction = "left"

def go_right():
    head.direction = "right"



def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)    
    
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)    

#keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")


#Main game loop
while True:
    wn.update()

    # check with a collision with the food
    if head.distance(food) < 20:
        #random sopt snake food
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('blue')
        new_segment.penup()
        segments.append(new_segment)

    #Move the segments in reverse order
for index in range(len(segments)-1, 0, -1):
    x = segments[index-1].xcor()
    y = segments[index-1].ycor()      
    segments[index].goto(x, y)  

#Move where the head is
if len(segments) > 0:
    x = head.xcor()
    y = head.ycor()
    segments[0].goto(x,y)     

   
        

    move()

    time.sleep(delay)

wn.mainloop()