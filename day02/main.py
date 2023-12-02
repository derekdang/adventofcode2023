# https://adventofcode.com/2023/day/2
import sys

def p1p2(input: list[str]) -> (int, int):
    RED_LIM, GREEN_LIM, BLUE_LIM = 12, 13, 14
    score = 0
    multi_score = 0
    for line in input:
        is_valid = True
        split = line.split(":")
        cube_sets = split[1].split(";")
        max_r, max_g, max_b = 0, 0, 0
        for a in cube_sets:
            counts = a.split(",")
            red_c, green_c, blue_c = 0, 0, 0
            
            for cube in counts:
                cube = cube.strip()
                if "red" in cube:
                    red_c = int(cube.split(" ")[0])
                    max_r = max(max_r, red_c)
                elif "blue" in cube:
                    blue_c = int(cube.split(" ")[0])
                    max_b = max(max_b, blue_c)
                elif "green" in cube:
                    green_c = int(cube.split(" ")[0])
                    max_g = max(max_g, green_c)
            if red_c > RED_LIM or blue_c > BLUE_LIM or green_c > GREEN_LIM:
                is_valid = False
        
        multi_score += (max_g * max_b * max_r)
        game_no = split[0].split(" ")[1]
        if is_valid:
            score += int(game_no)
    return score, multi_score

if __name__ == "__main__":
    input = open(sys.argv[1]).read().splitlines()
    ans_p1, ans_p2 = p1p2(input)
    print(f"{ans_p1}")
    print(f"{ans_p2}")