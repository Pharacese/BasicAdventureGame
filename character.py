class Character:

    def __init__(self, name: str,health: int,damage: int) -> None:
        self.name = name
        self.health = health
        self.damage = damage

    def __str__(self) -> str:
        return f"Fuck you, my health is {self.health}"

    def attack(self,target):
        target.health -= self.damage
        print(f"{target.name} recieved {self.damage} from {self.name}")

    