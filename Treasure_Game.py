print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You are at a cross road. Where do you want to go?")
# This is the first player's choice
way = (input("Right or Left? (answer with an r for right or l for left)"))
if way == "l":
    print("Correct way, keep walking on the road!")
    # That's the second player's choice
    print("You've come to a lake. There is an island in the middle of the lake.")
    lake = (input("So what you gonna do? Wait for a boat or swin to the island? (answer with: wait or swin)."))
    if lake == "wait":
        print("You hitchhiked a boat ride and arrived on the island!")
        # Now the final choice
        print("Okay, everything is fine with you, and you’ve made all the right choices so far... now for the final challenge...")
        doors = (input(
            "There is a house with three doors in different colors: Red, Blue, and Yellow. You can only choose one of them. Which one is the right one? (Answer only with: Red, for the red door; Blue, for the blue door; or Yellow, for the yellow door)."))
        if doors == "Red":
            print("Wrong door, you burned to death! The game is over!")
        elif doors == "Blue":
            print("Wrong door, you were eaten by beasts! The game is over!")
        elif doors == "Yellow":
            print("You found the treasure! You win!!! :)")
        else:
            print("Its not even an answer, the game is over!")
    elif lake == "swin":
        print("Unfortunately, you drowned in the lake, and the game is over for you!")
    else:
        print("Unfortunately, you drowned in the lake, and the game is over for you!")
elif way == "r":
    print("Wrong way, the game is over for you!")
else:
    print("Wrong way, the game is over for you!")
