def part1(changes):
    frequency = 0

    for change in changes:
        frequency += int(change)

    print(frequency)

def part2(changes):
    frequencies = []
    current_frequency = 0
    idx = 0
    
    while current_frequency not in frequencies:
        frequencies.append(current_frequency)
        change = int(changes[idx % len(changes)])
        current_frequency += change
        idx += 1

    print(current_frequency)


changes = []

with open("day1changes.txt") as file:
    changes = file.readlines()

print("Part 1:")
part1(changes)
print("Part 2:")
part2(changes)