import pytest
from datetime import date

from seasons import seasons


@pytest.mark.parametrize(
    "input,expected",
    [
        (f"{date.today().year}-{date.today().month}-{date.today().day}", "Zero minutes"),
        (f"{date.today().year-1}-{date.today().month}-{date.today().day}", "Five hundred twenty-five thousand, six hundred minutes"),
    ],
)
def test_seasons_valid_inputs(input, expected):
    assert seasons(input) == expected


def test_seasons_invalid_input():
    with pytest.raises(SystemExit):
        seasons("Cat 2022-02-30")