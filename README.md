# tmahind-a0
Elements of AI Assignment 01 (Problem 01):

The problem was a classic shortest distance algorithm where obstacles were denoted as 'X' and valid path by '.'.
My approach to this solution is breadth first search algorithm that explores all possible grid places to jump to.
To avoid recurrence to the same path, I have used a generic Boolean visited array that stores if the location was visited or not in the past(True or False). 
We only visit the path that has not been visited before!
To dive in the details, every cell has 4 possible directions to jump. In BFS (breadth first search) we explore all neighboring cells simultaneously and return the distance once the route(that reaches first) has reached the desired cell (i.e '@').
I have implemented the queue data structure by 
Calculating the minimum distance was easy, but to return a string was a little bit tricky (not too tricky to be said). 
I first had an idea of storing a string list for grid location, but later I decided to go with class data structure for better readability.
I track the x and y axis of grid, the travelled distance and the string path for the followed track. I simply update the cell class grid's string by appending the move (i.e R/U/D/L). Once we reach the goal destination, I have my answers in the class object. I simply return distance and string to the main function in the form of tuple as mentioned. 

Set of valid states: 
Valid states are the positions of pichus and their distance from the original pichu location i.e the starting point.

Successor Function: 
The successor function can be defined as the set of valid directions the pichu can travel. In other words, the valid locations the pichu can travel without conflicting with obstacles and the positions visited in the past (tracked by visited array).

Goal State Definition:
The goal state definition is the state in which the pichu has travelled and reached the destination ('@'). Also, if the goal state is not reached, we can return -1 stating that the goal state can not be reached within the given grid.

Initial State:
The initial state is the grid with pichu in its starting location, with multiple or no obstacles denoted as 'X' with the destination cell marked with '@'.



Elements of AI Assignment 01 (Problem 02):

State of Valid States: 
The valid states in this problem can be defined as the states in which the number of pichus mentioned can fit inside the grid without any conflicting positions.

Cost Function: 

Successor Function:

Goal State:
The Final Goal State can be observed as the grid with pichus at locations which are not conflicting with other pichus. If the goal state can not be reached, we return False denoting the same.

Initial State:





