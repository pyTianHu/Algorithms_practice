offsets = {
    "right": (0,1),
    "left": (0,-1),
    "up": (-1,0),
    "down": (1,0),
}


def positionChecker(matrix, pos):
    i, j = pos
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    return 0 <= i < num_rows and 0 <= j < num_cols and matrix[i][j] != "#"


def pathTracker(predecessors, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = predecessors[current]
    path.append(start)
    path.reverse()
    print(start,goal,path)