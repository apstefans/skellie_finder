class player:
    name = ""
    maxhp = 30
    current_hp = 30

    def print_inv(dct):
        print('In inventory:')
        if dct == {}:
            print('Inventory empty')
        else:
            for item, amount in dct.items():
                print("Inventory: {} x {}".format(item, amount))

    def use_potion(item):
        old_hp = player.current_hp
        new_hp = player.maxhp - old_hp
        player.current_hp += item.heal
        inv[item.name] -= 1
        if inv[item.name] < 1:
            inv.pop(item.name)
        if player.current_hp > player.maxhp:
            player.current_hp = player.maxhp
            print(player.name + ' heals ' + str(new_hp) + ' points!' )
        else:
            print('Player heals ' + str(item.heal) + ' points!' )

class potion:
    def __init__(self, name, heal):
        self.name = name
        self.heal = heal

inv = {}

small_potion = potion('Small Potion', 10)
large_potion = potion('Large Potion', 20)


