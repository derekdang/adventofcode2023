# https://adventofcode.com/2023/day/18
import sys
from tqdm import tqdm

def p1(input: list[list[str]]) -> int:
    m, n = 1000, 1000
    grid = [["." for _ in range (n)] for _ in range(m)]
    curr_r, curr_c = 500, 500
    dirs = {"R": (0,1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}
    edge = 0
    for line in input:
        dir, steps, color = line.split(" ")
        next_move = dirs[dir]
        edge += int(steps)
        for i in range(int(steps)):
            grid[curr_r + next_move[0]][curr_c + next_move[1]] = "#"
            curr_r = curr_r + next_move[0]
            curr_c = curr_c + next_move[1]
    lava_added_by_depth = 0
    filled = False
    visited = set()
    for r, line in enumerate(grid):
        l = "".join(line)
        first_index = l.find('#')
        last_index = l.rfind('#')
        if filled:
            break
        if first_index == -1 or last_index == -1:
            continue
        elif first_index != -1 and last_index != -1:
            q = []
            for c in range(first_index, last_index):
                if grid[r][c] == "." and not filled:
                    q.append((r,c))
                    while len(q) != 0:
                        size = len(q)
                        for i in range(size):
                            p = q.pop(0)
                            lava_added_by_depth += 1
                            grid[p[0]][p[1]] = "#"
                            visited.add(p)
                            for move in dirs.values():
                                next_move = (p[0] + move[0], p[1] + move[1])
                                if grid[next_move[0]][next_move[1]] == "." and next_move not in q and next_move not in visited:
                                    q.append(next_move)
                    filled = True
    return lava_added_by_depth + edge

def p2(input: list[list[str]]) -> int:
    z = {"0": "R", "1": "D", "2": "L", "3": "U"}
    edge = 0
    x_s, y_s = [], []
    x, y = 0, 0
    for line in input:
        dir, steps, color = line.split(" ")
        # _, _, color = line.split(" ")
        # dir = z[color[-2]]
        # steps = int(color[2: len(color) - 2], 16)
        steps = int(steps)
        edge += steps
        if dir == "R":
            x += steps
        elif dir == "L":
            x -= steps
        elif dir == "U":
            y += steps
        elif dir == "D":
            y -= steps
        x_s.append(x)
        y_s.append(y)
    print(x_s)
    print(y_s)
    # x_s = [-2, 0, 3, 1]
    # y_s = [-2, 4, -1, -1]
    s1 = 0
    s2 = 0
    s_1 = []
    s_2 = []
    for i,(a,b) in enumerate(zip(x_s, y_s)):
        next_x_row = x_s[(i + 1) % len(x_s)]
        next_y_row = y_s[(i + 1) % len(y_s)]
        s1 += (a * next_y_row)
        s2 += (b * next_x_row)
        s_1.append(a * next_y_row)
        s_2.append(b * next_x_row)
    print(s_1)
    print(s_2)
    print(abs(s1-s2) // 2)
    print(edge)
    return -1

if __name__ == "__main__":
    input = open(sys.argv[1]).read().splitlines()
    print(p1(input))
    p2(input)