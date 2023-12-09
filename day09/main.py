# https://adventofcode.com/2023/day/9
import sys

def find_sub_levels(level: list[int], sublevel_arr: list[list[int]]):
    sublevel_arr.append(level)
    curr_level = level
    while not all_zeros(curr_level):
        next_level = []
        for i in range(1, len(curr_level)):
            next_level.append(curr_level[i] - curr_level[i-1])
        sublevel_arr.append(next_level)
        curr_level = next_level
        
def all_zeros(l: list[int]) -> bool:
    return all(i == 0 for i in l)

def find_history(l: list[list[int]]) -> int:
    rev = list(reversed(l))
    j = 0
    while j < len(rev) - 1:
        bot = rev[j]
        top = rev[j + 1]
        last_elem, last_elem_top = bot[len(bot) - 1], top[len(top) - 1]
        x = last_elem + last_elem_top
        top.append(x)
        j += 1

    top = rev[len(rev) - 1]
    return top[len(top) - 1]

def find_f_history(l: list[list[int]]) -> int:
    rev = list(reversed(l))
    j = 0
    while j < len(rev) - 1:
        bot = rev[j]
        top = rev[j + 1]
        first_elem, first_elem_top = bot[0], top[0]
        x = first_elem_top - first_elem
        top.insert(0,x)
        j += 1 
    top = rev[len(rev) - 1]
    return top[0]

def p1(arr: list[list[int]]) -> int:
    history = 0
    for level in arr:
        sub_levels = []
        find_sub_levels(level, sub_levels)
        history += find_history(sub_levels)
    return history

def p2(arr: list[list[int]]) -> int:
    history = 0
    for level in arr:
        sub_levels = []
        find_sub_levels(level, sub_levels)
        history += find_f_history(sub_levels)
    return history

if __name__ == "__main__":
    input = open(sys.argv[1]).read().splitlines()
    arr = []
    for level, line in enumerate(input):
        arr.append([])
        for n in line.split(" "):
            arr[level].append(int(n))
    print(f"Part 1 with history looking at last element {p1(arr)}")
    print(f"Part 2 with history looking at first element {p2(arr)}")