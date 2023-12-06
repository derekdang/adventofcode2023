# https://adventofcode.com/2023/day/6
from tqdm import tqdm

sample = [7, 15, 30]
sample_dist = [9, 40, 200]
input = [62, 73, 75, 65]
input_dist = [644, 1023, 1240, 1023]

USE_SAMPLE = False
t_arr = sample if USE_SAMPLE else input
d_arr = sample_dist if USE_SAMPLE else input_dist
def p1(t_arr: list[int], d_arr: list[int]) -> int:
    score = 1
    for t,d in zip(t_arr, d_arr):
        num_ways_to_win = 0
        for i in range(0, t):
            velocity = i
            time_rem = t - i
            dist_traveled = time_rem * velocity
            if dist_traveled > d:
                num_ways_to_win += 1
        score *= num_ways_to_win
    return score

def p2(time: int, dist_to_beat: int) -> int:
    p2_count = 0
    for i in tqdm(range(0, time)):
        velocity = i
        time_rem = time - i
        dist_traveled = time_rem * velocity
        if dist_traveled > dist_to_beat:
            p2_count += 1
    return p2_count

if __name__ == "__main__":
    print(f"{p1(t_arr, d_arr)}")
    print(f"{p2(62737565, 644102312401023)}")