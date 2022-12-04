import re
INPUT_PATH = "4th\input.txt"

def part1(path_in):
    with open(path_in, "r") as input_file:
        fully_contained = 0
        for line in input_file.readlines():
            part1=line.split(",")[0];
            part2=line.split(",")[1];
            part1_1=int(part1.split("-")[0]);
            part1_2=int(part1.split("-")[1]);
            part2_1=int(part2.split("-")[0]);
            part2_2=int(part2.split("-")[1]);
            if (part1_1 <= part2_1 and part1_2 >= part2_2) or (part2_1 <= part1_1 and part2_2 >= part1_2):
                fully_contained += 1
    return fully_contained

def part2(path_in):
    with open(path_in, "r") as input_file:
        fully_contained = 0
        
        return fully_contained



if __name__ == "__main__":
    # Part One
    print(f"Assignment pairs which fully contains the other: {part1(INPUT_PATH)}")

    # Part Two
    print(f"TBRead: {part2(INPUT_PATH)}")
