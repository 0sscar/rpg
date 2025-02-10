from action import Weapons, Sword, Bow, Axe


class Heroes: 

    def __init__(self, name:str, weapon: int):
        self.name = name 
        self.weapon = weapon  
        self.advanteges() 

    def advanteges(self): 

        if self.name == "Human" and self.weapon == Sword: 
            self.weapon.damage = 12  
       
        elif self.name =="Elf" and self.weapon == Bow: 
             self.weapon.damage = 15
        
        elif self.name =="Dwarves" and self.weapon == Axe: 
            self.weapon.damage = 23 

