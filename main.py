import random
import os
import sys

# ANSI Colors
GREEN = "\33[1;32m"
GREENBLINK = GREEN + "\33[5;32m"
MAGENTA = "\33[1;35m"
YELLOW = "\33[1;33m"
YELLOWBLINK = YELLOW + "\33[5;33m"
RED = "\33[1;31m"
REDBLINK = RED + "\33[5;31m"
BLUE = "\33[1;34m"
TERMCOLOR = "\33[0m"

# Global Variables
sword_pos = ""
skellie_pos = ""
tim_pos = ""
sword_found = False
current_room = 'Bedroom'
new_game = True

## Functions

#Intro
def intro():
    f = open('skellie.txt', 'r')
    file_content = f.read()
    f.close()
    print(REDBLINK + file_content + TERMCOLOR)
    ranpos()
    input("\n\t\t\t     Press any key to start")

# Sword and Skellie positions
def ranpos():
    global sword_pos
    sword_pos = random.randint(1, 6)
    global skellie_pos
    skellie_pos = random.randint(1, 6)
    while sword_pos == skellie_pos:
        skellie_pos = random.randint(1, 6)
    global tim_pos
    tim_pos = random.randint(1, 6)
    while sword_pos == tim_pos or skellie_pos == tim_pos:
        tim_pos = random.randint(1, 6)

# Clear screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Play again
def playagain():
    again = ""
    global new_game
    global current_room
    while again != "y" or "n":
        again = input("Would you like to play again (y/n)? ")
        if again == "y":
            new_game = True
            current_room = 'Bedroom'
            break
        elif again == "n":
            clear()
            quit()
        else:
            print("Pick y or n")
            continue

def quit():
    print("Too scared of Skellie? I don't blame you.")
    sys.exit()

# Skeleton
def skellie():
    print(name +" sees the mighty Skellie!")
    if sword_found == True:
        print(name + " thrusts the rusty sword through Skellie!")
        print("Skellie lets out a loud cry, and crumbles down into dust.")
        print("You win!")
        playagain()
    else:
        print(name + " doesn't have the sword! Fists are no match against the mighty Skellie.")
        print(name + " has died a gruesome death.")
        print("You lose.")
        playagain()

# Tim
def Tim():
    print("A mysterious man in just a robe and sunglasses is waiting for you")
    print("Well isn't it a pleasure to see you here. I've been waiting a while... " + name)
    print(name + "'s asshole has been ravaged by Tim.\nYou walk home. Butt cheeks hurting. ")
    playagain()

# Sword
def sword():
    global sword_found
    sword_found = True
    print(name + " found the sword! Now go get that bastard!")
    print("Press e to exit the room")

# Start screen
def start():
    pass

msg = [
    f"Testing0",
    f"Testing1",
    f"Testing2",
    f"Testing3",
    f"Testing4",
    f"Testing5",
    f"Testing6",
    f"Testing7",
    f"Testing8",
    f"Testing9",
]

## Map
room = {
    'Bedroom' : {'N' : 'Corridor One', 'text' : msg[0], 'id' : 0},
    'Living Room' : {'E' : 'Corridor One', 'text' : msg[1], 'id' : 1},
    'Bathroom' : {'W' : 'Corridor One', 'text' : msg[2], 'id' : 2},
    'Scary Room' : {'E' : 'Corridor Two', 'text' : msg[3], 'id' : 3},
    'Music Room' : { 'W' : 'Corridor Two', 'text' : msg[4], 'id' : 4},
    'TV Room' : {'E' : 'Corridor Three', 'text' : msg[5], 'id' : 5},
    'Genesis Room' : {'W' : 'Corridor Three', 'text' : msg[6], 'id' : 6},
    'Corridor One' : {'W' : 'Living Room', 'E' : 'Bathroom', 'N' : 'Corridor Two', 'S' : 'Bedroom', 'text' : msg[7], 'id' : 0},
    'Corridor Two' : {'W' : 'Scary Room', 'E' : 'Music Room', 'N' : 'Corridor Three', 'S' : 'Corridor One', 'text' : msg[8], 'id' : 0},
    'Corridor Three' : {'W' : 'TV Room', 'E' : 'Genesis Room', 'S' : 'Corridor Two', 'text' : msg[9], 'id' : 0}
}
text = room[current_room]['text']

clear()
intro()

while True:
    clear()

    # Display location
    print(RED + current_room + TERMCOLOR)
    print(GREENBLINK + '=' * 20 + TERMCOLOR)    

    # Print message
    if new_game == True:
        ranpos()
        name = input("What is your name? ")
        print(f"{name} is woken up by a disturbing noise in the middle of the night.")
        print("It's probably that damn Skellie again. Find the sword and kill it!")
        print("There is exit to the North")
    else:
        print(text)
    text = room[current_room]['text']

    # Set new game to false
    new_game = False

    # See if Skellie, Sword or Tim are in room
    if skellie_pos == room[current_room]['id']:
        skellie()
        continue
    elif sword_pos == room[current_room]['id']:
        sword()
    elif tim_pos == room[current_room]['id']:
        Tim()
        continue
    elif room[current_room]['id'] > 0:
        print("The room is empty")
        print(f"There's nothing for {name} here.")

    # Change room
    user_input = input("Where do you want to go? ")
    direction = user_input.upper()
    try:
        current_room = room[current_room][direction]
    except:
        text = "You can't go that way"







