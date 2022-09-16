#!/usr/local/bin/python3
#
# arrange_pichus.py : arrange agents on a grid, avoiding conflicts
#
# Submitted by : [NAME: TANMAY GIRISH MAHINDRAKAR USERNAME: TMAHIND]
#
# Based on skeleton code in CSCI B551, Fall 2022.

from pickle import FALSE
import sys
from turtle import back

# Parse the map from a given filename
def parse_map(filename):
	with open(filename, "r") as f:
		return [[char for char in line] for line in f.read().rstrip("\n").split("\n")][3:]

# Count total # of pichus on house_map
def count_pichus(house_map):
    return sum([ row.count('p') for row in house_map ] )

# Return a string with the house_map rendered in a human-pichuly format
def printable_house_map(house_map):
    return "\n".join(["".join(row) for row in house_map])

# Add a pichu to the house_map at the given position, and return a new house_map (doesn't change original)
def add_pichu(house_map, row, col):
    return house_map[0:row] + [house_map[row][0:col] + ['p',] + house_map[row][col+1:]] + house_map[row+1:]

# Get list of successors of given house_map state
def successors(house_map):
    return [ add_pichu(house_map, r, c) for r in range(0, len(house_map)) for c in range(0,len(house_map[0])) if house_map[r][c] == '.' and isSafe(house_map,r,c)]

# check if house_map is a goal state
def is_goal(house_map, k):
    return count_pichus(house_map) == k 

# Arrange agents on the map
#
# This function MUST take two parameters as input -- the house map and the value k --
# and return a tuple of the form (new_house_map, success), where:
# - new_house_map is a new version of the map with k agents,
# - success is True if a solution was found, and False otherwise.
#

def isSafe(initial_house_map,row,col):
    #above
    safety = True
    if initial_house_map[row][col] == 'p' or initial_house_map[row][col] == 'X' or initial_house_map[row][col] == "@":
        return False
    for i in range(row, -1, -1):
        if initial_house_map[i][col] != '.':
            if initial_house_map[i][col] == 'X' or initial_house_map[i][col] == '@':
                break
            else:
                safety = False
                return False
    #below
    for i in range(row,len(initial_house_map),1):
        if initial_house_map[i][col] != '.':
            if initial_house_map[i][col] == 'X' or initial_house_map[i][col] == '@':
                break
            else:
                safety = False
                return False

    #right
    for i in range(col,len(initial_house_map[0]),1):
        if initial_house_map[row][i] != '.':
            if initial_house_map[row][i] == 'X' or initial_house_map[row][i] == '@':
                break
            else:
                safety = False
                return False
    
    #left
    for i in range(col, -1 , -1):
        if initial_house_map[row][i] != '.':
            if initial_house_map[row][i] == 'X' or initial_house_map[row][i] == '@':
                break
            else:
                safety = False
                return False
        

    #diag_up_left
    #col can be 0
    #row can be 0
    r,c = row,col
    while(r>-1 and c>-1):
        if initial_house_map[r][c] != '.':
            if initial_house_map[r][c] == 'X':
                break
            else:
                safety = False
                return False
        r-=1
        c-=1

    #diag_down_left
    #col can be 0
    #row can be full
    r,c = row,col
    while(c>-1 and r<len(initial_house_map)):
        if initial_house_map[r][c] != '.':
            if initial_house_map[r][c] == 'X':
                break
            else:
                safety = False
                return False
        r+=1
        c-=1
        
    #diag_up_right
    #col can be full
    #row can be 0
    r,c = row,col
    while(r>-1 and c<len(initial_house_map[0])):
        if initial_house_map[r][c] != '.':
            if initial_house_map[r][c] == 'X':
                break
            else:
                safety = False
                return False
        r-=1
        c+=1

    #diag_down_right
    #col can be full
    #row can be full
    r,c = row,col
    while(r<len(initial_house_map) and c<len(initial_house_map[0])):
        if initial_house_map[r][c] != '.':
            if initial_house_map[r][c] == 'X':
                break
            else:
                safety = False
                return False
        r+=1
        c+=1

    return safety


def solve(initial_house_map,k):
    
    # result = []

    # # first pichu initialization
    # pichu_loc = [(row_i,col_i) for col_i in range(len(initial_house_map[0])) for row_i in range(len(initial_house_map)) if initial_house_map[row_i][col_i]=="p"][0]    #initial pichu loc
    # col.add(pichu_loc[1])
    # diag_pos.add(pichu_loc[0] + pichu_loc[1])
    # diag_neg.add(pichu_loc[0] - pichu_loc[1])
    # #print(col,diag_pos,diag_neg)


    # # fringe = [initial_house_map]
    # # while len(fringe) > 0:
    # #     for new_house_map in successors( fringe.pop() ):
    # #         #print(new_house_map)
    # #         if is_goal(new_house_map,k):
    # #             return(new_house_map,True)
    # #         fringe.append(new_house_map)
    # #         print("appended",new_house_map)
    # new_house_map = initial_house_map.copy()    
    # def backtrack(r):
    #     # if is_goal(new_house_map,k):
        
       
    #     if count_pichus(new_house_map)==k:
    #         print(printable_house_map(new_house_map))
    #         print("#############")
    #         return new_house_map
    #     if r == len(new_house_map):
    #             return

    #     #print("Value of r is",r)

    #     for c in range(len(new_house_map[0])):
    #         #print(r,c)
    #         # if c in col or (r + c) in diag_pos or (r - c) in diag_neg or new_house_map[r][c] == 'X' or new_house_map[r][c] == '@':
    #         # if not(isSafe(new_house_map,r,c)) or new_house_map[r][c] == '@':
    #         if not(isSafe(new_house_map,r,c)) or new_house_map[r][c] == 'X' or new_house_map[r][c] == '@':
    #             # print("Value of row is",r)
    #             # print("Value of col is",c)
    #             # print("Inside this loop")
    #             #print(col,diag_pos,diag_neg)
    #             #print("Success",r,c)
    #             continue
    #         new_house_map[r][c] = 'p'
            

    #         # print(col,diag_pos,diag_neg)
    #         # print("Row incr",r+1)
    #         #print("At backtrack",r+1)
    #         backtrack(r + 1)
    #         new_house_map[r][c] = '.'
    #     if r != len(new_house_map):              ##commented this now
    #         backtrack(r+1)
            
        
    # ans = backtrack(0)
    # print(ans)
    # return ans
    if(k == 1):
        return(initial_house_map,True)

    fringe = [initial_house_map]
    while len(fringe) > 0:
        for new_house_map in successors( fringe.pop() ):
            if is_goal(new_house_map,k):
                return(new_house_map,True)
            fringe.append(new_house_map)
    return ([],False)





import time

# Main Function
if __name__ == "__main__":
    house_map=parse_map(sys.argv[1])
    # print(house_map)
    # This is k, the number of agents
    grid = [['.','X','X','@'],
            ['X','X','X','.'],
            ['X','X','X','X'],
            ['X','p','X','X']]
    k = int(sys.argv[2])
    start = time.time()
    solution = solve(house_map,k)
    end = time.time()
    print(start - end)
    # a = isSafe(grid,2,1)
    #print(printable_house_map(ans[0]))
    # print(ans)
    print ("Starting from initial house map:\n" + printable_house_map(house_map) + "\n\nLooking for solution...\n")
    # solution = solve(house_map,k)
    print ("Here's what we found:")
    print (printable_house_map(solution[0]) if solution[1] else "False")


