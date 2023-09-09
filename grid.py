from cell import Cell
import random

class Grid:
    def __init__(self, x) -> None:
        self.x = x
        self.y = x
        self.matrix = [[Cell() for j in range(self.y)] for i in range(self.x)]

    def in_grid(self, i, j):
        try:
            if self.matrix[i][j]:
                return True
        except:
            return False

    def set_cell(self, i, j, cell):
        if self.in_grid(i, j):
            self.matrix[i][j] = cell
    
    def get_cell(self, i, j):
        if self.in_grid(i, j): 
            return self.matrix[i][j]
    
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def is_neighbor(self, i, j, x, y):
        return (abs(x - i) == 1) or (abs(y - j) == 1)

    def get_neighbors(self, x, y):
        neighbors = [] 
        for i in range(x - 1, x + 2): 
            for j in range(y - 1, y + 2): 
                if self.in_grid(i, j) and self.is_neighbor(i, j, x, y): neighbors.append(self.get_cell(i,j)) 
        return neighbors

    def set_neighbors(self):
        for k in range(self.x):
            for m in range(self.y):
                cell = self.get_cell(k,m)
                cell.set_neighbors(self.get_neighbors(k, m))

    def __str__(self):
        affiche = str()
        for k in range(self.x):
            for m in range(self.y):
                affiche += str(self.get_cell(k, m))
            affiche += "\n"
        affiche += "\r"
        return affiche

    def random_init_cell(self, p):
        for k in range(self.x):
            for m in range(self.y):
                if random.randint(0,100) < p :
                    cell = self.get_cell(k, m)
                    cell.born()
                    cell.bascule()
    
    def play(self):
        for k in range(self.x):
            for m in range(self.y):
                cell = self.get_cell(k, m)
                cell.compute_future()
    
    def refresh(self):
        for k in range(self.x):
            for m in range(self.y):
                cell = self.get_cell(k, m)
                cell.bascule()