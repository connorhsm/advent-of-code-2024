import sys
from loguru import logger


INPUT_FILE = "input.txt"

logger.remove()
logger.add(sys.stderr, level="INFO")


def main() -> None:
    left_list, right_list = parse_input(
        read_input(INPUT_FILE),
    )

    print(f"Total distance: {do_the_first_thing(left_list, right_list)}")
    print(f"Similarity score: {do_the_second_thing(left_list, right_list)}")


def do_the_first_thing(left: list, right: list) -> int:
    left.sort()
    right.sort()

    total_distance = 0

    for i in range(len(left)):

        logger.debug(
            f"Left: {left[i]} | Right: {right[i]} | Distance: {abs(left[i] - right[i])}"
        )

        total_distance += abs(left[i] - right[i])

    return total_distance


def do_the_second_thing(left: list, right: list) -> int:

    similarity_score = 0

    for l in left:
        occurrences = right.count(l)
        similarity = l * occurrences

        logger.debug(f"Left: {l} | Occurrences: {occurrences} | Similarity: {similarity}")

        similarity_score += similarity

    return similarity_score


def parse_input(input: list[str]) -> tuple[list, list]:
    left_list = list()
    right_list = list()

    for line in input:
        split = line.split("   ")
        left_list.append(int(split[0]))
        right_list.append(int(split[1]))

    return left_list, right_list


def read_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.read().splitlines()


if __name__ == "__main__":
    main()
