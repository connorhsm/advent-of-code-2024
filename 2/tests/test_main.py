import pytest
from main import part_one, part_two


@pytest.mark.parametrize(
    "input, expected",
    [
        (
            [
                "7 6 4 2 1",
                "1 2 7 8 9",
                "9 7 6 2 1",
                "1 3 2 4 5",
                "8 6 4 4 1",
                "1 3 6 7 9",
            ],
            2,
        ),
    ],
)
def test_part_one(input, expected):
    assert part_one(input) == expected
    
@pytest.mark.parametrize(
    "input, expected",
    [
        (
            [
                "7 6 4 2 1",
                "1 2 7 8 9",
                "9 7 6 2 1",
                "1 3 2 4 5",
                "8 6 4 4 1",
                "1 3 6 7 9",
            ],
            4,
        ),
    ],
)
def test_part_two(input, expected):
    assert part_two(input) == expected
