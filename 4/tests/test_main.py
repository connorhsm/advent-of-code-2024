import pytest

from main import check_north


@pytest.mark.parametrize(
    "input, idy, idx, expected",
    [
        (
            [
                "XMXASSS",
                "MXASAXS",
                "MAXSMXS",
                "MASXXXS",
            ],
            3,
            4,
            True,
        ),
    ],
)
def test_check_north(input, idy, idx, expected):
    assert check_north(input, idy, idx) == expected
