# https://adventofcode.com/2023/day/1
import sys

def p1(input: list[str]) -> int:
    sum = 0
    for line in input:
        first_num, second_num = "", ""
        for char in line:
            if char.isdigit():
                first_num = char
                break
        for char in reversed(line):
            if char.isdigit():
                second_num = char
                break
        num = first_num + second_num
        sum += int(num)
    return sum

def p2(input: list[str]) -> int:
    sum = 0
    for line in input:
        first_num, second_num = "", ""
        index_one, index_two = 0, 0
        for i,char in enumerate(line):
            if char.isdigit():
                index_one = i
                first_num = char
                break
        for i,char in enumerate(reversed(line)):
            if char.isdigit():
                index_two = len(line)-i-1
                second_num = char
                break

        for key in map:
            if key in line:
                if line.find(key) < index_one:
                    index_one = line.find(key)
                    first_num = map[key]
        for key in map:
            if key in line:
                if line.rfind(key) > index_two:
                    index_two = line.rfind(key)
                    second_num = map[key]
        num = first_num + second_num
        sum += int(num)
    return sum

        
if __name__ == "__main__":
    input = open(sys.argv[1]).read().splitlines()
    map = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven": "7", "eight": "8", "nine": "9"}
    print(f"Part 1 sum of all values: {p1(input)}")
    print(f"Part 2 sum of all values with words: {p2(input)}")