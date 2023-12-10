# https://adventofcode.com/2023/day/10
import sys
from tqdm import tqdm
import re

def p1():
    start_rc = 0,0
    for i, row in enumerate(input):
        for j, col in enumerate(row):
            if col == "S":
                start_rc = i,j
    
    curr_pos = start_rc
    valid_moves = []
    
    for dir, conn in zip(dirs, connectors):
        new_r = start_rc[0] + dir[0]
        new_c = start_rc[1] + dir[1]
        connecting_pipe = input[new_r][new_c]
        if connecting_pipe in conn:
            valid_moves.append((new_r, new_c))

    dist = 1
    coord_dist = {start_rc: 0}
    while len(valid_moves) != 0:
        size = len(valid_moves)
        for i in range(size):
            curr_pos = valid_moves.pop(0)
            curr_char = input[curr_pos[0]][curr_pos[1]]
            coord_dist[curr_pos] = dist
            m = pipe_map[curr_char]
            for dir in m:
                new_r = curr_pos[0] + dir[0]
                new_c = curr_pos[1] + dir[1]
                if new_r < 0 or new_r >= len(input) or new_c < 0 or new_c >= len(input[0]):
                    continue

                connecting_pipe = input[new_r][new_c]
                if (new_r, new_c) not in coord_dist:
                    valid_moves.append((new_r, new_c))
        dist += 1
    print(max(coord_dist.values()))

    arr = []
    for i, row in enumerate(input):
        r = []
        arr.append(r)
        for j, col in enumerate(row):
            if (i,j) not in coord_dist:
                r.append("x")
            else:
                r.append(input[i][j])
    
    num_outside = 0
    for i, row in enumerate(arr):
        for j, char in enumerate(row):
            if char == "x":
                num_pipes = 0
                k = j
                while k >= 0:
                    if arr[i][k] in p2_conn:
                        num_pipes += 1
                    k -= 1
                if num_pipes % 2 == 1:
                    num_outside += 1
    print(num_outside)
    # for row in arr:
    #     print("".join(row))
p2_conn = ["|", "L", "J", "S"]
vpipe = [(1, 0), (-1, 0)]
hpipe = [(0, 1), (0, -1)]
lpipe = [(-1, 0), (0, 1)]
jpipe = [(0, -1), (-1, 0)]
fpipe = [(0, 1), (1, 0)]
sevpipe = [(1, 0), (0, -1)]
pipe_map = {"|": vpipe, "-": hpipe, "L": lpipe, "J":jpipe, "7":sevpipe, "F":fpipe}

south_connecting_pipes = ["|", "L", "J"]
north_connecting_pipes = ["|", "7", "F"]
east_connecting_pipes = ["-", "7", "J"]
west_connecting_pipes = ["-", "L", "F"]

connectors = [east_connecting_pipes, west_connecting_pipes, south_connecting_pipes, north_connecting_pipes]
dirs = [(0, 1), (0, -1), (1, 0),(-1, 0)]
if __name__ == "__main__":
    input = open(sys.argv[1]).read().splitlines()
    p1()
