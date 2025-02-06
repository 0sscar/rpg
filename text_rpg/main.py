class Player: 

    def __init__(self, helth = int, name= str, damage= int ):  
        self.name = name 
        self.helth = helth
        #self.max_hp = max_hp 
          
        self.damage = damage 

    def atack (self, target): 
        target.helth -= self.damage 
        target.helth = max(target.helth, 0) 

    def get_helth(self):        
    
        return(self.helth)

Hero = Player(helth =100, name = "Hero", damage=35 ) 
Villan = Player(helth=100, name= "Villan", damage=15) 


while Hero.helth > 0 and Villan.helth >0: 
    Hero.atack(Villan) 
    Villan.atack(Hero) 

    print(f"Name: {Hero.name} HP:{Hero.helth}") 
    print(f"Name: {Villan.name} HP:{Villan.helth}") 
    
    input() 
else: 
    print("Game Over")