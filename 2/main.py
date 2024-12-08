def part_one(input: list[str]) -> int:

    safe_count = 0

    for report in input:
        if check_safety_one(report):
            safe_count += 1

    return safe_count


def check_safety_one(numbers: str) -> bool:
    """
    For a list of numbers seperated by a space, are the numbers safe?

    Safety:
    - Numbers are all gradually increasing or all gradually decreasing
    - Gradual meaning at least one and at most three

    numbers: '7 6 4 2 1'
    """

    nums = [int(x) for x in numbers.split()]

    for i, n in enumerate(nums):

        # First iteration, set the state
        if i == 0:
            next = nums[i + 1]

            if n > next:
                # We're decreasing!
                state = False

            elif n < next:
                # We're increasing!
                state = True

            elif n == next:
                return False

            continue

        # Every other iteration, compare previours
        previous = nums[i - 1]

        if n > previous and state == False:
            # We have increased after state was decreasing!
            return False

        elif n < previous and state == True:
            # We have decreased after state was increasing!
            return False

        # How big was the diff?
        diff = abs(n - previous)

        if diff < 1 or diff > 3:
            # Not gradual!
            return False

    return True


def part_two(input: list[str]) -> int:

    safe_count = 0

    for report in input:
        if check_safety_one(report):
            safe_count += 1
        else:
            # It wasn't safe, retry it by removing on element at a time and if any one of them work, then it was safe enough
            if check_safety_two(report):
                safe_count += 1

    return safe_count

def check_safety_two(numbers: str) -> bool:
    nums = [int(x) for x in numbers.split()]
    
    for m in nums:
            
        unsafe = 0

        for i, n in enumerate(nums):

            # First iteration, set the state
            if i == 0:
                next = nums[i + 1]

                if n > next:
                    # We're decreasing!
                    state = False

                elif n < next:
                    # We're increasing!
                    state = True

                elif n == next:
                    state = None
                    unsafe += 1

                continue

            # Every other iteration, compare previours
            previous = nums[i - 1]

            if n > previous and state == False:
                # We have increased after state was decreasing!
                return False

            elif n < previous and state == True:
                # We have decreased after state was increasing!
                return False

            # How big was the diff?
            diff = abs(n - previous)

            if diff < 1 or diff > 3:
                # Not gradual!
                return False

        return True


def read_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.read().splitlines()


if __name__ == "__main__":
    input = read_input("input.txt")

    print("One:", part_one(input))
    print("Two:", part_two(input))
