# Modules
import random

# Sword and Skellie position
sword_pos = random.randint(1, 6)
skellie_pos = random.randint(1, 6)
while sword_pos == skellie_pos:
    skellie_pos = random.randint(1, 6)

# Sword found?
sword_found = False

# Skeleton
def skellie():
    print(name +" sees the mighty Skellie!")
    if sword_found == True:
        print(name + "thrusts his rusty sword through Skellie")
        print("Skellie lets out a loud cry, and crumbles down into dust.")
        print("You win!")
    else:
        print(name + " doesn't have his sword! His fists are no match against the mighty Skellie.")
        print(name + " has died a gruesome death.")
        print("You lose.")

# Rooms and Corridors

def start():
    print("There is exit to the north (n)")
    nav = ""
    while nav not in directions:
        nav = input("Where do you want to go?")
        if nav == "n":
            corridor_one()
        else:
            print("You need to pick where to go.")

def corridor_one():
    directions = ["n", "w", "e"]
    print("Corridor 1")
    print(name + " grabs his candle and walks out into the corridor.")
    print(name + " can go north (n) to walk down the corridor, or either west (w) or (e)\ninto the rooms on either side.")
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

def corridor_two():
    directions = ["n", "w", "e", "s"]
    nav = ""
    print("Corridor 2")
    print(name + " continues down the dimly lit corridor. Candle light flickering against the walls.")
    print(name + " can go north (n) to walk further down the corridor, or west (w) oe east (e)\ninto the rooms on either side.")
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
            
def corridor_three():
    directions = [ "w", "e", "s"]
    nav = ""
    print("Corridor 3")
    print(name + " heads even further down the corridor. Are you sure this is a good idea?")
    print("You come to the end of the corridor. You can either go east (e) or west (w)\ninto the rooms on either side.")
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
    
def room_one():
    directions = ["e"]
    nav = ""
    print("You enter a the room, the warm glow of the fireplace casts eiery showdows all over the room.\nThose cheeky skellies could be anywhere!")
    if sword_pos == 1: 
        global sword_found
        sword_found = True
        print("You found the sword! Now go get that bastard!")
        while nav not in directions:
            nav = input("Where do you want to go?")
            if nav == "e":
                corridor_one()
            else:
                print("You need to pick where to go.")
    elif skellie_pos == 1:
        skellie()
    else:
        print("The room is empty")
        print("There's nothing for you here. Press e to exit the room")
        while nav not in directions:
            nav = input("Where do you want to go?")
            if nav == "e":
                corridor_one()
            else:
                print("You need to pick where to go.")
    
   
def room_two():
    directions = ["e"]
    nav = ""
    print("You enter the room, its a bathroom. Damn skellie left the seat up again.")
    if sword_pos == 2: 
        global sword_found
        sword_found = True
        print("You found the sword! Now go get that bastard!")
        while nav not in directions:
            nav = input("Where do you want to go?")
            if nav == "e":
                corridor_one()
            else:
                print("You need to pick where to go.")
    elif skellie_pos == 2:
        skellie()
    else:
        print("The room is empty")
        print("There's nothing for you here. Press e to exit the room")
        while nav not in directions:
            nav = input("Where do you want to go?")
            if nav == "e":
                corridor_one()
            else:
                print("You need to pick where to go.")

def room_three():
    directions = ["e"]
    nav = ""
    print("Ahhhh! A bat flies out of the door. You peak your head in to see a delapedated room,\ncracks and water trickle down the walls.")
    if sword_pos == 3:
        global sword_found
        sword_found = True
        print("You found the sword! Now go get that bastard!")
        while nav not in directions:
            nav = input("Where do you want to go?")
            if nav == "e":
                corridor_two()
            else:
                print("You need to pick where to go.")
    elif skellie_pos == 3:
        skellie()
    else:
        print("The room is empty")
        print("There's nothing for you here. Press e to exit the room")
        while nav not in directions:
            nav = input("Where do you want to go?")
            if nav == "e":
                corridor_two()
            else:
                print("You need to pick where to go.")

def room_four():
    nav = ""
    directions = ["e"]
    print("Unos, Dos, Tres, Cuatro! You enter into the room and see a salsa band working on their montunos.\nThose Skellies do love their salsa!")
    if sword_pos == 4: 
        global sword_found
        sword_found = True
        print("You found the sword! Now go get that bastard!")
        while nav not in directions:
            nav = input("Where do you want to go?")
            if nav == "e":
                corridor_two()
            else:
                print("You need to pick where to go.")
    elif skellie_pos == 4:
        skellie()
    else:
        print("The room is empty")
        print("There's nothing for you here. Press e to exit the room")
        while nav not in directions:
            nav = input("Where do you want to go?")
            if nav == "e":
                corridor_two()
            else:
                print("You need to pick where to go.")

def room_five():
    nav = ""
    directions = ["e"]
    print("You walk into the room to find Piers Morgan waiting to interview you. Not this time Piers!")
    if sword_pos == 5: 
        global sword_found
        sword_found = True
        print("You found the sword! Now go get that bastard!")
        while nav not in directions:
            nav = input("Where do you want to go?")
            if nav == "e":
                corridor_three()
            else:
                print("You need to pick where to go.")
    elif skellie_pos == 5:
        skellie()
    else:
        print("The room is empty")
        print("There's nothing for you here. Press e to exit the room")
        while nav not in directions:
            nav = input("Where do you want to go?")
            if nav == "e":
                corridor_three()
            else:
                print("You need to pick where to go.")

def room_six():
    nav = ""
    directions = ["e"]
    print("As you walk into the room you see a Phill Coilns tickling the drum set with a couple of tibias.\n*dodo dodo dodo dodo dun dun! I can feel a skellie in the air tonight!")
    if sword_pos == 6: 
        global sword_found
        sword_found = True
        print("You found the sword! Now go get that bastard!")
        while nav not in directions:
            nav = input("Where do you want to go?")
            if nav == "e":
                corridor_three()
            else:
                print("You need to pick where to go.")
    elif skellie_pos == 6:
        skellie()
    else:
        print("The room is empty")
        print("There's nothing for you here. Press e to exit the room")
        while nav not in directions:
            nav = input("Where do you want to go?")
            if nav == "e":
                corridor_three()
            else:
                print("You need to pick where to go.")

if __name__ == "__main__":
    while True:
        directions = ["n"]
        print("Welcome to Skellie Finder")
        print("What is your name?")
        name = input()
        print(name  + " is woken up by a disturbing noise in the middle of the night.")
        print("It's probably those damn skeletons again. Find your sword and kill it!")
        start()