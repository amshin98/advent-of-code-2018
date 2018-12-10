import re

FABRIC_SIZE = 1000

def part1(claims):
    fabric = [[0] * FABRIC_SIZE for i in range(FABRIC_SIZE)]
    generate_fabric_claims(fabric, claims)

    multiple_claims = 0
    for i in range(len(fabric)):
        for j in range(len(fabric[0])):
            if fabric[i][j] >= 2:
                multiple_claims += 1

    return multiple_claims

def part2(claims):
    fabric = [[0] * FABRIC_SIZE for i in range(FABRIC_SIZE)]
    generate_fabric_claims(fabric, claims)

    for str_claim in claims:
        multiple = False
        claim = split_claim(str_claim)
        for i in range(int(claim[3]), int(claim[3]) + int(claim[6])):
            for j in range(int(claim[2]), int(claim[2]) + int(claim[5])):
                if fabric[i][j] > 1:
                    multiple = True

        if not multiple:
            return claim[0]


def generate_fabric_claims(fabric, claims):
    for str_claim in claims:
        #Note: start's @ idx 2 & 3, l and w @ idx 5 & 6
        claim = split_claim(str_claim)
        for i in range(int(claim[3]), int(claim[3]) + int(claim[6])):
            for j in range(int(claim[2]), int(claim[2]) + int(claim[5])):
                fabric[i][j] += 1

def split_claim(claim):
    return re.compile("\s|,|:|x").split(claim)

if __name__ == "__main__":
    claims = []

    with open("day3claims.txt") as file:
        claims = [line.strip() for line in file]

    print("Part 1: " + str(part1(claims)))
    print("Part 2: " + str(part2(claims)))
