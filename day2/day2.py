def part1(strings):

if __name__ == "__main__":
	strings = []

	with open("day2strings.txt") as file:
		strings = file.readlines()

	print("Part 1:")
	print(part(strings))