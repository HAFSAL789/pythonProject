import copy
maze = [[1,1,0,1],
        [0,1,1,1],
        [0,1,1,1],
        [0,1,1,1]]
length = len(maze)
destination = 2
visitedmaze = [[0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]]
def ratinmaze(maze,start,end,path,visitedm):
    if (start > - 1 and end > -1) and (start < length and end < length):
        if maze[start][end] == 1 and visitedm[start][end] == 0:

            if start == destination and end == destination:
                visitedm[start][end] = path
                print(visitedm)
            visitedm[start][end] = path
            path +=1
            ratinmaze(maze,start,end+1,path,copy.deepcopy(visitedm)),ratinmaze(maze,start-1,end,path,copy.deepcopy(visitedm)),ratinmaze(maze,start,end-1,path,copy.deepcopy(visitedm)),ratinmaze(maze,start+1,end,path,copy.deepcopy(visitedm))
ratinmaze(maze,0,0,1,visitedmaze)
