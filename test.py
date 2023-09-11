import classtest as cl
import time
import sys
import os
import random

GREEN = "\33[1;32m"
GREENBLINK = GREEN + "\33[5;32m"
MAGENTA = "\33[1;35m"
YELLOW = "\33[1;33m"
YELLOWBLINK = YELLOW + "\33[5;33m"
RED = "\33[1;31m"
REDBLINK = RED + "\33[5;31m"
BLUE = "\33[1;34m"
TERMCOLOR = "\33[0m"

# TEST AND DEVELOPMENT FILE FOR VARIOUS FUNCTIONS FOR SKELLIE FINER


#cl.player.name = input("What is your name? ")
#cl.player.name = "arnar"
#print(f"Hi {cl.player.name}!")
#
#small_potion = cl.potion('Small Potion', 10)
#large_potion = cl.potion('Large Potion', 20)
#
#text = cl.player.print_inv((cl.inv))
#print(text)
#
#print(f'You find a {cl.small_potion.name}!')
#if small_potion.name not in cl.inv:
#    cl.inv[small_potion.name] = 1
#else:
#    cl.inv[small_potion.name] += 1
#
#print("Potion added")
#
#print(f'You find a {cl.small_potion.name}!')
#if small_potion.name not in cl.inv:
#    cl.inv[small_potion.name] = 1
#else:
#    cl.inv[small_potion.name] += 1
#
#print("Another potion added")
#
#print(f'You find a {cl.large_potion.name}!')
#cl.inv[large_potion.name] = 1
#
#cl.player.print_inv(cl.inv)
#
#print('Health: ' + str(cl.player.current_hp) + '/' + str(cl.player.maxhp))
#print(f'{cl.player.name} takes 25 damage!')
#cl.player.current_hp = cl.player.current_hp - 25
#print('Health: ' + str(cl.player.current_hp) + '/' + str(cl.player.maxhp))
#
#
#print('Before Healing: ' + str(cl.player.current_hp))
#
#cl.player.print_inv((cl.inv))
#cl.player.use_potion(cl.small_potion)
#print('After Healing: ' + str(cl.player.current_hp))
#cl.player.print_inv((cl.inv))
#cl.player.use_potion(cl.large_potion)
#print('After Large Healing: ' + str(cl.player.current_hp))
#cl.player.print_inv((cl.inv))
#
#print("Found magic ring")
#cl.player.maxhp += 20
#print(cl.player.maxhp)
#
#print("*" * 50)
#
##f = open('skellie.txt', 'r')
##fc = f.read()
##f.close()
##var = "arnar"
##var = var.title()
##text = f"My name is {var} oh yeah\n"
##time.sleep(0.5)
##for letter in fc:
##    sys.stdout.write(letter)
##    sys.stdout.flush()
##    time.sleep(0.001)
#
#mindam = 2
#maxdam = 7
#
## Checking random damage output with a min and max damage
#count=0
#while count < 5:
#    num = random.randint (mindam, maxdam)
#    print(num)
#    count += 1
#print("------------")
#
#
#num = random.randint(1,3)
#print("Num is " + str(num)) 
#while num > 0:
#    print(num)
#    num -= 1


themap = {}

