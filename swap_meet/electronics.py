from swap_meet.item import Item
class Electronics(Item):
    def __init__(self, id, type = "Unknown", condition =0):
        super().__init__(condition)
        self.id = id
        self.type = type
        self.condintion = condition
        

    
    def get_category(self):
        return "Electronics"
    

    def __str__(self):
        return f"An object of type Electronics with id {self.id}. This is a {self.type} device."
        
 # not passing the first test case for Electronics