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
    
    #map of unvisited nodes to know what we have and have not visited
    unvisited = np.zeros((Gridsize,Gridsize),dtype=bool)
    #making a map of infinities to be able to track the shortest path 
    dist=np.ones((Gridsize,Gridsize),dtype=int)*np.Infinity
    #making the starting point 0
    dist[0,0] = 0
    visited = []
    #print(unvisited)
    
    #print(visited)
    complete = False
    count = 0
    
    
    while x != Gridsize-1 and y != Gridsize -1:
    #to look to the right if we have any neighbours there
        if x < Gridsize -1:
            print('value of right node is: ' + str(graph[y, x+1]))
            print('coordinate of the right node is : '+ str(x+1) +',' +str(y))
            count += 1
            print(count)
            x+=1
            # if dist[y,x+1]>graph[y,x+1]+dist[y,x] and not unvisited[y,x+1]:
            #     dist[y,x+1]=graph[y,x+1]+dist[y,x]
            #     print(dist)
                #complete = True
        #to look to the left if we have any neighbours there
        if x > 0:
            print('value of the left node is: '+ str(graph[y,x-1]))
            print('coordinate of the left node is : '+ str(x-1) +',' +str(y))
            count += 1
            print(count)
            x-=1
            # if dist[y,x-1]>graph[y,x-1]+dist[y,x] and not unvisited[y,x-1]:
            #     dist[y,x-1]=graph[y,x-1]+dist[y,x]
            #     print(dist)
                #complete = True
        #to look down to see if we have any neighbours there
        if y < Gridsize -1:
            print('value of the down node is: '+ str(graph[y+1,x]))
            print('coordinate of the down node is : '+ str(x) +',' +str(y+1))
            count += 1
            print(count)
            y+=1
            # if dist[y+1,x]>graph[y+1,x]+dist[y,x] and not unvisited[y+1,x]:
            #     dist[y+1,x]=graph[y+1,x]+dist[y,x]
            #     print(dist)
                #complete = True
        if y > 0:
            print('value of the above node is: '+ str(graph[y-1,x]))
            print('coordinate of the above node is : '+ str(x) +',' +str(y-1)) 
            count += 1
            print(count)
            y-=1
            # if dist[y-1,x]>graph[y-1,x]+dist[y,x] and not unvisited[y-1,x]:
            #     dist[y-1,x]=graph[y-1,x]+dist[y,x]
            #     print(dist)
                #complete = True
        unvisited[x,y]=True
        #print(unvisited)
                
        
        
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
