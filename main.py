import time
import os

from character import Character, Hero, Enemy

import weapons

c1 = Hero(name= "Kris", health= 100, weapon= weapons.iron_sword)
c2 = Hero(name= "Danny", health= 100, weapon= weapons.fists)




def main():





    
    while ((c1.health >= 0) and (c2.health >= 0)):

        c1.attack(c2)
        print(f"{c1.name} attacked {c2.name} for {c1.weapon.damage}: {c2.name} now has {c2.health} HP")
        time.sleep(.3)

        c2.attack(c1)
        print(f"{c2.name} attacked {c1.name} for {c2.weapon.damage}: {c1.name} now has {c1.health} HP")
        time.sleep(.3)

        # if c1.health or c2.health < 0:
        #     print("breaking")
        #     break
        # else:
        #     pass



main()