rooms = {
    'Bedroom'     : {'name' : 'Bedroom',      'exits' : None, 'Room Visited' : 'No',
        'Desc'    : "Nice"},
    'Toilet'      : {'name' : 'Toilet',       'exits' : None, 'Room Visited' : 'No',
        'Desc'    : "Nice"},
    'Living Room' : {'name' : 'Living Room',  'exits' : None, 'Room Visited' : 'No',
        'Desc'    : "Nice"},
    'RoomFour'    : {'name' : 'Room Four',    'exits' : None, 'Room Visited' : 'No',
        'Desc'    : "Nice"},
    'RoomFive'    : {'name' : 'Room Five',    'exits' : None, 'Room Visited' : 'No',
        'Desc'    : "Nice"},
    'RoomSix'     : {'name' : 'Room Six',     'exits' : None, 'Room Visited' : 'No',
        'Desc'    : "Nice"},
    'RoomSeven'   : {'name' : 'Room Seven',   'exits' : None, 'Room Visited' : 'No',
        'Desc'    : "Nice"},
    'RoomEight'   : {'name' : 'Room Eight',   'exits' : None, 'Room Visited' : 'No',
        'Desc'    : "Nice"},
    'RoomNine'    : {'name' : 'Room Nine',    'exits' : None, 'Room Visited' : 'No',
        'Desc'    : "Nice"},
    'RoomTen'     : {'name' : 'Room Ten',     'exits' : None, 'Room Visited' : 'No',
        'Desc'    : "Nice"},
    'RoomEleven'  : {'name' : 'Room Eleven',  'exits' : None, 'Room Visited' : 'No',
        'Desc'    : "Nice"},
    'RoomTwelve'  : {'name' : 'Room Twelve',  'exits' : None, 'Room Visited' : 'No',
        'Desc'    : "Nice"},
    'RoomThirteen': {'name' : 'Room Thirteen','exits' : None, 'Room Visited' : 'No',
        'Desc'    : "Nice"},
    'RoomFourteen': {'name' : 'Room Fourteen','exits' : None, 'Room Visited' : 'No',
        'Desc'    : "Nice"},
    'RoomFifteen' : {'name' : 'Room Fifteen', 'exits' : None, 'Room Visited' : 'No',
        'Desc'    : "Nice"},
    'RoomSixteen' : {'name' : 'Room Sixteen', 'exits' : None, 'Room Visited' : 'No',
        'Desc'    : "Nice"},
}

def generate_xy():
    layout = []
    generate_xy.start_location = [random.randint(0,9), random.randint(0,9)]
    layout.append(tuple(generate_xy.start_location[:]))
    loopcount = 0
    xory = 0
    up_or_down = 0
    add_room = generate_xy.start_location
    roomslist = list(rooms.keys())
    while loopcount <= random.randint(10,15):
        #Decide if x or y will be altered
        add_room = list(add_room)
        xory_old = xory
        xory = random.randint(0,1)
        # Decide if x or y will be increased or decreased
        up_or_down_old = up_or_down
        up_or_down = random.randint(-1,1)
        # Make sure it actually goes up or down 1
        while up_or_down == 0:
            up_or_down = random.randint(-1,1)
        # Check if number is out of bounds
        while add_room[xory] + up_or_down > 9 or add_room[xory] + up_or_down < 0:
            xory = random.randint(0,1)
            up_or_down = random.randint(-1,1)
            while up_or_down == 0:
                up_or_down = random.randint(-1,1)
        # The new (x,y)
        add_room[xory] = add_room[xory] + up_or_down
        # Add new room to the list
        add_room = tuple(add_room)
        if add_room not in layout:
            layout.append(tuple(add_room[:]))
        else:
            xory = xory_old
            up_or_down = up_or_down_old
            continue
        loopcount += 1

    # Add starting room
    themap[layout[0]] = rooms['Bedroom']
    bedroom_num = roomslist.index('Bedroom')
    roomslist.pop(bedroom_num)
    layout.pop(0)

    #Generate rest of rooms
    while len(layout) > 0:
        layout_to_add = random.choice(layout)
        layout_index = layout.index(layout_to_add)
        room_to_add = random.choice(roomslist)
        room_index = roomslist.index(room_to_add)
        themap[layout[layout_index]] = rooms[room_to_add]
        layout.pop(layout_index)
        roomslist.pop(room_index)

    # Generating exit (x,y) and applying them to each room
    northlist = []
    southlist = []
    westlist  = []
    eastlist  = []

    i = 0
    while i < len(themap.keys()):
        # North
        north = list(list(themap.keys())[i])
        north[1] = north[1] + 1
        northlist.append(tuple(north))
        # South
        south =  list(list(themap.keys())[i])
        south[1] = south[1] - 1
        southlist.append(tuple(south))
        # East
        east =  list(list(themap.keys())[i])
        east[0] = east[0] + 1
        eastlist.append(tuple(east))
        # West
        west =  list(list(themap.keys())[i])
        west[0] = west[0] - 1
        westlist.append(tuple(west))
        i += 1

    for keys in themap.keys():
        themap[keys]['exits'] = northlist[0], southlist[0], westlist[0], eastlist[0]
        northlist.pop(0)
        southlist.pop(0)
        eastlist.pop(0)
        westlist.pop(0)

