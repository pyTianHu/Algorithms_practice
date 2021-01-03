from Algorithms_prac import Stack
from matrixes import matrixNames,simple_sixbysix, obstacle_sixbysix
from helperfunctions import offsets,positionChecker,pathTracker

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
