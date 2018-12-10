def part1(strings):
    two_strings = 0
    three_strings = 0

    for string in strings:
        string_dict = {}
        for letter in string:
            if letter in string_dict:
                string_dict[letter] += 1
            else:
                string_dict[letter] = 1

        if 2 in string_dict.values():
            two_strings += 1
        if 3 in string_dict.values():
            three_strings += 1

    return two_strings * three_strings

def part2(strings):
    #Note: absolute value of ord(z) - ord(a) = 25
    sum_dict = {}
    for string in strings:
        sum_dict[string] = get_int_sum(string)


    for string1 in sum_dict:
        for string2 in sum_dict:
            if abs(sum_dict[string1] - sum_dict[string2]) <= 25:
                shared = string_check(string1.strip(), string2.strip())
                if shared != None:
                    return shared

def string_check(string1, string2):
    shared = ""
    for idx in range(len(string1)):
        if string1[idx] == string2[idx]:
            shared += string1[idx]
    
    if len(shared) != len(string1) - 1:
        shared = None

    return shared


def get_int_sum(string):
    sum = 0
    for letter in string:
        sum += ord(letter)
    return sum


if __name__ == "__main__":
    strings = []

    with open("day2strings.txt") as file:
        strings = [line.strip() for line in file]

    print("Part 1:" + str(part1(strings)))
    print("Part 2:" + str(part2(strings)))