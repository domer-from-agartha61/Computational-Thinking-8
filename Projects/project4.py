import turtle, time, random
from utils import *
#my game is a clicker game where you buy mortadella for pizza coin so that you can buy the gabagool man so you can get more pizza coin.

# Section 1 - setup
# TODO - set a background using set_background()
set_background("underwater")
# TODO - create at least two variables and set their starting value. ex: cookies = 0
Mortadella = 0
Gabagool = 0
Pizza_coin = 0
# OPTIONAL: use this invisible alien to say a message
message_sprite = create_sprite("alien", -200,200)
message_sprite.write("Mortadella",font=("Arial", 24, "bold"))
message_sprite.hideturtle()
message_sprite.clear()



# Section 2 - controls
# TODO - define an action. ex: def my_control()
def Mortadella_maker():
    global Pizza_coin ,Mortadella 
    Pizza_coin += 1 
    x = random.randint(-200,200)
    y = random.randint(-200,200)           
    create_sprite("Mortadella.gif")

window.onkeypress(Mortadella_maker, "m")
# When b clicked remove money and replace with tony suprano.
def Gabagool_buyer():
    global Pizza_coin, Gabagool
    if Pizza_coin >= 20:
        Gabagool += 1
        Pizza_coin -= 20
    x = random.randint(-100,100)
    y = random.randint(-100,100)           
    create_sprite("Gabagool.gif")
window.onkeypress(Gabagool_buyer, "b")
   

# TODO - choose a key to do the action. ex: window.onkeypress(my_control, "space")

# TODO - make a second control





# Section 3 - game loop
window.listen()
for i in range(1000000000):
    message_sprite.clear()
    message_sprite.write(f"Pizza coin: {Pizza_coin}", font=("Arial", 24, "bold"))
    
    # TODO - put any automatic actions here


    # OPTIONAL - use the message sprite to say a message
    # message_sprite.clear()
    # message_sprite.write("Hello")

    time.sleep(0.01)
    window.update()