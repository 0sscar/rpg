from action import Weapons, Sword, Bow, Axe


class Heros: 

    def __init__(self, name:str, advantage:int, weapon: int):
        self.name = name 
        self.advantage = advantage 
        self.weapon = weapon 
    def advanteges(self): 

        if self.name == "Human" and self.weapon == Sword: 
            self.weapon.damage = 12  
       
        elif self.name =="Elf" and self.weapon == Bow: 
             self.weapon.damage = 15
        
        elif self.name =="anao" and self.weapon == Axe: 
            self.weapon.damage = 23 

