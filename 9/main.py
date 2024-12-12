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


# 4 minutes ;(
def super_alternative_compact_filesystem(input: list) -> list:
    reversed_input = input[::-1]
    unique_values = set(input)
    unique_values.remove(".")

    for i, c in enumerate(reversed_input):
        if c not in unique_values:
            continue

        file_block_size = get_block_size(reversed_input, i)
        unique_values.remove(c)

        left_most_normal_index = len(input) - i - file_block_size

        dot_count = 0

        for j, d in enumerate(input):
            if dot_count > 0:
                dot_count -= 1
                # 50% speed increase
                continue

            if j >= left_most_normal_index:
                # Only move left
                break

            # Search forwards for a dot
            if d == ".":
                free_block_size = get_block_size(input, j)
                if free_block_size >= file_block_size:
                    input = swap_list_indices(
                        input, j, left_most_normal_index, file_block_size
                    )
                    print(j, left_most_normal_index, file_block_size)
                    break
                else:
                    dot_count = free_block_size - 1

    return input


def swap_list_indices(input: list, x: int, y: int, size: int) -> list:
    for i in x, y:
        if i + size > len(input):
            raise ValueError()

    temp = input[x : x + size]
    input[x : x + size] = input[y : y + size]
    input[y : y + size] = temp

    return input


def get_block_size(input: list, index: int) -> int:
    """
    Given the value at the index of input
    find how many of those values are repated ahead of the index before a gap, inclusive
    """

    size = 0
    for c in input[index:]:

        if c == input[index]:
            size += 1

        else:
            break

    return size


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
        if c == ".":
            continue

        checksum += i * c

    return checksum


def read_input(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read().strip()


if __name__ == "__main__":
    input = read_input("input.txt")

    print(
        "P1 Solution:",
        calculate_checksum(
            compact_filesystem(
                expand_disk_map(input),
            )
        ),
    )

    print(
        "P2 Solution:",
        calculate_checksum(
            super_alternative_compact_filesystem(
                expand_disk_map(input),
            )
        ),
    )
