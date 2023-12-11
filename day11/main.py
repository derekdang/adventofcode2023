# https://adventofcode.com/2023/day/11
import sys

def p1(EXPANSION_RANGE: int):
    galaxy_set = set()
    m = len(input)
    n = len(input[0])
    for i, row in enumerate(input):
        for j, col in enumerate(row):
            if input[i][j] == "#":
                galaxy_set.add((i,j))
    rows_to_add = []
    for i in range(m):
        is_empty = True
        for coords in galaxy_set:
            r = coords[0]
            if r == i:
                is_empty = False
                break
        if is_empty:
            rows_to_add.append(i)
    
    cols_to_add = []
    for j in range(n):
        is_empty = True
        for coords in galaxy_set:
            c = coords[1]
            if j == c:
                is_empty = False
                break
        if is_empty:
            cols_to_add.append(j)

    new_map = []
    for i, row in enumerate(input):
        new_map.append(list(row))
        if i in rows_to_add:
            for _ in range(EXPANSION_RANGE):
                arr = ["."] * n
                new_map.append(arr)
    
    offset = 0
    for new_c in cols_to_add:
        for row in new_map:
            for y in range(EXPANSION_RANGE):
                row.insert(new_c + y + offset, ".")
        offset += EXPANSION_RANGE

    # for row in new_map:
    #     print("".join(row))
    
    new_map_coords = []
    for i, row in enumerate(new_map):
        for j, col in enumerate(row):
            if new_map[i][j] == "#":
                new_map_coords.append((i,j))
    
    sum_of_dist_of_all_pairs = 0
    for k, start_coord in enumerate(new_map_coords):
        for l in range(k + 1, len(new_map_coords)):
            other_coord = new_map_coords[l]
            sum_of_dist_of_all_pairs += abs(start_coord[0] - other_coord[0]) + abs(start_coord[1] - other_coord[1])
    return sum_of_dist_of_all_pairs

if __name__ == "__main__":
    input = open(sys.argv[1]).read().splitlines()
    sum_length = 0
    for i in range(1, 2):
        sum_length = p1(i)
    dist_added_with_each_expansion = p1(2) - sum_length # 447_064 for my puzzle input
    print(f"Part 1 Sum of dist b/t all pairs empty row/col expand once {sum_length}")
    for i in range(2, 1_000_000):
        sum_length += dist_added_with_each_expansion
    print(f"Part 2: Sum of dist after 1_000_000 expansions {sum_length}")