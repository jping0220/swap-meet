from swap_meet.item import Item

class Clothing(Item):
    
    def __init__(self,id, fabric = "Unknown", condition = 0):
        super().__init__(condition)
        self.id = id
        self.fabric = fabric
        self.condition = condition
        

    def get_category(self):
        return "Clothing"
    
    
    def __str__(self):
        return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."
    

     # not passing the first test case for Clothing