# https://adventofcode.com/2023/day/16
import sys
from tqdm import tqdm
def p1(entry_point_r, entry_point_c, start_dir):
    card_dirs = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}
    d_map = {"L": "<", "R": ">", "U": "^", "D": "v"}
    visited = set()
    distinct_dirs = {}
    simple_list = ["<",">", "^", "v"]
    q = []
    m, n = len(input), len(input[0])
    grid = [["." for _ in range(n)] for _ in range(m)]
    q.append((entry_point_r, entry_point_c, start_dir))
    prev_len = len(visited)
    while len(q) != 0:
        size = len(q)
        for i in range(size):
            r,c,dir = q.pop(0)
            if r < 0 or r >= m or c < 0 or c >= n:
                continue
            if input[r][c] == ".": 
                visited.add((r, c, dir))
                if grid[r][c] == ".":
                    grid[r][c] = d_map[dir]
                    distinct_dirs[(r,c)] = set()
                    distinct_dirs[(r,c)].add(d_map[dir])
                else:
                    if grid[r][c] in simple_list:
                        distinct_dirs[(r,c)].add(d_map[dir])
                        if len(distinct_dirs[(r,c)]) > 1:
                            grid[r][c] = len(distinct_dirs[(r,c)])
                new_r, new_c = r + card_dirs[dir][0], c + card_dirs[dir][1]
                q.append((new_r, new_c, dir))
            elif input[r][c] == "/":
                grid[r][c] = "/"
                visited.add((r, c, dir))
                new_dir = ""
                if dir == "R":
                    new_r, new_c, new_dir = go_up(card_dirs, r, c)
                elif dir == "L":
                    new_r, new_c, new_dir = go_down(card_dirs, r, c)
                elif dir == "U":
                    new_r, new_c, new_dir = go_right(card_dirs, r, c)
                elif dir == "D":
                    new_r, new_c, new_dir = go_left(card_dirs, r, c)
                q.append((new_r, new_c, new_dir))
            elif input[r][c] == "\\":
                grid[r][c] = "\\"
                visited.add((r, c, dir))
                new_dir = ""
                if dir == "R":
                    new_r, new_c, new_dir = go_down(card_dirs, r, c)
                elif dir == "L":
                    new_r, new_c, new_dir = go_up(card_dirs, r, c)
                elif dir == "U":
                    new_r, new_c, new_dir = go_left(card_dirs, r, c)
                elif dir == "D":
                    new_r, new_c, new_dir = go_right(card_dirs, r, c)
                q.append((new_r, new_c, new_dir))
            elif input[r][c] == "-":
                grid[r][c] = "-"
                visited.add((r, c, dir))
                if dir == "R" or dir == "L":
                    new_r, new_c = r + card_dirs[dir][0], c + card_dirs[dir][1]
                    if (new_r, new_c, dir) not in visited:
                        q.append((new_r, new_c, dir))
                elif dir == "D" or dir == "U":
                    new_dir = "L"
                    new_r, new_c = r + card_dirs[new_dir][0], c + card_dirs[new_dir][1]
                    if (new_r, new_c, new_dir) in visited:
                        pass
                    else:
                        if (new_r, new_c, new_dir) not in q:
                            q.append((new_r, new_c, new_dir))
                    second_dir = "R"
                    new_r, new_c = r + card_dirs[second_dir][0], c + card_dirs[second_dir][1]
                    if (new_r, new_c, second_dir) in visited:
                        pass
                    else:
                        if (new_r, new_c, second_dir) not in q:
                            q.append((new_r, new_c, second_dir))
            elif input[r][c] == "|":
                grid[r][c] = "|"
                visited.add((r, c, dir))
                if dir == "D" or dir == "U":
                    new_r, new_c = r + card_dirs[dir][0], c + card_dirs[dir][1]
                    if (new_r, new_c, dir) not in visited:
                        q.append((new_r, new_c, dir))
                elif dir == "R" or dir == "L":
                    new_dir = "U"
                    new_r, new_c = r + card_dirs[new_dir][0], c + card_dirs[new_dir][1]
                    if (new_r, new_c, new_dir) in visited:
                        pass
                    else:
                        if (new_r, new_c, new_dir) not in q:
                            q.append((new_r, new_c, new_dir))
                    second_dir = "D"
                    new_r, new_c = r + card_dirs[second_dir][0], c + card_dirs[second_dir][1]
                    if (new_r, new_c, second_dir) in visited:
                        pass
                    else:
                        if (new_r, new_c, second_dir) not in q:
                            q.append((new_r, new_c, second_dir))
    distinct_visits = set()
    for a,b,_ in visited:
        distinct_visits.add((a,b))
    return len(distinct_visits)
            
def go_left(card_dirs, r, c):
    new_r, new_c = r + card_dirs["L"][0], c + card_dirs["L"][1]
    new_dir = "L"
    return new_r,new_c,new_dir

def go_right(card_dirs, r, c):
    new_r, new_c = r + card_dirs["R"][0], c + card_dirs["R"][1]
    new_dir = "R"
    return new_r, new_c, new_dir

def go_down(card_dirs, r, c):
    new_r, new_c = r + card_dirs["D"][0], c + card_dirs["D"][1]
    new_dir = "D"
    return new_r, new_c, new_dir

def go_up(card_dirs, r, c):
    new_r, new_c = r + card_dirs["U"][0], c + card_dirs["U"][1]
    new_dir = "U"   
    return new_r, new_c, new_dir

if __name__ == "__main__":
    input = open(sys.argv[1]).read().splitlines()
    print(f"Part 1 Number of Tiles Energized: {p1(0,0,'R')}")
    m, n = len(input), len(input[0])
    entry_points = []
    for r in range(m):
        if r == 0:
            entry_points.append((r, 0, "D"))
            entry_points.append((r, n - 1, "D"))
        entry_points.append((r, n - 1, "L"))
        entry_points.append((r, 0, "R"))
    for c in range(1, n):
        entry_points.append((0, c, "D"))
        entry_points.append((m - 1, c, "U"))

    biggest_val = 0
    for e_r, e_c, start_dir in tqdm(entry_points):
        biggest_val = max(biggest_val, p1(e_r, e_c, start_dir))
    print(f"Part 2 Max Number of Tiles Energized from a specific pt along the edge: {biggest_val}")