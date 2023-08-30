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
protection_pos = ""
sword_found = False
protection_found = False
use_protection = ""
tim_found = False
current_room = 'Bedroom'
new_game = True
direction = ""
skellie_name = RED + "Skellie" + TERMCOLOR
tim_name = GREEN + "Tim" + TERMCOLOR

## Functions

#Intro
def intro():
    f = open('skellie.txt', 'r')
    file_content = f.read()
    f.close()
    print(REDBLINK + file_content + TERMCOLOR)
    print(RED + "\t\tFind the sword before you bump into Skellie to win.")
    print("    Navigate with n to go north, s to go south, w to go west and e to go east" + TERMCOLOR)
    ranpos()
    input("\n\t\t\t    Press any key to start")

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
    global protection_pos
    protection_pos = random.randint(1,6)
    while protection_pos == tim_pos or protection_pos == skellie_pos or protection_pos == sword_pos:
        protection_pos = random.randint(1,6)

# Clear screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Play again
def playagain():
    again = ""
    global new_game
    global current_room
    global sword_found
    global protection_found
    global tim_found
    while again != "y" or "n":
        again = input(f"{BLUE}Would you like to play again (y/n)? {TERMCOLOR}")
        if again == "y":
            new_game = True
            current_room = 'Bedroom'
            sword_found = False
            protection_found = False
            tim_found = False
            break
        elif again == "n":
            quit()
        else:
            print(f"{YELLOW}Pick y or n{TERMCOLOR}")
            continue

def quit():
    clear()
    print("Too scared of Skellie? I don't blame you.")
    sys.exit()
        
# Skeleton
def skellie():
    print(f"{name} sees the mighty Skellie!")
    if sword_found == True:
        print(f"{name} thrusts the rusty sword through {skellie_name}!")
        print(f"{skellie_name} lets out a loud cry, and crumbles down into dust.")
        print(f"{BLUE}You win!{TERMCOLOR}")
        playagain()
    else:
        print(f"{name} doesn't have the sword! Fists are no match against the mighty {skellie_name}.")
        print(f"{name} has died a gruesome death.")
        print(f"{RED}You lose.{TERMCOLOR}")
        playagain()

# Tim
def Tim():
    global tim_found
    global use_protection
    global current_room
    global user_input
    global name
    round_two = ""
    if tim_found == False:
        print("A mysterious man in just a robe and sunglasses is waiting for you")
        print(f'"Well isn\'t it a pleasure to see you here. I\'ve been waiting a while... {name}." he says in a deep sultry voice.')
        print(f'"My name is {tim_name}." His powers of sedcution are irresistable. {name} gives in to the temptation.')
        if protection_found == True:
            while use_protection != "y" or "n":
                use_protection = input(f"{BLUE}Would you like to use the protection? {TERMCOLOR}")
                if use_protection == 'y' or 'n':
                    break
                else:
                    print('Pick y or n')
            if use_protection == "y":
                clear()
                print(f"{tim_name} gives {name} the experience of a lifetime. He's gentle, yet firm. {name} is in a state of elevated bliss!")
                name = f'{YELLOW}Sticky {name}{TERMCOLOR}'
                print(f'After 90 minutes of intense lovemaking, {name} takes a deep breath, gets dressed and decides to carry on looking for {skellie_name}')
                tim_found = True
                return
            elif use_protection == "n":
                clear()
                print(f"While distracted, Skellie rushes in and kills {name}. Died with the pants down. How embarrassing!")
                print(f"Next time, USE PROTECTION!")
                print(f"{RED}You lose.{TERMCOLOR}")
                playagain()
            else:
                print(f"{YELLOW}Pick y or n{TERMCOLOR}")
        else:
            print(f"{name} doesn't have any protection! But there is no resisting the amazing charm of {tim_name}.")
            print(f"While distracted, Skellie rushes in and kills {name}. Died with the pants down. How embarrassing!")
            print(f"{RED}You lose.{TERMCOLOR}")
            playagain()
    else:
        print(f'{name} sees {tim_name} sitting smoking a cigarette, recovering from their interaction earlier. A warm feeling rushes through {name}\n"Thanks for earlier {name}" {tim_name} says.')
        while round_two != "y" or "n":
            round_two = input(f'"Would you like another round?" {tim_name} asks ')
            if round_two == "y":
                clear()
                print(f"{tim_name} works his magic on {name}. It gets better and stickier every time!")
                name = f'{YELLOW}Very {name}{TERMCOLOR}'
                return
            elif round_two == "n":
                clear()
                print(f"Although very tempting, {name} declines the offer this time. Skellie won't kill himself")
                return
            else:
                print(f"{YELLOW}Pick y or n{TERMCOLOR}")
                continue

# Sword
def sword():
    global sword_found
    sword_found = True
    print(f"{name} found the sword! Now go get that bastard!")

# Protection
def protection():
    global protection_found
    protection_found = True
    print(f"{name} found protection! This might come in handy.")

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
        name_input = input(BLUE + "What is your name? " + TERMCOLOR)
        name = YELLOW + name_input.title() + TERMCOLOR
        print(f"{name} is woken up by a disturbing noise in the middle of the night.")
        print(f"It's probably that damn {skellie_name} again. Find the sword and kill it!")
        print('-' * 15)
    else:
        print(text)
        print('-' * 15)
        print(f"Tim {tim_pos} Skellie {skellie_pos} sword {sword_pos} protection {protection_pos}")

    # Set new game to false
    new_game = False

    msg = [
        f"{name} is back in the bedroom. Go back out there and find {skellie_name}!",
        f"{name} enters the room, the warm glow of the fireplace casts eery shawdows all over the room. That cheeky {skellie_name} could be anywhere!",
        f"{name} enters the bathroom. Damn {skellie_name} left the seat up again",
        f"Ahhhh! A bat flies out of the door. {name} peaks the head in to see a delapedated room.\nCracks and water trickle down the walls.",
        f"Unos, Dos, Tres, Cuatro! {name} enters the room and sees a salsa band working on their montunos.\nThat {skellie_name} does love salsa!",
        f"{name} walks into the room to finds Piers Morgan waiting for an interview. Not this time Piers!",
        f"As {name} walks into the room they see Phil Collins tickling the drum set with a couple of tibias.\n*dodo dodo dodo dodo dun dun! I can feel a {skellie_name} in the air tonight!",
        f"{name} grabs a candle and walks out into the corridor.",
        f"{name} continues down the dimly lit corridor. Candle light flickering against the walls.",
        f"{name} heads even further down the corridor. Are you sure this is a good idea?",
        ]
    
    # Map
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
    
    # See if Skellie, Sword or Tim are in room
    if skellie_pos == room[current_room]['id']:
        skellie()
        continue
    elif sword_pos == room[current_room]['id']:
        if sword_found == False:
            sword()
        else:
            print(f"{name} has already taken the sword from this room. There's nothing else here.")
    elif tim_pos == room[current_room]['id']:
        Tim()
        if new_game == True:
            continue

    elif protection_pos == room[current_room]['id']:
        if protection_found == False:
            protection()
        else:
            print(f"{name} has already taken the protection from this room. There's nothing else here.")
    elif room[current_room]['id'] > 0:
        print("The room is empty")
        print(f"There's nothing for {name} here.")

    # Change room
    user_input = input(BLUE + "Where to? " + TERMCOLOR)
    direction = user_input.upper()
    
    if direction == "EXIT":
        quit()
    else:
        try:
            current_room = room[current_room][direction]
            text = room[current_room]['text']
        except:
            text = "You can't go that way"