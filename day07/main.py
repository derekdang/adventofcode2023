# https://adventofcode.com/2023/day/7
import sys
import functools

def compareP2(a: str, b: str) -> int:
    score = {"A": 13, "K": 12, "Q": 11, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3":3, "2": 2, "J": 1}
    for a_char, b_char in zip(a,b):
        a_score, b_score = score[a_char], score[b_char]
        if a_score < b_score:
            return -1
        elif a_score > b_score:
            return 1
    return 0

def compareP1(a: str, b: str) -> int:
    score = {"A": 13, "K": 12, "Q": 11, "J": 10.5, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3":3, "2": 2}
    for a_char, b_char in zip(a,b):
        a_score, b_score = score[a_char], score[b_char]
        if a_score < b_score:
            return -1
        elif a_score > b_score:
            return 1
    return 0

def sort_into_bucket(hand: str,
                     card_count: dict(),
                     highcards: list[str], 
                     onepair: list[str], 
                     twopairs: list[str], 
                     threeofakinds: list[str], 
                     fullhouses: list[str], 
                     fourofakinds: list[str], 
                     fiveofakinds: list[str]):
    if len(card_count) == 1:
        fiveofakinds.append(hand)
    elif len(card_count) == 2:
        for _, num in card_count.items():
            if num == 1 or num == 4:
                fourofakinds.append(hand)
                break
            else:
                fullhouses.append(hand)
                break
    elif len(card_count) == 3:
        contains_three = False
        for _, num in card_count.items():
            if num == 3:
                contains_three = True
                break
        if contains_three:
            threeofakinds.append(hand)
        else:
            twopairs.append(hand)
    elif len(card_count) == 4:
        onepair.append(hand)
    else:
        highcards.append(hand)

def count_chars(hand: str) -> dict():
    char_count = {}
    for char in hand:
        if char not in char_count:
            char_count[char] = 0
        char_count[char] = char_count[char] + 1
    return char_count

ordering = ["A","K","Q","T"]
for i in reversed(range(2,10)):
    ordering.append(str(i))
ordering.append("J")

def make_strongest_hand(orginal_hand: str) -> str:
    permutations = set()
    permutations.add(orginal_hand)
    for i, char in enumerate(orginal_hand):
        if char == "J":
            to_add = set()
            for s in permutations:
                for c in ordering:
                    new_s = s[:i] + c + s[i + 1:]
                    to_add.add(new_s)
            for s in to_add:
                permutations.add(s)
        else:
            continue
    sorted_permutations = sorted(list(permutations), key=functools.cmp_to_key(compareP2))
    highcards, onepair, twopairs, threeofakinds, fullhouses, fourofakinds, fiveofakinds = [],[],[],[],[],[],[]
    scoring = [highcards, onepair, twopairs, threeofakinds, fullhouses, fourofakinds, fiveofakinds]
    for new_hand in sorted_permutations:
        h_count = count_chars(new_hand)
        sort_into_bucket(new_hand, h_count, highcards, onepair, twopairs, threeofakinds, fullhouses, fourofakinds, fiveofakinds)
    for hand_type in reversed(scoring):
        if len(hand_type) > 0:
            sorted_hand_type = sorted(hand_type, key=functools.cmp_to_key(compareP2))
            return sorted_hand_type[len(sorted_hand_type) - 1]
        
def p1():
    hands = {}
    highcards, onepair, twopairs, threeofakinds, fullhouses, fourofakinds, fiveofakinds = [],[],[],[],[],[],[]
    scoring = [highcards, onepair, twopairs, threeofakinds, fullhouses, fourofakinds, fiveofakinds]
    for line in input:
        hand, bid = line.split(" ")
        hands[hand] = int(bid)
        h_count = count_chars(hand)
        sort_into_bucket(hand, h_count, highcards, onepair, twopairs, threeofakinds, fullhouses, fourofakinds, fiveofakinds)   

    hand_no = 1
    score = 0
    for hand_type in scoring:
        sorted_hand_type = sorted(hand_type, key=functools.cmp_to_key(compareP1))
        for hand in sorted_hand_type:
            score += hand_no * hands[hand]
            hand_no += 1
    return score

def p2():
    hands = {}
    highcards, onepair, twopairs, threeofakinds, fullhouses, fourofakinds, fiveofakinds = [],[],[],[],[],[],[]
    scoring = [highcards, onepair, twopairs, threeofakinds, fullhouses, fourofakinds, fiveofakinds]
    for line in input:
        hand, bid = line.split(" ")
        hands[hand] = int(bid)
        
        h_count = count_chars(hand)
        if "J" in h_count:
            j_hand = make_strongest_hand(hand)
            h_count = count_chars(j_hand)
        sort_into_bucket(hand, h_count, highcards, onepair, twopairs, threeofakinds, fullhouses, fourofakinds, fiveofakinds)

    hand_no = 1
    score = 0
    for hand_type in scoring:
        sorted_hand_type = sorted(hand_type, key=functools.cmp_to_key(compareP2))
        for hand in sorted_hand_type:
            score += hand_no * hands[hand]
            hand_no += 1
    return score

if __name__ == "__main__":
    input = open(sys.argv[1]).read().splitlines()
    print(f"Part 1 Winnings with standard scoring: {p1()}")
    print(f"Part 2 Winnings with wildcard scoring: {p2()}")