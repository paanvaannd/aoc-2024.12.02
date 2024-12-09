#!/usr/bin/env python

# Import 3rd-party modules
import pytest

# Import custom modules
import red_nosed_reports.red_nosed_reports as rnr

# Type aliases
report = tuple[int, ...]


@pytest.mark.parametrize(
    ("report_line", "expected"),
    (
        pytest.param((1, 3, 5, 7, 11), True,
                     id="Testing order: ascending, unique, non-incrementing."),
        pytest.param((1, 2, 3, 5, 5), True,
                     id="Testing order: ascending, repeating, incrementing."),
        pytest.param((5, 4, 3, 2, 1), True,
                     id="Testing order: descending, unique, incrementing."),
        pytest.param((5, 5, 4, 3, 2), True,
                     id="Testing order: descending, repeating, incrementing."),
        pytest.param((1, 2, 3, 5, 4), False,
                     id="Testing order: unordered, unique, incrementing."),
        pytest.param((5, 3, 4, 2, 1), False,
                     id="Testing order: unordered, unique, incrementing.")
    )
)
def test_is_ordered(report_line: report, expected: bool):
    assert rnr.is_ordered(report_line) == expected, \
    "Levels should either be uniformly ascending or descending."


@pytest.mark.parametrize(
    ("report_line", "expected"),
    (
        pytest.param((1, 2, 3, 4, 9), True,
                     id="Testing uniqueness: unique, ascending, non-incrementing."),
        pytest.param((9, 7, 5, 8, 1), True,
                     id="Testing uniqueness: unique, unordered, incrementing."),
        pytest.param((1, 1, 2, 3, 4), False,
                     id="Testing uniqueness: repeating, ascending, incrementing."),
        pytest.param((5, 5, 4, 3, 1), False,
                     id="Testing uniqueness: repeating, descending, incrementing.")
    )
)
def test_is_unique(report_line: report, expected: bool):
    assert rnr.is_unique(report_line) == expected, \
    "There should be no repeated levels in the report."


@pytest.mark.parametrize(
    ("report_line", "expected"),
    (
        pytest.param((1, 2, 3, 5, 4), True,
                     id="Testing incrementing: incrementing, ascending, unique."),
        pytest.param((1, 2, 3, 5, 5), True,
                     id="Testing incrementing: incrementing, ascending, repeating."),
        pytest.param((5, 4, 3, 2, 1), True,
                     id="Testing incrementing: incrementing, decreasing, unique."),
        pytest.param((5, 1, 7, 12, 1), False,
                     id="Testing incrementing: non-incrementing, unordered, repeating."),
        pytest.param((8, 3, 7, 2, 9), False,
                     id="Testing incrementing: non-incrementing, unordered, unique.")
    )
)
def test_is_appropriately_incrementing(report_line: report, expected: bool):
    assert rnr.is_appropriately_incrementing(report_line) == expected, \
    "Changes in level magnitude should not exceed 3."


@pytest.mark.parametrize(
    ("report_line", "expected"),
    (
        pytest.param((1, 2, 3, 4, 5), True,
                     id="Testing safety: safe, ascending, unique, incrementing."),
        pytest.param((10, 9, 7, 4, 3), True,
                     id="Testing safety: safe, descending, unique, incrementing."),
        pytest.param((1, 4, 7, 10, 13), True,
                     id="Testing safety: safe, ascending, unique, incrementing (by 3)."),
        pytest.param((1, 2, 4, 3, 5), False,
                     id="Testing safety: unsafe, unordered, unique, incrementing."),
        pytest.param((3, 9, 12, 20, 3), False,
                     id="Testing safety: unsafe, unordered, repeating, non-incrementing."),
        pytest.param((1, 2, 3, 4, 4), False,
                     id="Testing safety: unsafe, ordered, repeating, incrementing."),
        pytest.param((1, 4, 7, 4, 4), False,
                     id="Testing safety: unsafe, unordered, repeating, incrementing."),
        pytest.param((1, 4, 7, 11, 13), False,
                     id="Testing safety: unsafe, ascending, unique, non-incrementing.")
    )
)
def test_determine_safety_strict(report_line: report, expected):
    assert rnr.determine_strict_safety(report_line) == expected


@pytest.mark.parametrize(
    ("report_line", "expected"),
    (
        pytest.param((1, 2, 3, 3, 5), True,
                     id="Testing dampened safety: safe, if repetition dampened."),
        pytest.param((10, 6, 5, 4, 3), True,
                     id="Testing dampened safety: safe, if increment dampened."),
        pytest.param((1, 2, 3, 5, 4), True,
                     id="Testing dampened safety: safe, if disorder dampened.")
    )
)
def test_determine_safety_dampened(report_line: report, expected):
    assert rnr.determine_dampened_safety(report_line) == expected

