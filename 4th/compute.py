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
        file = open("4th\output.txt", "a")
        for line in input_file.readlines():
            part1_1=int(line.split(",")[0].split("-")[0]);
            part1_2=int(line.split(",")[0].split("-")[1]);
            part2_1=int(line.split(",")[1].split("-")[0]);
            part2_2=int(line.split(",")[1].split("-")[1]);

            if (part1_1 <= part2_1 and part1_2 >= part2_2) or (part2_1 <= part1_1 and part2_2 >= part1_2):
                file.write(line);
        file.close()
        file=open("4th\output.txt", "r").readlines()
        file.sort()
        print(file)
        i = 0
        
        # while i < len(file):
        #     if ''.join(sorted(set(str(file[i].strip())).intersection(set(str(file[i+1].strip()))).intersection(set(str(file[i+2].strip()))))) in lower_case: #join will convert the list to a string and sorted will sort the string, intersection will find the common elements between the three sets
        #         sum += lower_case.index(''.join(sorted(set(str(file[i].strip())).intersection(set(str(file[i+1].strip()))).intersection(set(str(file[i+2].strip()))))))+1 #+1 is the start for the lower case letters value in the problem
        #     if ''.join(sorted(set(str(file[i].strip())).intersection(str(file[i+1].strip()),str(file[i+2].strip())))) in upper_case: #join will convert the list to a string and sorted will sort the string, intersection will find the common elements between the three sets
        #         sum += upper_case.index(''.join(sorted(set(str(file[i].strip())).intersection(set(str(file[i+1].strip()))).intersection(set(str(file[i+2].strip()))))))+26+1 #26+1 is the start for the higher case letters value in the problem
        #     i+=3
        # for line in input_file.readlines():
        #     part1_1=int(line.split(",")[0].split("-")[0]);
        #     part1_2=int(line.split(",")[0].split("-")[1]);
        #     part2_1=int(line.split(",")[1].split("-")[0]);
        #     part2_2=int(line.split(",")[1].split("-")[1]);
        
        while i < len(file):
            j = i;
            while j < len(file):
                if (file[i].split(",")[0].split("-")[0] <= file[j].split(",")[0].split("-")[0] and (file[i].split(",")[0].split("-")[1] <= file[j].split(",")[1].split("-")[1] or file[i].split(",")[0].split("-")[1] <= file[j].split(",")[1].split("-")[1])) or (file[i].split(",")[0].split("-")[0] >= file[j].split(",")[0].split("-")[0] and (file[i].split(",")[0].split("-")[1] >= file[j].split(",")[1].split("-")[1] or file[i].split(",")[0].split("-")[1] >= file[j].split(",")[1].split("-")[1])):
                    j+=1
                else:
                    pairs_overlap += 1
                    j+=1
                    i+=1
            i+=1
        return pairs_overlap



if __name__ == "__main__":
    # Part One
    print(f"Assignment pairs which fully contains the other: {part1(INPUT_PATH)}")

    # Part Two
    print(f"TBRead: {part2(INPUT_PATH)}")
