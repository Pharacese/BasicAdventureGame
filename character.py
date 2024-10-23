import weapons


class Character:


    #Also needs strength, intelligence, dexterity, charisma, 
    def __init__(self, name: str,health: int) -> None:
        self.name = name
        self.health = health

    def __str__(self) -> str:
        return f"Fuck you, my health is {self.health}"

    def attack(self,target):
        target.health -= self.weapon.damage 
        print(f"{target.name} recieved {self.weapon.damage} from {self.name}")

class Hero(Character):
    def __init__(self,
                 name: str,
                 health: int,
                 weapon
                 ) -> None:
        super().__init__(name, health)
        self.weapon = weapon 

class Enemy(Character):

    def __init__(self, 
                 name: str, 
                 health: int, 
                 weapon
                 ) -> None:
        super().__init__(name, health)
        self.weapon = weapon


    # def __init__(self, name : str, health : int, damage : int) -> None:
    #     self.name = name
    #     self.health = health
    #     self.damage = damage
         
    # def __str__(self) -> str:
    #     print(f"An {self.name}")

    
    


# class Mage(Character):
#     def 



# if x == 2:
#     class PlayerCharacter(Mage):
        



# class Warrior(Character):
#     def __init__(self, name: str, health: int, damage: int) -> None:
#         super().__init__(name, health, damage)



# class Rou


# class PlayerCharacter()
    

