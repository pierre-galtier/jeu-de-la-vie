class Cell:
    def __init__(self) -> None:
        self.current = False
        self.future = False
        self.neighbors = None

    def get_current(self):
        return self.current

    def set_neighbors(self, neighbors):
        self.neighbors = neighbors
    
    def get_neighbors(self):
        return self.neighbors
    
    def born(self):
        self.future = True
    
    def die(self):
        self.future = False
    
    def bascule(self):
        self.current = self.future
    
    def __str__(self) -> str:
        if self.current:
            return "⚪"
        else:
            return "⚫"
    
    def compute_future(self): 
        alive_neighbours = 0 
 
        for cell in self.get_neighbors(): 
            if cell.get_current(): 
                alive_neighbours += 1 
 
        if (alive_neighbours != 2) and (alive_neighbours != 3) and self.get_current(): 
            self.die() 
        elif (alive_neighbours == 3) and not self.get_current(): 
            self.born() 
        else: 
            self.futur = self.current