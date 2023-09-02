import classtest as cl

cl.player.name = input("What is your name? ")
print(f"Hi {cl.player.name}!")

small_potion = cl.potion('Small Potion', 10)
large_potion = cl.potion('Large Potion', 20)

print(f'You find a {cl.small_potion.name}!')
cl.inv[small_potion.name] = 1

print(f'You find a {cl.large_potion.name}!')
cl.inv[large_potion.name] = 1

cl.player.print_inv(cl.inv)

print('Health: ' + str(cl.player.current_hp) + '/' + str(cl.player.maxhp))
print(f'{cl.player.name} takes 20 damage!')
cl.player.current_hp = cl.player.current_hp - 20
print('Health: ' + str(cl.player.current_hp) + '/' + str(cl.player.maxhp))


print('Before Healing: ' + str(cl.player.current_hp))

cl.player.print_inv((cl.inv))
cl.player.use_potion(cl.small_potion)
print('After Healing: ' + str(cl.player.current_hp))
cl.player.print_inv((cl.inv))
cl.player.use_potion(cl.large_potion)
print('After Large Healing: ' + str(cl.player.current_hp))
cl.player.print_inv((cl.inv))

print("Found magic ring")
cl.player.maxhp += 20
print(cl.player.maxhp)