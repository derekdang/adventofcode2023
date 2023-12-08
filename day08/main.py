# https://adventofcode.com/2023/day/8
import sys
from math import lcm
instr = "LRLRRRLRRRLLLRLRRLLRLRRRLRLRRRLRLRRRLRLRRRLRRRLRLLRRRLRLRLRRLRRLRLRRLRRLRRLLRRRLRRRLRRLRRLRRLRRRLLRRLRLRRLRLRRLRRLRLRRLRRLLRLRRRLRRLRRRLLRLRLRLLRLLRLLRLRRLLRRLRLRLRRLRLLRRRLLRRRLRRLLRRRLRRRLRLRRRLLRRRLRLRRRLLLRRRLRLRLRRRLRRRLRRRLRLRRLLLRRLRRRLLRLRRRLRLRLLLRRLRLRRRLRLRRRR"
def p1(mapping: dict(), instr: str, s: str) -> int:
    index, n = 0, len(instr)
    while s != "ZZZ":
        if index >= n:
            char = instr[index % n]
        else:
            char = instr[index]
        if char == "L":
            s = mapping[s][0]
        else:
            s = mapping[s][1]
        index+= 1
    return index

def p2(mapping: dict(), instr: str):
    n = len(instr)
    strings = []
    for key in mapping:
        if key[2] == "A":
            strings.append(key)
    index = 0
    tmp = [21409, 14363, 15989, 16531, 19241, 19783]
    last_seen_z = [0] * len(strings)
    while True:
        for i, z_string in enumerate(strings):
            if z_string[2] == "Z":
                if last_seen_z[i] == 0:
                    last_seen_z[i] = index
        all_seen_z = True

        for num in last_seen_z:
            if num == 0:
                all_seen_z = False
        if all_seen_z:
            return lcm(*last_seen_z)

        if index >= n:
            char = instr[index % n]
        else:
            char = instr[index]
        new_strings = []
        for new_string in strings:
            if char == "L":
                new_strings.append(mapping[new_string][0])
            else:
                new_strings.append(mapping[new_string][1])
        strings = new_strings
        index += 1

if __name__ == "__main__":
    input = open(sys.argv[1]).read().splitlines()
    mapping = {}
    for line in input:
        key, value = line.split(" =")
        l,r = value.split(", ")
        mapping[key] = l[2:],r[:len(r)-1]
    print(f"Part 1 to get from AAA to ZZZ is {p1(mapping, instr, 'AAA')} steps")
    print(f"Part 2 keys that end in A to simultaneously all end in Z is {p2(mapping, instr)} steps")