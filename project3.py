import turtle, time, random
from utils import *

# Section 1 - Variables
# TODO - add starting values for all the variables
x1 = -100
y1 = 50
x2 = -100
y2 = 100
x3 = -100
y3 = -50
x4 = -100
y4 = -100


# Section 2 - Setup
# # TODO - use your own background, and set your four turtles to images of your choice
set_background("castle")
Eb = create_sprite("Electro_brainz.gif",x1,y1)
As = create_sprite("All_Star.gif",x2,y2)
tv = create_sprite("Tv_zombie.gif",x3,y3)
t4 = create_sprite("basketball",x4,y4)


# Section 3 - Racing
# repeats 31 times
# tv always wins because it goes 4/5 of a square each loop and the others move less
for i in range(31):
    x1 += 4
    x2 += 3
    x3 += 8
    x4 += 5

    Eb.goto(x1, y1)
    As.goto(x2, y2)
    tv.goto(x3, y3)
    t4.goto(x4, y4)

    window.update()
    time.sleep(0.1)


 #Section 4 - Winner
 
 
if Eb >= tv and Eb >= As and Eb >= x4:
    print("player 1 wins!")
elif As >= Eb and As >= tv and As >= x4:
    print("player 2 wins!")
elif tv >= Eb and tv >= As and tv >= x4:
    print("player 3 wins")
elif x4 >= Eb and x4 >= tv and x4 >= As:
    print("player 4 wins")
turtle.exitonclick()