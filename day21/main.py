# https://adventofcode.com/2023/day/21
import sys
from tqdm import tqdm

def p1(NUM_STEPS: int) -> int:
    visited = set()
    q = []
    m = len(input)
    n = len(input[0])
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    for r,line in enumerate(input):
        for c,_ in enumerate(line):
            if input[r][c] == "S":
                q.append((r,c))
    
    
    for i in range(NUM_STEPS):
        to_visit = set()
        for cr,cc in q:
            visited.add((cr,cc))
            for dir in dirs:
                nr = cr + dir[0] 
                nc = cc + dir[1]
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue
                if (input[nr][nc] == "." or input[nr][nc] == "S") and (nr,nc) not in to_visit:
                    to_visit.add((nr,nc))
        q = []
        q.extend(to_visit)
    return len(q)

if __name__ == "__main__":
    input = open(sys.argv[1]).read().splitlines()
    NUM_STEPS = 64
    print(f"Part 1 Num of cells elf can be on after {NUM_STEPS} steps: {p1(NUM_STEPS)}")