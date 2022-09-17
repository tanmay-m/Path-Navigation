# tmahind-a0


## Elements of AI Assignment 01 (Problem 01 - Navigation):

The problem was a classic shortest distance algorithm where obstacles were denoted as 'X' and valid path by '.'.
My approach to this solution is breadth first search algorithm that explores all possible grid places to jump to.
To avoid recurrence to the same path, I have used a generic Boolean visited array that stores if the location was visited or not in the past(True or False). 
We only visit the path that has not been visited before!
To dive in the details, every cell has 4 possible directions to jump. In BFS (breadth first search) we explore all neighboring cells simultaneously and return the distance once the pichu(that reaches first) has reached the desired cell (i.e '@').
I have implemented the queue data structure using functions of append() and pop(0).
From each current position, new valid cells which are not visited before are appended into to queue and are later popped to follow their own path to the destination!
Calculating the minimum distance was easy, but to return a string was a little bit tricky (not too tricky to be said). 
I first had an idea of storing a string list for grid location, but later I decided to go with class data structure for better readability.
I track the x and y axis of grid, the travelled distance and the string path for the followed track. I simply update the cell class grid's string by appending the move (i.e R/U/D/L). Once we reach the goal destination, I have my answers in the class object. I simply return distance and string to the main function in the form of tuple as mentioned. 


### Set of valid states: 
Valid states are the positions of pichus (at the current instance) and their distance from the original pichu location i.e the starting point. 

### Successor Function: 
The successor function can be defined as the set of valid directions the pichu can travel. In other words, the valid locations the pichu can travel without conflicting with obstacles and the positions visited in the past (tracked by visited array).

### Goal State Definition:
The goal state definition is the state in which the pichu has travelled and reached the destination ('@'). Also, if the goal state is not reached, we can return -1 stating that the goal state can not be reached within the given grid.

### Initial State:
The initial state is the grid with pichu in its starting location, with multiple or no obstacles denoted as 'X' with the destination cell marked with '@'.

### Cost Function:
The cost function can be defined as total paths covered to reach the goal state. In this case, we can measure the cost function by distance of traversals or the summation of number of times we have moved from one state to the other. 



## Elements of AI Assignment 01 (Problem 02 -  Hide and Seek):

This problem can be categorized as a twisted version of the classic N-Queens problem. The twist is in the gird, wherein, there are obstacles which are treated as wall and a pichu can hide behind the wall even if the there is a pichu in its killing direction. 
To attain this flexibility, I have defined a safe function which computes the safety parameter from all attacking directions. The directions are up, down, right, left, diagonal up-left, diagonal up-right, diagonal down-left and diagonal down-right. 
To compute the final grid state, we go through the sets of valid states followed by the states returned from the successor function. Here, I have made a Depth First Search approach to find the states which can potentially reach the final state of placing ‘k’ number of pichus in the grid. The DFS approach can be seen in the code using stack fringe as its functions of append() and pop().  In the code, we can see a fringe data structure used as a queue with simple append and pop functions. In this way, we push each elements into grid and exploring our solution until we find a final state which matches our goal state.

IMPORTANT (CHALLENGES FACED):
Here, from observation, we can easily tell that there can be many solution for a single value of k. In my first attempt on solving this problem, I was unaware about the need to find only one solution, so my program gave all possible outcomes for any value of k. While running the code for map1.txt and pichus 7 or 6, I got so many solutions in the console that all my solutions were not visible (due to console overwriting). In that code, I use multiple calls to a function called backtrack(), wherein I call this function for each row and the next one. 
After consulting TA Radhyesham, he told me stick with one solution as the testing server may not respond properly to this output. After this, my code got much simpler which can be seen in the solve function and sadly, I had to comment my functions and all the dear hard work that was put in earlier. If you wish to check all possible solutions, you can reverse the commented parts in the solve() function and also the backtrack(r) function and run the program to check for all possible solutions if you are really interested. (Although it might not work correctly on test server but the output can be seen in the console). 


### State of Valid States: 
The valid states in this problem can be defined as the states in which the number of pichus mentioned can fit inside the grid without any conflicting positions.

### Cost Function:
The cost function in this scenario can be defined as the number of steps taken to reach the goal state of ‘k’ pichus exactly fitting inside the map without any hindrance.

### Successor Function:
The successor function in this scenario can be explained as the next valid grid states that can be considered during the search function. Meaning, the next states which give the potential valid locations to place the pichu/pichus.
 
### Goal State:
The Final Goal State can be observed as the grid with pichus at locations which are not conflicting with other pichus. If the goal state can not be reached, we return False denoting the same.

### Initial State:
The initial state is the state in which the map contains at least one pichu with obstacles and the observer denoted as ‘@’ which is to be treated as a wall. 
