# Rooms for Skellie Finder
class Rooms:
    def __init__(self, name, desc, exits):
        self.name = name
        self.desc = desc
        self.exits = exits

class LivingRoom(Rooms)
    


#world = {}
#world['Bedroom'] = Rooms(
#    'Bedroom',
#    'A very comfy bed',
#    {'N' : 'Living Room', 'S' : 'Sex Dungeoun'}
#)
#world['Living Room'] = Rooms(
#    'Living Room',
#    'Warm room with a fireplace',
#    {'S' : 'Bedroom', 'W' : 'Kitchen'}
#)

#current_room = world['Bedroom']
#    
#print(current_room.name)
#print(current_room.desc)
#where = input('Where do you want to go?').upper()
#current_room = world[current_room.exits[where]]
#print(current_room.name)
#print(current_room.desc)