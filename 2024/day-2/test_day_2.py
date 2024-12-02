import pytest

import day_2


def test_extract_reports_from_file():
    reports = day_2.extract_reports_from_file("day_2_input.txt")
    assert reports[0] == [74, 76, 78, 79, 76]
    assert reports[1] == [38, 40, 43, 44, 44]
    assert len(reports) == 1000


@pytest.mark.parametrize('input,expected',
                         [([1, 3, 5, 8, 9], True), ([1, 3, 2, 9, 10], False), ([1, 3, 5, 7, 7], False)])
def test_check_is_report_safe(input, expected):
    assert day_2.check_is_report_safe(input) == expected