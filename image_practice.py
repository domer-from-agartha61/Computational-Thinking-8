# Section 1 - Your code
from utils import *
set_background("summer")

s1 = create_sprite("alien", 34, 14)
s2 = create_sprite("alien", -100, 100)
s2 = create_sprite("alien", -100, -100)
s2 = create_sprite("alien", 100, -100)

message1 = create_sprite("alien",-200,200)
message1.color("purple")
message1.write("MANGOES",font = ("Arial", 40, "normal"))
message1.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()