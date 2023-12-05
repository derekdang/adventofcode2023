# https://adventofcode.com/2023/day/5
import sys
from tqdm import tqdm

def p1():
    maps = input[1:]
    map_list = []
    for _ in range(len(maps)):
        map_list.append({})

    for ind, info in enumerate(maps):
        split = info.split("\n")
        curr_map = map_list[ind]
        for i in range(1, len(split)):
            line = split[i].split(" ")
            start = int(line[1])
            end = start + int(line[2]) - 1
            curr_map[(start,end)] = (int(line[0]), int(line[0]) + int(line[2]) - 1)
    seeds = input[0].split(":")[1].strip().split(" ")
    
    min_lo = sys.maxsize - 1
    for seed in seeds:
        val = int(seed)
        for map in map_list:
            for key in map:
                if key[0] <= val <= key[1]:
                    val = map[key][0] + (val - key[0])
                    break
            
        min_lo = min(min_lo, val)
    print(min_lo)

    min_val2 = sys.maxsize - 1
    min_seed = 0
    index = 0
    for i in range(4, 6, 2):
        start = int(seeds[i])
        end = start + int(seeds[i + 1])
        for j in tqdm(range(1_890_346_000, 1_893_460_732)):
            val = int(j)
            for ind,map in enumerate(map_list):
                for key in map:
                    if key[0] <= val <= key[1]:
                        val = map[key][0] + (val - key[0])
                        break
            if val < min_val2:
                min_seed = j
                min_val2 = val
                index = i
    print(index, min_seed, min_val2)

if __name__ == "__main__":
    input = open(sys.argv[1]).read().split("\n\n")
    p1()