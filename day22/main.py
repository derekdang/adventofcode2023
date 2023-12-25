# https://adventofcode.com/day/22
import sys
from tqdm import tqdm

# simulate falls from first to end
# then calculate which supports which from top to bot
def p1():
    for block in blocks:
        print(block)

if __name__ == "__main__":
    input = open(sys.argv[1]).read().splitlines()
    blocks = []
    for line in input:
        b1,b2 = line.split("~")
        b1_arr = [int(x) for x in b1.split(",")]
        b2_arr = [int(x) for x in b2.split(",")]
        blocks.append([b1_arr,b2_arr])
    blocks = sorted(blocks, key= lambda x: x[1][2])
    p1()