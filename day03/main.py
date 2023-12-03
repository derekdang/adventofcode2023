# https://adventofcode.com/2023/day/3
import sys

def is_part_number(r: int, start: int, end: int) -> bool:
    for c in range(start,end):
        for i,j in dirs:
            if r+i < 0 or r+i >= len(input) or c+j < 0 or c+j >= len(input[r]):
                continue
            else:
                if not input[r+i][c+j].isdigit() and input[r+i][c+j] != '.':
                    return True
    return False

def find_start_and_end_for_num(row: int, left: int, right: int) -> (int, int):
    while left > 0 and input[row][left-1].isdigit():
        left -= 1
    while right < len(input[row]) and input[row][right].isdigit():
        right +=1
    return left, right

def p1(input: list[str]) -> int:
    sum = 0
    for r, line in enumerate(input):
        c = 0
        while c < len(line): 
            if line[c].isdigit():
                start = c
                end = start
                while end < len(line) and line[end].isdigit():
                    end += 1
                if is_part_number(r, start, end):
                    sum += int(line[start:end])
                    c = end
            c += 1
    return sum
                
def p2(input: list[str]) -> int:
    gear_sum = 0
    nums_included = {}
    for r, line in enumerate(input):
        for c, ch in enumerate(line):
            if ch == "*":
                neighbors = []
                for i,j in dirs:
                    if r+i < 0 or r+i >= len(input) or c+j < 0 or c+j >= len(input[r]):
                        continue
                    if input[r+i][c+j].isdigit():
                        row = r+i
                        start, end = c+j, c+j
                        start, end = find_start_and_end_for_num(row, start, end)
            
                        num = int(input[row][start:end])
                        if row not in nums_included:
                            nums_included[row] = []
                        if (start,end) not in nums_included[row]:
                            neighbors.append(int(num))
                            nums_included[row].append((start,end))
            
                if len(neighbors) >= 2:
                    product = 1
                    for n in neighbors:
                        product *= n
                    gear_sum += product
    return gear_sum

if __name__ == "__main__":
    input = open(sys.argv[1]).read().splitlines()
    dirs = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
    print(f"Part 1 Sum of all part scores: {p1(input)}")
    print(f"Part 2 Sum of all gear scores: {p2(input)}")