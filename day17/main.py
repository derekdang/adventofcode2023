# https://adventofcode.com/2023/day/17
import sys
from tqdm import tqdm

class Step:
    def __init__(self, dir, num_steps, r, c, heat_loss):
        self.dir = dir
        self.num_steps = num_steps
        self.r = r
        self.c = c
        self.heat_loss = heat_loss
    
dirs = [(1, 0), (-1, 0), [0, 1], [0, -1]]
cardinal_l = ["D", "U", "R", "L"]
# dfs or bfs?
# don't add to queue if prev steps taken were of same dir
def p1():
    m, n = len(input), len(input[0])
    visited = {} # map keeping track of min val of heat incurred to get to point[r][c]
    for i in range(m):
        for j in range(n):
            visited[(i, j)] = sys.maxsize - 1
    visited[(0, 0)] = 0
    q = [Step("D", num_steps=1, r=1, c=0, heat_loss=int(input[1][0])), Step("R", num_steps=1, r=0, c=1, heat_loss=int(input[0][1]))]
    while len(q) != 0:
        size = len(q)
        for _ in range(size):
            s = q.pop(0)
            curr_point = (s.r, s.c)
            print(s.dir, s.num_steps, s.r, s.c, s.heat_loss)
            visited[curr_point] = min(s.heat_loss, visited[curr_point])
            if curr_point == (m - 1, n - 1):
                print(f"END HEAT LOSS:  {s.heat_loss}")
                print(f"END HEAT LOSS:  {s.heat_loss}")
                print(f"END HEAT LOSS:  {s.heat_loss}")
            for d_arr, ch in zip(dirs, cardinal_l):
                if d_arr == s.dir and s.num_steps == 4:
                    continue
                if s.dir == "D" and ch == "U":
                    continue
                if s.dir == "R" and ch == "L":
                    continue
                if s.dir == "U" and ch == "D":
                    continue
                if s.dir == "L" and ch == "R":
                    continue

                next_r, next_c = s.r + d_arr[0], s.c + d_arr[1]
                if next_r >= 0 and next_r < m and next_c >= 0 and next_c < n:
                    # print(visited[(next_r, next_c)])
                    next_incurred_hl = int(input[next_r][next_c])
                    if visited[(next_r, next_c)] < next_incurred_hl + s.heat_loss:
                        continue 
                    else:
                        if ch == s.dir:
                            num_steps = s.num_steps
                        else:
                            num_steps = 0
                        if num_steps + 1 > 4:
                            continue
                        q.append(Step(ch, num_steps + 1, next_r, next_c, s.heat_loss + next_incurred_hl))
                
    print(visited[m - 1][n - 1])


if __name__ == "__main__":
    input = open(sys.argv[1]).read().splitlines()
    p1()