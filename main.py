from grid import Grid
import time

g = Grid(10)
g.random_init_cell(33)
g.set_neighbors()

while True:
    print(g)
    print("\n")
    time.sleep(0.5)
    g.play()
    g.refresh()