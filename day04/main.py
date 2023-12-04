# https://adventofcode.com/2023/day/4
import sys

def p1p2(input: list[str]) -> (int, int):
    total_pts = 0
    total_cards = 0
    extra_copies = {}
    for line in input:
        count = 0
        nums = line.split(':')
        card_no = int(nums[0].split('Card')[1])
        winning, my_nums = nums[1].split('|')
        winning_set = set()
        for num in winning.split(' '):
            if num == "":
                continue
            winning_set.add(int(num))
        
        for n in my_nums.split(' '):
            if n == "":
                continue
            if int(n) in winning_set:
                count += 1
        if count > 0:
            total_pts += pow(2, count - 1)
        num_copies = extra_copies[card_no] if card_no in extra_copies else 0
        
        total_cards += num_copies + 1
        for j in range(card_no + 1, card_no + count + 1):
            if j not in extra_copies:
                extra_copies[j] = 0
            extra_copies[j] += num_copies + 1
    return total_pts, total_cards
        
if __name__ == "__main__":
    input = open(sys.argv[1]).read().splitlines()
    ans_p1, ans_p2 = p1p2(input)
    print(f"Part 1 Total score for all cards: {ans_p1}")
    print(f"Part 2 Total number of cards processed: {ans_p2}")