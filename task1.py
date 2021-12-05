import numpy as np
import matplotlib.pyplot as plt

#setting the size of the Grid
Gridsize = 3

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

# print(grid[0, 0+1])
#  = move right
 
# print([grid[0+1, 0]])
# =move down

def shortestPath1(graph, start, end):
   
    current = start
    x,y = 0,0
    path = []
    path.append((x,y))
    print(current)
    
    unvisited = np.zeros((Gridsize,Gridsize),dtype=bool)
    dist=np.ones((Gridsize,Gridsize),dtype=int)*np.Infinity
    #making the starting point 0
    dist[0,0] = 0
    visited = []
    print(unvisited)
    
    #print(visited)
    complete = False
    
    
    # while not complete:
    #to look to the right if we have any neighbours there
    if x < Gridsize -1:
        print(x+1, y)
    #to look to the left if we have any neighbours there
    if x > 0:
        print(x-1,y)
    #to look down to see if we have any neighbours there
    if y < Gridsize -1:
        print(x,y+1)
    if y > 0:
        print(x,y-1)        
        
    
    #while (len(visited) < GridSize):
        
    #while not complete:
        
    #if ((x>0 or y>0) and x+1< len(graph) and y+1<len(graph)):
        
        
    
    #
    #brute force answer
    #
    # while x != Gridsize-1 or y != Gridsize-1:
    #     #looking right to see if its in bounds if it goes right
    #     if x+1 < graph.shape[0]:
    #         #looking right to see if its in bounds if it goes down
    #         if y+1 < graph.shape[1]:
    #             if (graph[y,x+1] > graph[y+1,x]):
    #                 print(grid[y+1, x])
    #                 print("down")
    #                 current = grid[y+1,x]
    #                 y+=1
    #                 print(y)
    #                 path.append((x,y))
    #                 print(path)
    #             else:
    #                 print(grid[y,x+1])
    #                 print("right")
    #                 current = grid[y,x+1]
    #                 x+=1
    #                 print(x)
    #                 path.append((x,y))
    #                 print(path)
    #         else:
    #             print(grid[y,x+1])
    #             print("right")
    #             current = grid[y,x+1]
    #             x+=1
    #             print(x)
    #             path.append((x,y))
    #             print(path)
    #     else:
    #         print(grid[y+1,x])
    #         print("down")
    #         current = grid[y+1,x]
    #         y+=1
    #         print(y)
    #         path.append((x,y))
    #         print(path)
            
            
    #highlight the path that it is moving
    
shortestPath1(grid, grid[0,0], grid[Gridsize-1,Gridsize-1])

# def shortestPath2():
