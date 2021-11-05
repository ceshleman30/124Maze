# import statements
import turtle
import random 

# maze configuration
wall_length = 60
wall_number = 30
wall_color = "black"
path_width = 20
center_walls = 6

#initilize turtle
wall_builder = turtle.Turtle()
wall_builder.speed("fastest")
wall_builder.hideturtle()

player = turtle.Turtle()
player.penup()
player.goto(10,10)
player.pendown()
player.shape("turtle")
player.color("blue")
player.pencolor("blue")

# maze functions
def make_walls(): #this is going to make spiral of walls
    global wall_length
    global center_walls
    for i in range(wall_number):
        if(i<center_walls): #makes middle
            wall_builder.forward(wall_length)
            wall_builder.left(90)
            wall_length += path_width

        else:
            random_door = random.randint(1,2)
            random_wall1 = random.randint(10,wall_length/4)
            random_wall2 = random.randint(10, wall_length/4)
            if (random_door == 1):
                #section 1
                wall_builder.forward(random_wall1)
                #section 2
                make_door()
                #section 3
                wall_builder.forward(random_wall2)
                #section 4
                make_barrier()
                #section 5
                wall_builder.forward(wall_length - random_wall1 - path_width - random_wall2)
                wall_builder.left(90)
                wall_length += path_width
            else:
                #section 1
                wall_builder.forward(random_wall1)
                #section 2
                make_barrier()
                #section 3
                wall_builder.forward(random_wall2)
                #section 4
                make_door()
                #section 5
                wall_builder.forward(wall_length - random_wall1 - path_width - random_wall2)
                wall_builder.left(90)
                wall_length += path_width


def make_door():
    wall_builder.penup()
    wall_builder.forward(path_width)
    wall_builder.pendown()

def make_barrier():
    wall_builder.left(90) 
    wall_builder.forward(path_width * 2)
    wall_builder.back(path_width * 2)
    wall_builder.right(90)

def move():
    player.forward(5)

def Left():
    player.setheading(180)
    move()

def Right():
    player.setheading(0)
    move()

def Up():
    player.setheading(90)
    move()

def Down():
    player.setheading(270)
    move()

# events
make_walls()

wn = turtle.Screen()

wn.listen()
wn.onkeypress(Left,"a")
wn.onkeypress(Up,"w")
wn.onkeypress(Right,"d")
wn.onkeypress(Down,"s")

wn.mainloop()