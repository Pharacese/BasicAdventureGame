class Enemy:

    def __init__(self, name : str, health : int, damage : int) -> None:
        self.name = name
        self.health = health
        self.damage = damage
         
    def __str__(self) -> str:
        print(f"An {self.health}")

    def attack(self,target):
        target.health -= self.damage 