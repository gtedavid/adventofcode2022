# witout any library
INPUT_PATH = "3rd\input.txt"

def part1(path_in):
    lower_case=[];
    upper_case=[];

    for i in range(26):
        lower_case.append(chr(97+i)); # 97 is the ASCII code for 'a'
        upper_case.append(chr(65+i)); # 65 is the ASCII code for A

    with open(path_in, "r") as input_file:
        sum = 0
        for line in input_file.readlines():
            length_line = len(str(line.strip()))            

            if length_line%2 == 0: #string length is even
                part1 = slice(0,length_line//2)
                part2 = slice(length_line//2,length_line)

                if ''.join(sorted(set.intersection(set(str(line.strip())[part1]),set(str(line.strip())[part2])))) in lower_case: #join will convert the list to a string and sorted will sort the string, intersection will find the common elements between the two sets
                    sum += lower_case.index(''.join(sorted(set.intersection(set(str(line.strip())[part1]),set(str(line.strip())[part2])))))+1 #+1 is the start for the lower case letters value in the problem

                if ''.join(sorted(set.intersection(set(str(line.strip())[part1]),set(str(line.strip())[part2])))) in upper_case: #join will convert the list to a string and sorted will sort the string, intersection will find the common elements between the two sets
                    sum += upper_case.index(''.join(sorted(set.intersection(set(str(line.strip())[part1]),set(str(line.strip())[part2])))))+26+1 #26+1 is the start for the higher case letters value in the problem

            else: #string length is odd
                part1 = slice(0,length_line//2)
                part2 = slice(length_line//2,length_line)

                if ''.join(sorted(set.intersection(set(str(line.strip())[part1]),set(str(line.strip())[part2])))) in lower_case: #join will convert the list to a string and sorted will sort the string, intersection will find the common elements between the two sets
                    sum += lower_case.index(''.join(sorted(set.intersection(set(str(line.strip())[part1]),set(str(line.strip())[part2])))))+1 #+1 is the start for the lower case letters value in the problem

                if ''.join(sorted(set.intersection(set(str(line.strip())[part1]),set(str(line.strip())[part2])))) in upper_case: #join will convert the list to a string and sorted will sort the string, intersection will find the common elements between the two sets
                    sum += upper_case.index(''.join(sorted(set.intersection(set(str(line.strip())[part1]),set(str(line.strip())[part2])))))+26+1 #26+1 is the start for the higher case letters value in the problem
        return sum

def part2(path_in):
    lower_case=[];
    upper_case=[];

    for i in range(26):
        lower_case.append(chr(97+i)); # 97 is the ASCII code for 'a'
        upper_case.append(chr(65+i)); # 65 is the ASCII code for A

    with open(path_in, "r") as input_file:
        sum = 0
        i=0;
        file=input_file.readlines()
        while i < len(file):
            if ''.join(sorted(set(str(file[i].strip())).intersection(set(str(file[i+1].strip()))).intersection(set(str(file[i+2].strip()))))) in lower_case: #join will convert the list to a string and sorted will sort the string, intersection will find the common elements between the three sets
                sum += lower_case.index(''.join(sorted(set(str(file[i].strip())).intersection(set(str(file[i+1].strip()))).intersection(set(str(file[i+2].strip()))))))+1 #+1 is the start for the lower case letters value in the problem
            if ''.join(sorted(set(str(file[i].strip())).intersection(str(file[i+1].strip()),str(file[i+2].strip())))) in upper_case: #join will convert the list to a string and sorted will sort the string, intersection will find the common elements between the three sets
                sum += upper_case.index(''.join(sorted(set(str(file[i].strip())).intersection(set(str(file[i+1].strip()))).intersection(set(str(file[i+2].strip()))))))+26+1 #26+1 is the start for the higher case letters value in the problem
            i+=3
        return sum


if __name__ == "__main__":
    sum_priorities = part1(INPUT_PATH)
    # Part One
    print(f"Sum of priorities: {sum_priorities}")
    # Part Two
    print(f"Sum of priorities: {part2(INPUT_PATH)}")

# References:
# for the common letter https://python-programs.com/python-program-to-find-common-characters-between-two-strings/
# https://www.geeksforgeeks.org/python-convert-list-to-string/
# https://www.pythontutorial.net/python-basics/python-set-intersection/#:~:text=In%20Python%2C%20you%20can%20use%20the%20set%20intersection,method%20and%20%26%20operator%20have%20the%20same%20performance