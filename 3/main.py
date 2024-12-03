import re

INPUT_FILE = "input.txt"


def main() -> None:
    input = read_input(INPUT_FILE)

    print(part_one(input))
    print(part_two(input))


def part_one(input: str) -> int:
    occurrences = re.findall(r"mul\([0-9]+,[0-9]+\)", input)

    total = 0

    for i in occurrences:
        total += multiply_mul(i)

    return total


def part_two(input: str) -> None:
    occurrences = re.findall(r"mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)", input)

    total = 0
    state_enabled = True

    for i in occurrences:
        if i == "do()":
            state_enabled = True
        elif i == "don't()":
            state_enabled = False

        if i.startswith("mul(") and state_enabled:
            total += multiply_mul(i)

    return total


def multiply_mul(mul_string: str) -> int:
    # mul_string appears like 'mul(684,550)'

    split = mul_string.split(",")
    left = int(split[0].replace("mul(", ""))
    right = int(split[1].replace(")", ""))

    return left * right


def read_input(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read().replace("\n", "")


if __name__ == "__main__":
    main()
