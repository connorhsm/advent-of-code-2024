# Word search
# Find XMAS

from enum import Enum, auto


WORD = "XMAS"


class Direction(Enum):
    N = auto()
    E = auto()
    S = auto()
    W = auto()

    NE = auto()
    SE = auto()
    SW = auto()
    NW = auto()

    def get_location(
        self, position: tuple[int, int], board_size: tuple[int, int]
    ) -> tuple[None, None] | tuple[int, int]:
        # Where position = (y, x) and board_size = (y, x)

        match self:
            case Direction.N:
                location = position[0] - 1, position[1]

            case Direction.E:
                location = position[0], position[1] + 1

            case Direction.S:
                location = position[0] + 1, position[1]

            case Direction.W:
                location = position[0], position[1] - 1

            # Maybe oppotunity missed to combine above operations to produce the below
            case Direction.NE:
                location = position[0] - 1, position[1] + 1

            case Direction.SE:
                location = position[0] + 1, position[1] + 1

            case Direction.SW:
                location = position[0] + 1, position[1] - 1

            case Direction.NW:
                location = position[0] - 1, position[1] - 1

        # for l, b in zip(location, board_size):
        #     if l >= b or l < 0:
        #         return None, None

        # if location(0) >= board_size(0) or location(0) < 0 or location(1) >= board_size(1) or location(1) < 0:
        #     return None

        return location


def main():
    input = read_input("input_test.txt")

    # print(input)

    # part_one(input)
    part_one_v2(input)


def part_one(input) -> int:
    for idy, i in enumerate(input):  # Each line
        for idx, j in enumerate(i):  # Each char

            # We want to find the starting char, X
            if j != "X":
                continue

            # Great, we've found one.
            # Its time to traverse all directions and find the next valid char, M

            # How to see each direction?
            # East: j + 1
            # West: j - 1
            # North: i - 1
            # South: i + 1
            # Diag NE: i - 1 AND j + 1 # This is duplicating, intresting
            # Diag SE: i + 1 AND j + 1
            # Diag SW: i + 1 AND j - 1
            # Diag NW: i - 1 AND j - 1
            # maybe enum?

            # We also need to check that we're not at any list boundary
            # enumerate? handle index error?

            # if idy + 1 >= len(i):  # Must be repeated for each case
            #     # End of line
            #     continue

            for d in Direction:
                y, x = d.get_location((idy, idx), (len(i), len(j)))

                print(y, x)

                if y and x:
                    print(j, idy, idx, y, x, i[y], j[x])

            break
        break

        # if i[idy + 1] == "M":
        #     print("yay")

        # print(idx, idy, j)

    pass


def part_one_v2(input: str) -> None:
    total = 0
    for idy, y in enumerate(input):
        # print(y)

        for idx, x in enumerate(y):
            # for letters in word
            # is this the first letter?
            # if so further checks
            # if not, contine
            
            if x == WORD[0]:
                if check_north(input, idy, idx):
                    total += 1
                
                
                
                
                # Ah we have found the start of a word!
                # Lets check around it
                # for letter in WORD[1:]:
                    # if north has letter 2, 
                    
                
                
                
                

            # If current is the first letter
            # Then check every direction for the second letter
            # and so on
            continue
            if x == XMAS[0]:
                # Now check every direction for the second letter
                for idc, c in enumerate(XMAS[1:]):
                    # for every direction

                    print(x)

                # print(check_north(input, idy, idx))

            total += 1
            continue

            # try:
            #     print(input[idy + 1][idx])
            #     check_north(input, idy, idx)
            # # check_east(input, idy, idx)

            # except IndexError:
            #     pass

            # if y[idx + 1] == "M":
            #     print("yay1")

            #     if y[idx + 2] == "A":
            #         print("yay2")

            #         if y[idx + 3] == "S":
            #             print("yay3")

            for idc, c in enumerate(XMAS):
                if x == XMAS[0]:
                    pass

                if x == c and idc == 0:
                    print(x, c)
                # total += 1

    print(total)


def check_north(input, idy, idx, i = 1) -> bool:
    if i == len(WORD) - 1:
        return True
    
    try:
        if input[idy - i][idx] == WORD[i]:
            print(input[idy - i][idx], WORD[i], idy, idx)
            check_north(input, idy, idx, i + 1)
    except IndexError:
        return False

    return False


def check_east(input, idy, idx):
    if input[idy][idx : idx + 4] == XMAS:
        print(XMAS)


def read_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.read().splitlines()

    # Brain
    # For each starting point (any X character)
    # traverse every direction until you find the last valid character or an invalid character

    # Part two predicition
    # Search for additional Ms


if __name__ == "__main__":
    main()
