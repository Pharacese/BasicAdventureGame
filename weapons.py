class Weapon:
    
    def __init__(self,
                 name: str,
                 weapon_type: str,
                 damage: int,
                 value : int) -> None:
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = value
    

iron_sword = Weapon(name="Iron Sword",
                    weapon_type="Sharp",
                    damage= 5,
                    value= 10)

short_bow = Weapon(name="Short Bow",
                   weapon_type= "Ranged",
                   damage= 4,
                   value= 8)

axe = Weapon(name="Axe",
             weapon_type="Crush",
             damage= 5,
             value= 10)

warhammer = Weapon(name= "Warhammer",
                   weapon_type= "Blunt",
                   damage= 8,
                   value= 12)

fists = Weapon(name= "Fists",
               weapon_type= "Blunt",
               damage= 2,
               value= 1)


        