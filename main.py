import random
import os
import sys

# Global Variables
sword_pos = ""
skellie_pos = ""
tim_pos = ""
name = ""
sword_found = False
msg = ' '

## Functions

#Intro
def intro():
    f = open('skellie.txt', 'r')
    file_content = f.read()
    f.close()
    print(REDBLINK + file_content + TERMCOLOR)
    ranpos()
    input("Press any key to start")

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
    while again != "y" or "n":
        again = input("Would you like to play again (y/n)? ")
        if again == "y":
            start()
        elif again == "n":
            quit()
        else:
            print("Pick y or n")
            continue

# Skeleton
def skellie():
    print(name +" sees the mighty Skellie!")
    again = ""
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
    again = ""
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

## Map
room = {
    'Bedroom' : {'N' : 'Corridor One', 'text' : msg[0]},
    'Living Room' : {'E' : 'Corridor One', 'text' : msg[1], 'id' : 1},
    'Bathroom' : {'W' : 'Corridor One', 'text' : msg[2], 'id' : 2},
    'Scary Room' : {'E' : 'Corridor Two', 'text' : msg[3], 'id' : 3},
    'Music Room' : { 'W' : 'Corridor Two', 'text' : msg[4], 'id' : 4},
    'TV Room' : {'E' : 'Corridor Three', 'text' : msg[5], 'id' : 5},
    'Genesis Room' : {'W' : 'Corridor Three', 'text' : msg[6], 'id' : 6},
    'Corridor One' : {'W' : 'Living Room', 'E' : 'Bathroom', 'N' : 'Corridor Two', 'S' : 'Bedroom', 'text' : msg[7]},
    'Corridor Two' : {'W' : 'Scary Room', 'E' : 'Music Room', 'N' : 'Corridor Three', 'S' : 'Corridor One', 'text' : msg[8]},
    'Corridor Three' : {'W' : 'TV Room', 'E' : 'Genesis Room', 'S' : 'Corridor Two', 'text' : msg[9]}
}