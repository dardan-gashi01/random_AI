import numpy as np
import matplotlib.pyplot as plt

#setting the size of the Grid
Gridsize = 6

#creating a grid of size Gridsize and generating all of the grids with random valuesf rom 1-9
grid = np.random.randint(0, 9, size=(Gridsize, Gridsize))
#setting the value of the start value which is the top left
grid[0,0]=np.random.randint(0,9)
#same thing as above but this time the target which is bottom right
grid[Gridsize-1,Gridsize-1]= np.random.randint(0,9)
#creating the grid using matplot library
fig, ax = plt.subplots(figsize=(Gridsize, Gridsize))
#turning axis off so it looks nicer
ax.axis("off")
#this creates a matrix so it is easier to use while coding
ax.matshow(grid, cmap = None)

#filling the grid with the numbers and centering the numbers
for y in range(Gridsize):
    for x in range(Gridsize):
        cell = grid[y][x]
        ax.text(x, y, str(cell), va='center', ha='center')
#showing the grid to the user
plt.show()

#function for task1a so Dijkstra
def shortestPath1(graph, start, end):
    
    


    
    
shortestPath1(grid, grid[0,0], grid[Gridsize-1,Gridsize-1])
