INPUT_PATH = "2nd\input.txt"

def part1(path_in):
    with open(path_in, "r") as input_file:
        points = 0
        for line in input_file.readlines():
            if str(line.strip()) == "A X" or str(line.strip()) == "A X ":
                points += 4
            if str(line.strip()) == "A Y" or str(line.strip()) == "A Y ":
                points += 8
            if str(line.strip()) == "A Z" or str(line.strip()) == "A Z ":
                points += 3
            if str(line.strip()) == "B X" or str(line.strip()) == "B X ":
                points += 1
            if str(line.strip()) == "B Y" or str(line.strip()) == "B Y ":
                points += 5
            if str(line.strip()) == "B Z" or str(line.strip()) == "B Z ":
                points += 9
            if str(line.strip()) == "C X" or str(line.strip()) == "C X ":
                points += 7
            if str(line.strip()) == "C Y" or str(line.strip()) == "C Y ":
                points += 2
            if str(line.strip()) == "C Z" or str(line.strip()) == "C Z ":
                points += 6
    return points


def part2(path_in):
    with open(path_in, "r") as input_file:
        points = 0
        for line in input_file.readlines():
            if str(line.strip()) == "A X" or str(line.strip()) == "A X ":
                points += 4
            if str(line.strip()) == "A Y" or str(line.strip()) == "A Y ":
                points += 8
            if str(line.strip()) == "A Z" or str(line.strip()) == "A Z ":
                points += 3
            if str(line.strip()) == "B X" or str(line.strip()) == "B X ":
                points += 1
            if str(line.strip()) == "B Y" or str(line.strip()) == "B Y ":
                points += 5
            if str(line.strip()) == "B Z" or str(line.strip()) == "B Z ":
                points += 9
            if str(line.strip()) == "C X" or str(line.strip()) == "C X ":
                points += 7
            if str(line.strip()) == "C Y" or str(line.strip()) == "C Y ":
                points += 2
            if str(line.strip()) == "C Z" or str(line.strip()) == "C Z ":
                points += 6
    return points



if __name__ == "__main__":
    game_score = part1(INPUT_PATH)
    # Part One
    print(f"Total points: {game_score}")
