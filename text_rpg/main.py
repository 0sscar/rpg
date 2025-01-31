class Player: 

    def __init__(self, age):  
        self.age = age 
           
    def get_age (self): 
        return self.age

a = Player(17)  
print (a.get_age())  