# Count how many exits each room has
checkroomlist = list(themap.keys())
countexits = {}
# Iterate through all the map keys
for i in range(0, len(checkroomlist)):
    tmpstore = []
    # Extract the exits for that particular key
    for j in range(0,4):
        test = checkroomlist[i]
        tmplist = (themap[checkroomlist[i]]['exits'][j])
        tmpstore.append(tmplist)
    # Check which exits are part of the map and count them
    for k in range(0,4):
        if tmpstore[k] in checkroomlist:
            if checkroomlist[i] not in countexits:
                countexits[checkroomlist[i]] = 1
            else:
                countexits[checkroomlist[i]] += 1

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_map():
    map_display = ''
    for y in range (0,10):
        listyeah = []
        for x in range (0,10):
            listyeah.append((x,y))
        for k in range (0,10):
            line = ''
            for l in range(0,10):
                if listyeah[l] == current_room:
                    line += GREEN + 'p' + TERMCOLOR  
                elif listyeah[l] in list(themap):
                    if themap[listyeah[l]]['Room Visited'] == 'Yes':
                        line = line + BLUE + 'x' + TERMCOLOR
                    else:
                        line += 'x'     
                else:
                    line += ' '
        if line == ' ' * 10:
            continue
        if map_display == '':
            map_display = '\n' + map_display + line + '\n'
        else:
            map_display = map_display + line + '\n'
    return map_display

# Testing navigation
generate_xy()
current_room = tuple(generate_xy.start_location)
current_room_name = str(themap[current_room]['name'])
room_count = 0
text = themap[current_room]['Desc']

while True:
    clear()
    if themap[current_room]['Room Visited'] == 'No':
        themap[current_room]['Room Visited'] = 'Yes'
        room_count += 1
    print(BLUE + themap[current_room]['name'] + ' ' + str(current_room) + TERMCOLOR)
    print('Rooms Visited/Total Rooms: ' + str(room_count) + "/" + str(len(themap)))
    print(text)
    print(display_map())
    #Find available exits
    exitroomname = ""
    exitlist = []
    for i in range(0, (len(themap[current_room]['exits']))):
        exitname = themap[current_room]['exits'][i]
        try:
            exitlist.append(themap[exitname]['name'])
        except:
            continue
        try:
            exitroomname = exitroomname + " | " + themap[exitname]['name'] + ' ' + (GREEN + str(exitname) + TERMCOLOR if themap[exitname]['Room Visited'] == 'No' else BLUE + str(exitname) + TERMCOLOR)
        except:
            continue

    print('Availabe exits' + exitroomname + " | ")
    #Get input where to go
    user_input = input('Input ').title()
    if user_input == 'Look Map':
        text = display_map()
        continue
    #Find what (x,y) the user input is in
    for i in range(0, len(list(themap))):
        if user_input in themap[list(themap)[i]]['name']:
            if themap[list(themap)[i]]['name'] == user_input:
                if themap[list(themap)[i]]['name'] in exitlist:
                    current_room = list(themap)[i]
                    break
    
    if themap[current_room]['name'] not in exitlist:
        text = 'You cant go there'
    else:
        text = themap[current_room]['Desc']

