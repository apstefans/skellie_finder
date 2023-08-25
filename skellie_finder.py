# Modules
import random
import sys
import os

# Global variables
sword_pos = ""
skellie_pos = ""
tim_pos = ""
name = ""

# Clear screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Sword and Skellie position
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

# Sword found?
sword_found = False

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

# Empty
def empty():
    directions = ["e"]
    nav = ""
    print("The room is empty")
    print("There's nothing for " + name + " here. Press e to exit the room")
    while nav not in directions:
        nav = input("Where do you want to go?")
        if nav == "e":
            corridor_one()
        else:
            print("You need to pick where to go.")
            continue

# Rooms and Corridors
def start():
    clear()
    ranpos()
    print("What is your name?")
    global name
    name = input()
    print(name  + " is woken up by a disturbing noise in the middle of the night.")
    print("It's probably those damn skeletons again. Find your sword and kill it!")
    print("There is exit to the (n)orth")
    nav = ""
    directions = ["n"]
    while nav not in directions:
        nav = input("Where do you want to go?")
        if nav == "n":
            corridor_one()
        else:
            print("You need to pick where to go.")
            continue

def corridor_one():
    directions = ["n", "w", "e"]
    print("Corridor 1")
    print(name + " grabs a candle and walks out into the corridor.")
    print(name + " can go (n)orth to walk down the corridor, or either (w)est or (e)ast into the rooms on either side.")
    nav = ""
    while nav not in directions:
        nav = input("Where do you want to go?")
        if nav == "n":
            corridor_two()
        elif nav == "w":
            room_one()
        elif nav == "e":
            room_two()
        else:
            print("You need to pick where to go.")
            continue

def corridor_two():
    directions = ["n", "w", "e", "s"]
    nav = ""
    print("Corridor 2")
    print(name + " continues down the dimly lit corridor. Candle light flickering against the walls.")
    print(name + " can go (n)orth to walk further down the corridor, or (w)est or (e)ast into the rooms on either side.")
    while nav not in directions:
        nav = input("Where do you want to go?")
        if nav == "n":
            corridor_three()
        elif nav == "w":
            room_three()
        elif nav == "e":
            room_four()
        elif nav == "s":
            corridor_one()
        else:
            print("You need to pick where to go.")
            continue
            
def corridor_three():
    directions = [ "w", "e", "s"]
    nav = ""
    print("Corridor 3")
    print(name + " heads even further down the corridor. Are you sure this is a good idea?")
    print(name + " comes to the end of the corridor. You can either go (e)ast or (w)est into the rooms on either side.")
    while nav not in directions:
            nav = input("Where do you want to go?")
            if nav == "w":
                room_five()
            elif nav == "e":
                room_six()
            elif nav == "s":
                corridor_two()
            else:
                print("You need to pick where to go.")
                continue
    
def room_one():
    directions = ["e"]
    nav = ""
    print(name + " enters the room, the warm glow of the fireplace casts eery shawdows all over the room. Those cheeky skellies could be anywhere!")
    if sword_pos == 1: 
        sword()
        while nav not in directions:
            nav = input("Where do you want to go?")
            if nav == "e":
                corridor_one()
            else:
                print("You need to pick where to go.")
                continue
    elif skellie_pos == 1:
        skellie()
    elif tim_pos == 1:
        Tim()
    else:
       empty()
   
def room_two():
    directions = ["e"]
    nav = ""
    print(name + " enters the room, its a bathroom. Damn Skellie left the seat up again.")
    if sword_pos == 2: 
        global sword_found
        sword_found = True
        print(name + " found the sword! Now go get that bastard!")
        print("Press e to exit the room")
        while nav not in directions:
            nav = input("Where do you want to go?")
            if nav == "e":
                corridor_one()
            else:
                print("You need to pick where to go.")
                continue
    elif skellie_pos == 2:
        skellie()
    elif tim_pos == 2:
        Tim()
    else:
        print("The room is empty")
        print("There's nothing for " + name + " here. Press e to exit the room")
        while nav not in directions:
            nav = input("Where do you want to go?")
            if nav == "e":
                corridor_one()
            else:
                print("You need to pick where to go.")
                continue

