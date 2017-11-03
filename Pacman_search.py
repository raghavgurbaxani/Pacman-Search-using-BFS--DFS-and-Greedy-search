import numpy as np
import sys
import os.path

# global variables

# list to store the frontier
frontier = []

# matrix to store heuristic for each location
heuristic = []

# value to indicate if we have found all dots (equal to 1 if all dots have been found)
found = 0

# counter to keep track of total steps taken in each search strategy
bfs_steps = None

# counter to keep track of number of nodes expanded in each search
bfs_nodes_expanded = 0

# cost of min path
bfs_final_cost = 0

bfs_final_cost = 0

def main():
    global frontier
    global bfs_steps
    global dfs_steps
    global bfs_final_cost
    global heuristic

    # save maze into 2d numpy array
    maze = convertMazeToList('C:\\Users\\Raghav\\Desktop\\mediumMaze.txt')
    maze_height = maze.shape[0]
    maze_width = maze.shape[1]

    # numpy array representing the minimum cost to get to each location in maze
    bfs_steps = np.empty(([maze_height, maze_width]))

    # initialize each value to max possible int value
    bfs_steps[:] = sys.maxsize

    # get all locations of dots in maze
    dot_locations = get_Dots(maze)
    print("dot locations: ", dot_locations)

    # get starting location of search
    start_location = getStartingPosition(maze)
    print("start location: ", start_location)

    # set cost to get to starting location to 0
    bfs_steps[start_location[0], start_location[1]] = 0
    frontier = [start_location]
    while(len(frontier) > 0):
        bfs(maze)
        #c=c+1
        #if (c==1000):
         #   break

#    print("dfs_nodes_expanded: ", dfs_nodes_expanded)
 #   print("dfs steps: ", dfs_steps)
    print(maze)
    print("bfs_nodes_expanded: ", bfs_nodes_expanded)

def bfs(maze):
    global frontier
    global found
    global bfs_steps
    global bfs_nodes_expanded

    # list to hold all children locations
    children = []

    # pop current location from front of queue
    current_location = frontier[0]
    bfs_nodes_expanded += 1

    # minimum number of steps taken to get to the current location
    current_steps = bfs_steps[current_location[0], current_location[1]]

    # remove the node from frontier
    frontier.pop(0)

    # if current location is the dot, we pop it out of dots list
    if maze[current_location[0], current_location[1]] == '.':
        print("found dot at: ", current_location[0], ",", current_location[1])
        print("found dot with path cost: ", current_steps)
        #frontier = []
        return

    # get children in order: top, right, bottom, left
    children.append((current_location[0] - 1, current_location[1]))
    children.append((current_location[0], current_location[1] + 1))
    children.append((current_location[0] + 1, current_location[1]))
    children.append((current_location[0], current_location[1] - 1))

    for child in children:
        # if child is valid destination, add it to frontier and update path cost
        if maze[child[0], child[1]] == ' ':
            frontier.append((child[0], child[1]))
            bfs_steps[child[0], child[1]] = current_steps + 1

        # if child has already been visited or is goal, add it to frontier and update step cost if it's less than previous min
        elif maze[child[0], child[1]] == '.' or maze[child[0], child[1]] == 'v':
            previous_min = bfs_steps[child[0], child[1]]

            if previous_min > current_steps + 1:
                frontier.append((child[0], child[1]))
                bfs_steps[child[0], child[1]] = current_steps + 1

    maze[current_location[0], current_location[1]] = 'v'
    
# Read a text file representing a maze and construct a 2D array
def convertMazeToList(filename):
    maze_matrix = np.genfromtxt(filename, dtype=str, delimiter=1)
    size = maze_matrix.shape
    return maze_matrix


# Find all dot locations of a given maze matrix
def get_Dots(maze):
    dot_locations = list(np.where(maze=='.'))
    return dot_locations


# Return the starting indices (location of 'P')
def getStartingPosition(maze):
    start_location = np.where(maze=='P')
    return (start_location[0][0], start_location[1][0])

if __name__ == "__main__":
    main()

