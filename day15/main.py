# https://adventofcode.com/2023/day/15
import sys

def hash(s: str) -> int:
    code = 0
    for char in s:
        code += ord(char)
        code *= 17
        code = code % 256
    return code

def find(label: str, arr: list[(str, int)]) -> int:
    for i, (l, focal_len) in enumerate(arr):
        if l == label:
            return i
    return -1

def p1(input: str) -> int:
    arr = input.split(",")
    total = sum(hash(s) for s in arr)
    return total

def p2(input: str) -> int:
    arr = input.split(",")
    hash_map = {}
    box_label_map = {}
    score = 0
    for i in range(256):
        hash_map[i] = []
        box_label_map[i] = set()
    for s in arr:
        if "=" in s:
            label = s[:len(s) - 2]
            focal_len = int(s[s.index("=") + 1:])
            
            box_no = hash(label)
            if label in box_label_map[box_no]:
                box = hash_map[box_no]
                index = find(label, box)
                box.pop(index)
                box.insert(index, (label, focal_len))
            else:
                hash_map[box_no].append((label, focal_len))
                box_label_map[box_no].add(label)
        else:
            label = s[:len(s) - 1]
            box_no = hash(label)
            if label in box_label_map[box_no]:
                box = hash_map[box_no]
                index = find(label, box)
                box.pop(index)
                box_label_map[box_no].remove(label)

    for k, v_list in hash_map.items():
        for ind, item in enumerate(v_list):
            focal_length = item[1]
            score += (focal_length * (ind + 1) * (k + 1))
    return score
        
if __name__ == "__main__":
    input = open(sys.argv[1]).read()
    print(f"Part 1 sum of hash code of all input: {p1(input)}")
    print(f"Part 2 sum of k,v pairs in 'hash map' logic: {p2(input)}")