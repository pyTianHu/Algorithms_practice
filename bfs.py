from Algorithms_prac import Queue
from matrixes import matrixNames,simple_sixbysix, obstacle_sixbysix
from helperfunctions import offsets,pathTracker,positionChecker

#working with Queue
#enqueue startvalue, so queue is not empty right away, we have something to work with
#Dequeue
#is the dequeued value the goal?
    #yes => done
    #no =>  enqueue undiscovered neighbors
            #update predecessors with current cell so path can be given back
            #repeat until yes

def bfs(maze, start, goal):
    q = Queue()
    q.enqueue(start)
    predecessors = {start: None}

    while not q.isempty():
        currentCell = q.dequeue()
        if currentCell == goal:
            return pathTracker(predecessors, start, goal)
        for direction in ["up", "right", "down", "left"]:
            rowOffset, colOffset = offsets[direction]
            neighbor = (currentCell[0] + rowOffset, currentCell[1] + colOffset)
            if positionChecker(maze, neighbor) and neighbor not in predecessors:
                q.enqueue(neighbor)
                predecessors[neighbor] = currentCell
    return None


start = (1,1)
goal = (4,4)

bfs(simple_sixbysix,start,goal)