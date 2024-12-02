import pytest
from main import parse_input, do_the_first_thing, do_the_second_thing


@pytest.mark.parametrize(
    "input, expected",
    [
        (
            [
                "1   2",
                "3   4",
                "5   6",
            ],
            (
                [1, 3, 5],
                [2, 4, 6],
            ),
        ),
        (
            [
                "2348   9503",
                "89043   8343",
                "2484   3894",
            ],
            (
                [2348, 89043, 2484],
                [9503, 8343, 3894],
            ),
        ),
    ],
)
def test_parse_input(input, expected):
    assert parse_input(input) == expected


@pytest.mark.parametrize(
    "input_left, input_right, expected",
    [
        (
            [195, 343, 594, 127],
            [958, 739, 894, 273],
            1605
        ),
        (
            [1, 3, 5],
            [2, 4, 6],
            3,
        ),
        (
            [2348, 89043, 2484],
            [9503, 8343, 3894],
            86945,
        ),
    ],
)
def test_do_the_first_thing(input_left, input_right, expected):
    assert do_the_first_thing(input_left, input_right) == expected

@pytest.mark.parametrize(
    "input_left, input_right, expected",
    [
        (
            [1, 3, 5],
            [1, 3, 6],
            4,
        ),
        (
            [10, 20, 30, 50, 60],
            [20, 10, 40, 10, 10],
            50,
        ),
    ],
)
def test_do_the_second_thing(input_left, input_right, expected):
    assert do_the_second_thing(input_left, input_right) == expected
