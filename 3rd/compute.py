import re
INPUT_PATH = "3rd\input.txt"

def part1(path_in):
    lower_case=[];
    upper_case=[];
    for i in range(26):
        lower_case.append(chr(97+i));
        upper_case.append(chr(65+i));
    # print(lower_case);
    # print(upper_case);
    with open(path_in, "r") as input_file:
        sum = 0
        for line in input_file.readlines():
            length_line = len(str(line.strip()))
            #print(length_line)
            
            if length_line%2 == 0:
                part1 = slice(0,length_line//2)
                part2 = slice(length_line//2,length_line)
                #print(''.join(sorted(set.intersection(set(str(line.strip())[part1]),set(str(line.strip())[part2])))));
                if ''.join(sorted(set.intersection(set(str(line.strip())[part1]),set(str(line.strip())[part2])))) in lower_case:
                    sum += lower_case.index(''.join(sorted(set.intersection(set(str(line.strip())[part1]),set(str(line.strip())[part2])))))+1
                if ''.join(sorted(set.intersection(set(str(line.strip())[part1]),set(str(line.strip())[part2])))) in upper_case:
                    sum += upper_case.index(''.join(sorted(set.intersection(set(str(line.strip())[part1]),set(str(line.strip())[part2])))))+26+1
                #print("First Half of String:",str(line.strip())[part1])
                #print("Second Half of String:",str(line.strip())[part2])
            else:
                part1 = slice(0,length_line//2)
                part2 = slice(length_line//2,length_line)
                #print(''.join(sorted(set.intersection(set(str(line.strip())[part1]),set(str(line.strip())[part2])))));
                if ''.join(sorted(set.intersection(set(str(line.strip())[part1]),set(str(line.strip())[part2])))) in lower_case:
                    sum += lower_case.index(''.join(sorted(set.intersection(set(str(line.strip())[part1]),set(str(line.strip())[part2])))))+1
                if ''.join(sorted(set.intersection(set(str(line.strip())[part1]),set(str(line.strip())[part2])))) in upper_case:
                    sum += upper_case.index(''.join(sorted(set.intersection(set(str(line.strip())[part1]),set(str(line.strip())[part2])))))+26+1
                #print("First Half of String:",str(line.strip())[part1])
                #print("Second Half of String:",str(line.strip())[part2])

        return sum



if __name__ == "__main__":
    sum_priorities = part1(INPUT_PATH)
    # Part One
    print(f"Sum of priorities: {sum_priorities}")