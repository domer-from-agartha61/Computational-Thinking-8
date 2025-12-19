Kai_points = 0
Zane_points = 0
Cole_points = 0
Lloyd_points = 0
Jay_points = 0

answer1 = input("Do you like A red B white C black D green E blue")
if answer1 == "A" or answer1 == "a":
    Kai_points += 1
elif answer1 == "B" or answer1 == "b":
    Zane_points += 1
elif answer1== "C" or answer1 == "b":
    Cole_points += 1
elif answer1 == "D" or answer1 == "d":
    Lloyd_points += 12
elif answer1 == "E" or answer1 == "e":
    Jay_points += 1
answer2 = input("Do you like A fire B ice C earth D green E lighting")
if answer2 == "A" or answer2 == "a":
    Kai_points += 1
elif answer2 == "B" or answer2 == "b":
    Zane_points += 1
elif answer2== "C" or answer2 == "b":
    Cole_points += 1
elif answer2 == "D" or answer2 == "d":
    Lloyd_points += 12
elif answer2 == "E" or answer2 == "e":
    Jay_points += 1
answer3 = input("Do you like A season 7 B season 4 C season 5 D season 1 E season 6")
if answer3 == "A" or answer3 == "a":
    Kai_points += 1
elif answer3 == "B" or answer3 == "b":
    Zane_points += 1
elif answer3== "C" or answer3 == "b":
    Cole_points += 1
elif answer3 == "D" or answer3 == "d":
    Lloyd_points += 12
elif answer3 == "E" or answer3 == "e":
    Jay_points += 1
answer4 = input("Do you like A katana B shurikens C sythe D short sword E nunchucks")
if answer4 == "A" or answer4 == "a":
    Kai_points += 1
elif answer4 == "B" or answer4 == "b":
    Zane_points += 1
elif answer4== "C" or answer4 == "b":
    Cole_points += 1
elif answer4 == "D" or answer4 == "d":
    Lloyd_points += 12
elif answer4 == "E" or answer4 == "e":
    Jay_points += 1
answer5 = input("Do you like A acronix B master chen C morro D lord garmadon E nadakhan")
if answer5 == "A" or answer5 == "a":
    Kai_points += 1
elif answer5 == "B" or answer5 == "b":
    Zane_points += 1
elif answer5== "C" or answer5 == "b":
    Cole_points += 1
elif answer5 == "D" or answer5 == "d":
    Lloyd_points += 12
elif answer5 == "E" or answer5 == "e":
    Jay_points += 1
if Kai_points >= Zane_points >= Cole_points >= Lloyd_points >= Jay_points:
    print("your favorite ninja is Kai ")
if Zane_points >= Kai_points >= Cole_points >= Lloyd_points >= Jay_points:
    print("your favorite ninja is Zane")
if Cole_points >= Zane_points >= Kai_points >= Lloyd_points >= Jay_points:
    print("your favorite ninja is Cole")
if Lloyd_points >= Zane_points >= Cole_points >= Kai_points >= Jay_points:
    print("your favorite ninja is Lloyd")
if Jay_points >= Zane_points >= Cole_points >= Lloyd_points >= Kai_points:
    print(" your favorite ninja is Jay")