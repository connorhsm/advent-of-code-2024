def expand_disk_map(input: str) -> list:

    result = []
    for i, digit in enumerate(input):
        for n in range(int(digit)):
            if i % 2 == 0:
                # File
                result.append(int(i / 2))

            if i % 2 == 1:
                # Space
                result.append(".")

    return result


def compact_filesystem(input: list) -> list:
    """
    
    Pass in a list of file blocks and free space "." and
    return a compacted list of the file blocks without any
    free space, according to the compacting rules.

    In: [0, 0, '.', '.', '.', ... 6, 6, 6, 6, '.', 7, 7, 7, '.', 8, 8, 8, 8, 9, 9]
    Out: [0, 0, 9, 9, 8, ... 3, 3, 3, 6, 4, 4, 6, 5, 5, 5, 5, 6, 6]
    
    """

    dot_less = [x for x in input if x != "."]

    result = []
    for c in input:
        if len(dot_less) == 0:
            break

        if c == ".":
            result.append(dot_less[-1])
            dot_less.pop()

        else:
            result.append(c)
            dot_less.pop(0)

    return result


def calculate_checksum(input: list) -> int:
    checksum = 0
    for i, c in enumerate(input):
        checksum += i * c

    return checksum


def read_input(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read().strip()


if __name__ == "__main__":
    input = read_input("input.txt")

    print(
        "Solution:",
        calculate_checksum(
            compact_filesystem(
                expand_disk_map(input),
            )
        ),
    )