def room_three():
    directions = ["e"]
    nav = ""
    print("Ahhhh! A bat flies out of the door. " + name + "peaks the head in to see a delapedated room.\nCracks and water trickle down the walls.")
    if sword_pos == 3:
        global sword_found
        sword_found = True
        print(name + " found the sword! Now go get that bastard!")
        print("Press e to exit the room")
        while nav not in directions:
            nav = input("Where do you want to go?")
            if nav == "e":
                corridor_two()
            else:
                print("You need to pick where to go.")
                continue
    elif skellie_pos == 3:
        skellie()
    elif tim_pos == 3:
        Tim()
    else:
        print("The room is empty")
        print("There's nothing for " + name + " here. Press e to exit the room")
        while nav not in directions:
            nav = input("Where do you want to go?")
            if nav == "e":
                corridor_two()
            else:
                print("You need to pick where to go.")
                continue

def room_four():
    nav = ""
    directions = ["e"]
    print("Unos, Dos, Tres, Cuatro! " + name + "enters into the room and see a salsa band working on their montunos.\nThose Skellies do love their salsa!")
    if sword_pos == 4: 
        global sword_found
        sword_found = True
        print(name + " found the sword! Now go get that bastard!")
        print("Press e to exit the room")
        while nav not in directions:
            nav = input("Where do you want to go?")
            if nav == "e":
                corridor_two()
            else:
                print("You need to pick where to go.")
                continue
    elif skellie_pos == 4:
        skellie()
    elif tim_pos == 4:
        Tim()
    else:
        print("The room is empty")
        print("There's nothing for " + name + " here. Press e to exit the room")
        while nav not in directions:
            nav = input("Where do you want to go?")
            if nav == "e":
                corridor_two()
            else:
                print("You need to pick where to go.")
                continue

def room_five():
    nav = ""
    directions = ["e"]
    print(name + "walks into the room to finds Piers Morgan waiting for an interview. Not this time Piers!")
    if sword_pos == 5: 
        global sword_found
        sword_found = True
        print(name + " found the sword! Now go get that bastard!")
        print("Press e to exit the room")
        while nav not in directions:
            nav = input("Where do you want to go?")
            if nav == "e":
                corridor_three()
            else:
                print("You need to pick where to go.")
                continue
    elif skellie_pos == 5:
        skellie()
    elif tim_pos == 5:
        Tim()
    else:
        print("The room is empty")
        print("There's nothing for " + name + " here. Press e to exit the room")
        while nav not in directions:
            nav = input("Where do you want to go?")
            if nav == "e":
                corridor_three()
            else:
                print("You need to pick where to go.")
                continue

def room_six():
    nav = ""
    directions = ["e"]
    print("As " + name +  "walks into the room they see Phil Collins tickling the drum set with a couple of tibias.\n*dodo dodo dodo dodo dun dun! I can feel a skellie in the air tonight!")
    if sword_pos == 6: 
        global sword_found
        sword_found = True
        print(name + " found the sword! Now go get that bastard!")
        print("Press e to exit the room")
        while nav not in directions:
            nav = input("Where do you want to go?")
            if nav == "e":
                corridor_three()
            else:
                print("You need to pick where to go.")
                continue
    elif skellie_pos == 6:
        skellie()
    elif tim_pos == 6:
        Tim()
    else:
        print("The room is empty")
        print("There's nothing for " + name + " here. Press e to exit the room")
        while nav not in directions:
            nav = input("Where do you want to go?")
            if nav == "e":
                corridor_three()
            else:
                print("You need to pick where to go.")
                continue

def quit():
    print("Too scared of Skellie? I don't blame you.")
    from sys import exit
    exit()


if __name__ == "__main__":
    while True:
        clear()
        print("Welcome to Skellie Finder")
        start()