from action import Weapons, Sword, Bow, Axe
from hero import Heros 


class Player: 

    def __init__(self, health: int, name: str, weapon: Weapons ):
        self.name = name 
        self.health = health            
        self.weapon = weapon
    def atack (self, target): 
        target.health -= self.weapon.damage 
        target.health = max(target.health, 0) 
        print(f"{self.name} use {self.weapon.name} dealing {self.weapon.name}")        
    def get_health(self):        
    
        return(self.health)

print("Who is gonna be your hero?")

Hero = Player(health =100, name = "anao",  weapon= Axe ) 
Villan = Player(health=100, name= "Villan", weapon=Sword) 


while Hero.health > 0 and Villan.health >0: 
    Hero.atack(Villan) 
    Villan.atack(Hero) 
    
    print(f"Name: {Hero.name} HP:{Hero.health}") 
    print(f"Name: {Villan.name} HP:{Villan.health}") 
    
    input() 
else: 
    print("Game Over") 