# https://adventofcode.com/2023/day/12
import sys
from tqdm import tqdm
def p1():
    total = 0
    for ind, line in enumerate(input):
        config, arrangement = line.split()
        arrangement = arrangement.split(',')
        arrangement = [int(x) for x in arrangement]

        ## make all permutations 
        ## split by "."
        ## see if size matches for each element zipped?
        num_hash, num_unknown = 0, 0
        for char in config:
            if char == "#":
                num_hash += 1
            elif char == "?":
                num_unknown += 1
        start = [""]
        for x in config:
            new_start = []
            for s in tqdm(start):
                if x == "?":
                    new_start.append(s + "#")
                    new_start.append(s + ".")
                else:
                    new_start.append(s + x)
            start = new_start

        num_arrangements = 0
        for s in start:
            arr = s.split(".")
            while '' in arr:
                arr.remove('')
            if len(arr) != len(arrangement):
                continue
            is_valid = True
            for i,j in zip(arr, arrangement):
                if len(i) != j:
                    is_valid = False
                    break
            if is_valid:
                num_arrangements += 1
        total += num_arrangements
    print(total)

    start = [""]
    for x in config:
        new_start = []
        for s in tqdm(start):
            if x == "?":
                new_start.append(s + "#")
                new_start.append(s + ".")
            else:
                new_start.append(s + x)
        start = new_start
            # arr = list(filter(lambda x: x == "", arr))
            
if __name__ == "__main__":
    input = open(sys.argv[1]).read().splitlines()
    p1()