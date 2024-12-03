import pytest

import day_2

def test_extract_reports_from_file():
    reports = day_2.extract_reports_from_file("day_2_input.txt")
    assert reports[0] == [74, 76, 78, 79, 76]
    assert reports[1] == [38, 40, 43, 44, 44]
    assert len(reports) == 1000


@pytest.mark.parametrize('input,expected',
                         [([1, 3, 5, 8, 9], True), ([1, 3, 2, 9, 10], False), ([1, 3, 5, 7, 7], False)])
def test_is_ascending_or_descending(input, expected):
    assert day_2.is_ascending_or_descending(input) is expected


@pytest.mark.parametrize('input,expected',
                         [([1005, 1007, 1010, 1011, 1012], True), ([10, 13, 17, 18, 19], False)])
def test_has_valid_difference(input, expected):
    assert day_2.has_valid_difference(input) is expected


@pytest.mark.parametrize('input,expected',
                         [([105, 107, 110, 111, 111], False), ([10, 13, 17, 18, 19], False), ([1, 5, 4, 5, 7], False), ([1, 4, 5, 8, 9], True)])
def test_is_report_safe(input, expected):
    assert day_2.has_valid_difference(input) is expected


def test_evaluate_reports():
    reports = [[1, 3, 5, 8, 9], [1005, 1007, 1010, 1011, 1012], [1, 3, 2, 9, 10], [10, 13, 15, 17, 17]]
    assert day_2.evaluate_reports(reports) == (2, 2)


def test_evaluate_reports_with_removals():
    reports = [[1, 3, 5, 8, 9], [1005, 1007, 1010, 1011, 1012], [1, 3, 6, 5, 7], [10, 13, 15, 17, 17]]
    assert day_2.evaluate_reports_with_removal(reports) == (4, 0)