#!/usr/local/bin/python3
#
# route_pichu.py : a maze solver
#
# Submitted by : [NAME:TANMAY GIRISH MAHINDRAKAR USERNAME:TMAHIND]
#
# Based on skeleton code provided in CSCI B551, Fall 2022.

import sys

class pichu_cell:
        def __init__(self,x_loc,y_loc,move_count,move_string):
                self.x_loc = x_loc
                self.y_loc = y_loc
                self.move_count = move_count
                self.move_string = move_string


# Parse the map from a given filename
def parse_map(filename):
        with open(filename, "r") as f:
                return [[char for char in line] for line in f.read().rstrip("\n").split("\n")][3:]
                
# Check if a row,col index pair is on the map
def valid_index(pos, n, m):
        return 0 <= pos[0] < n  and 0 <= pos[1] < m

# Find the possible moves from position (row, col)
def moves(map, row, col):
        moves=((row+1,col), (row-1,col), (row,col-1), (row,col+1))

        # Return only moves that are within the house_map and legal (i.e. go through open space ".")
        return [ move for move in moves if valid_index(move, len(map), len(map[0])) and (map[move[0]][move[1]] in ".@" ) ]

# Perform search on the map
#
# This function MUST take a single parameter as input -- the house map --
# and return a tuple of the form (move_count, move_string), where:
# - move_count is the number of moves required to navigate from start to finish, or -1
#    if no such route exists
# - move_string is a string indicating the path, consisting of U, L, R, and D characters
#    (for up, left, right, and down)

def search(house_map):
        # Find pichu start position
        pichu_loc = [(row_i,col_i) for col_i in range(len(house_map[0])) for row_i in range(len(house_map)) if house_map[row_i][col_i]=="p"][0]
        #print(pichu_loc)

        visited = [[False for i in range(len(house_map[0]))] for j in range(len(house_map))]
        
        pichu_queue = []
        #print(pichu_loc[0])
        #print(pichu_loc[1])
        pichu_posi = pichu_cell(pichu_loc[0],pichu_loc[1],0,'')

        pichu_queue.append(pichu_posi)
        visited[pichu_posi.x_loc][pichu_posi.y_loc] = True

        while(len(pichu_queue)!=0):
                pichu_posi = pichu_queue.pop(0)

                if house_map[pichu_posi.x_loc][pichu_posi.y_loc] == '@':
                        return (pichu_posi.move_count, pichu_posi.move_string)
                
                if (pichu_posi.x_loc - 1,pichu_posi.y_loc) in  moves(house_map,pichu_posi.x_loc,pichu_posi.y_loc) and visited[pichu_posi.x_loc - 1][pichu_posi.y_loc] != True:
                        pichu_queue.append(pichu_cell(pichu_posi.x_loc - 1,pichu_posi.y_loc, pichu_posi.move_count + 1, pichu_posi.move_string + 'U'))
                        visited[pichu_posi.x_loc - 1][pichu_posi.y_loc] = True
                        # print("moving UP")

                if (pichu_posi.x_loc + 1,pichu_posi.y_loc) in  moves(house_map,pichu_posi.x_loc,pichu_posi.y_loc) and visited[pichu_posi.x_loc + 1][pichu_posi.y_loc] != True:
                        pichu_queue.append(pichu_cell(pichu_posi.x_loc + 1,pichu_posi.y_loc, pichu_posi.move_count + 1, pichu_posi.move_string + 'D'))
                        visited[pichu_posi.x_loc + 1][pichu_posi.y_loc] = True
                        # print("moving DOWN")

                if (pichu_posi.x_loc,pichu_posi.y_loc - 1) in  moves(house_map,pichu_posi.x_loc,pichu_posi.y_loc) and visited[pichu_posi.x_loc][pichu_posi.y_loc - 1] != True:
                        pichu_queue.append(pichu_cell(pichu_posi.x_loc,pichu_posi.y_loc - 1, pichu_posi.move_count + 1, pichu_posi.move_string + 'L'))
                        visited[pichu_posi.x_loc][pichu_posi.y_loc - 1] = True
                        # print("moving LEFT")

                if (pichu_posi.x_loc,pichu_posi.y_loc + 1) in  moves(house_map,pichu_posi.x_loc,pichu_posi.y_loc) and visited[pichu_posi.x_loc][pichu_posi.y_loc + 1] != True:
                        pichu_queue.append(pichu_cell(pichu_posi.x_loc,pichu_posi.y_loc + 1, pichu_posi.move_count + 1, pichu_posi.move_string + 'R'))
                        visited[pichu_posi.x_loc][pichu_posi.y_loc + 1] = True
                        # print("moving RIGHT")

                

                # print(list(moves(house_map,pichu_posi.x_loc,pichu_posi.y_loc)))

                # print(type(moves(house_map,pichu_posi.x_loc,pichu_posi.y_loc)))
                # print(type(([pichu_posi.x_loc - 1,pichu_posi.y_loc])))
                # print((pichu_posi.x_loc - 1,pichu_posi.y_loc) in  moves(house_map,pichu_posi.x_loc,pichu_posi.y_loc))
                
                # print(visited)

                # print((4,0) in moves(house_map,pichu_posi.x_loc,pichu_posi.y_loc))


        return (-1,"")
                




# Main Function
if __name__ == "__main__":
        house_map=parse_map(sys.argv[1])
        print("Shhhh... quiet while I navigate!")
        # visited1 = [[False for _ in range(len(grid[0]))]
        #        for _ in range(len(grid))]
        
        ans = search(house_map)
        
        # solution = search(house_map)
        print("Here's the solution I found:")
        print(str(ans[0])+" "+ans[1])

        # print(str(solution[0]) + " " + solution[1])

