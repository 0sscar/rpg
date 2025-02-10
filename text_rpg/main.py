from action import Weapons, Sword, Bow, Axe, knife
from hero import Heroes 
from helth_bar import HealthBar

class Player: 

    def __init__(self, health: int, name: str, weapon: Weapons ):
        self.name = name 
        self.health = health            
        self.weapon = weapon
        self.health_max = health 

    def atack (self, target): 
        target.health -= self.weapon.damage 
        target.health = max(target.health, 0) 
        print(f"{self.name} use {self.weapon.name} dealing {self.weapon.damage} damage") 
                
    def get_health(self):        
    
        return(self.health)


def Hero_choose(): 
    print("Who is gonna be your hero?") 
    print("[1] for humanan \n[2] for Elf \n[3] for Dwarves")
    choice= input("enter the number of your hero: ")  

    if choice == "1": 
        return "Human"  
    elif choice == "2":  
        return "Elf" 
    elif choice == "3":  
        return "Dwarves"   
    
def Weapon_choose(): 
    print("\nNow choose your weapon:\n")
    print("[1] for Sword \n[2] for Bow \n[3] for Axe") 
    choice = input("enter the number of your weapon: ")

    if choice == "1": 
        return Sword 
    elif choice == "2": 
        return Bow 
    elif choice == "3": 
        return Axe 
    


Hero_type = Hero_choose()         
Weapon_type = Weapon_choose() 

hero = Heroes(name=Hero_type, weapon=Weapon_type)

Hero = Player(health =100, name = Hero_type,  weapon= hero.weapon) 
Villan = Player(health=100, name= "Villan", weapon=knife) 

hero_health_bar = HealthBar(Hero, color="green")  
villan_health_bar = HealthBar(Villan, color="red")  

while Hero.health > 0 and Villan.health >0: 
    Hero.atack(Villan) 
    Villan.atack(Hero) 
    
    print(f"Name: {Hero.name} HP:{Hero.health}") 
    print(f"Name: {Villan.name} HP:{Villan.health}") 

    hero_health_bar.update()
    villan_health_bar.update()
    hero_health_bar.draw()
    villan_health_bar.draw()
    
    input() 
else: 
    print("Game Over") 