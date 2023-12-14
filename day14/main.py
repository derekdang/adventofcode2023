# https://adventofcode.com/day/14
import sys
from tqdm import tqdm

def fall_north(grid: list[list[str]]) -> list[list[str]]:
    m = len(grid)
    n = len(grid[0])
    new_grid = [['.' for x in range (n)] for y in range(m)]
    for c in range(n):
        mapping = {}
        num_round_rocks = 0
        for r in range(m):
            if grid[r][c] == "O":
                num_round_rocks += 1
            elif grid[r][c] == "#":
                mapping[r] = num_round_rocks
                num_round_rocks = 0

        indices = sorted(list(mapping.keys()))
        for i in indices:
            new_grid[i][c] = "#"
        
        prev_stopped = 0
        for i in indices:
            num_rocks_to_write = mapping[i]
            for j in range(prev_stopped, prev_stopped + num_rocks_to_write):
                new_grid[j][c] = "O"
            prev_stopped = i + 1
        if num_round_rocks != 0:
            for j in range(prev_stopped, num_round_rocks + prev_stopped):
                new_grid[j][c] = "O"
    return new_grid

def p1(grid: list[list[str]]) -> int:
    new_grid = fall_north(grid)
    m, n = len(grid), len(grid[0])
    weight_score = 0 
    for r in range(m):
        for c in range(n):
            if new_grid[r][c] == "O":
                weight_score += m - r
    return weight_score

def p2(grid: list[list[str]]) -> int:
    rotated = grid
    weight_score = 0
    seen = {}
    for i in tqdm(range(145)):
        for _ in range(4): # Tilt it in the 4 cardinal directions by rotating 90° and tilt north because it is a square matrix
            new_grid = fall_north(rotated)
            rotated = [list(a) for a in zip(*new_grid[::-1])]
            
        s = ""
        for line in rotated:
            s += "".join(line)
        
        if s in seen:
            # prev = seen[s]
            seen[s] = i
            # print(f"{i} grid seen at {prev}")
            if i % 11 == 9: # My cycle is 11
                weight_score = 0
                m, n = len(rotated), len(rotated[0])
                for r in range(m):
                    for c in range(n):
                        if rotated[r][c] == "O":
                            weight_score += m - r
        else:
            seen[s] = i
    return weight_score

if __name__ == "__main__":
    input = open(sys.argv[1]).read().splitlines()
    print(f"Part 1 Weight Score After 'tilting' the grid north: {p1(input)}")
    print(f"Part 2 Weight Score After 1_000_000_000 cycles: {p2(input)}")