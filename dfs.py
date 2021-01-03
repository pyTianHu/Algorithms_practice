from Algorithms_prac import Stack
from matrixes import matrixNames,simple_sixbysix, obstacle_sixbysix
from helperfunctions import offsets,positionChecker,pathTracker

#Working with stack
#Pushing start position into the stack
#Assigning current position and check if current position == goal
# if yes => return path
# if no =>  get direction offsets and assign neighboring cell alues
           #if the neighboring cell values are valid, and they are not already checked (predecessors) push them to stack #in the matrix range, not obstacles, not walls (#)

def dfs(matrix,start,goal):
    stack = Stack()
    stack.push(start)
    predecessors = {start: None}
    
    while not stack.isempty():
        currentCell = stack.pop()
        #print(currentCell) - mükszik, a start értékeit adja vissza
        if currentCell == goal:
            return pathTracker(predecessors, start, goal)
        for direction in ["right","left","up","down"]:
            rowOffset, colOffset = offsets[direction]
            neighbor = (currentCell[0]+rowOffset) , (currentCell[1] + colOffset)
            #print(currentCell,neighbor) - mükszik a positiontjek funkció
            if positionChecker(matrix, neighbor) and neighbor not in predecessors:
                stack.push(neighbor)
                predecessors[neighbor] = currentCell
                #print(currentCell , neighbor)
                #print(stack)
                #print("-------------------------\n")


start = (1,1)
goal = (4,4)

dfs(simple_sixbysix,start,goal)
