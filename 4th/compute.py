import re
INPUT_PATH = "4th\input.txt"

def part1(path_in):
    with open(path_in, "r") as input_file:
        fully_contained = 0
        for line in input_file.readlines():
            part1_1=int(line.split(",")[0].split("-")[0]);
            part1_2=int(line.split(",")[0].split("-")[1]);
            part2_1=int(line.split(",")[1].split("-")[0]);
            part2_2=int(line.split(",")[1].split("-")[1]);

            if (part1_1 <= part2_1 and part1_2 >= part2_2) or (part2_1 <= part1_1 and part2_2 >= part1_2):
                fully_contained += 1
    return fully_contained

def part2(path_in):
    with open(path_in, "r") as input_file:
        pairs_overlap = 0
        for line in input_file.readlines():
            part1_1=int(line.split(",")[0].split("-")[0]);
            part1_2=int(line.split(",")[0].split("-")[1]);
            part2_1=int(line.split(",")[1].split("-")[0]);
            part2_2=int(line.split(",")[1].split("-")[1]);

            if not (int(line.split(",")[0].split("-")[1]) < int(line.split(",")[1].split("-")[0]) or int(line.split(",")[0].split("-")[0]) > int(line.split(",")[1].split("-")[1])):
                pairs_overlap += 1
        return pairs_overlap


if __name__ == "__main__":
    # Part One
    print(f"Assignment pairs which fully contains the other: {part1(INPUT_PATH)}")

    # Part Two
    print(f"Number of Overlaps: {part2(INPUT_PATH)}")
