#!/usr/bin/env python

# Built-in modules
import os

# Globals
SCRIPT_PATH = os.path.abspath(__file__)
SCRIPT_ROOT = os.path.dirname(SCRIPT_PATH)
PROJECT_ROOT = os.path.dirname(SCRIPT_ROOT)
MAX_INCREMENT = 3

# Type aliases
report = tuple[int, ...]


def read_data_file(filename: str) -> str:
    _data_file = os.path.join(PROJECT_ROOT, "data", filename)
    with open(_data_file, mode="r") as _file:
        return _file.read()


def is_ordered(report_line: report) -> bool:
    return (tuple(sorted(report_line, reverse=False)) == report_line
            or tuple(sorted(report_line, reverse=True)) == report_line)


def is_unique(report_line: report) -> bool:
    return len(set(report_line)) == len(report_line)


def is_appropriately_incrementing(report_line: report) -> bool:
    _appropriate_increment = True
    for i, _level in enumerate(report_line):
        _prior = report_line[i-1] if i > 0 else report_line[i]
        if _level > _prior + MAX_INCREMENT or _level < _prior - MAX_INCREMENT:
            _appropriate_increment = False
            break
    return _appropriate_increment


def dampen_issue(report_line: report, i: int) -> bool:
    _unsafe_report = list(report_line)
    del _unsafe_report[i]
    _modified_report = tuple(_unsafe_report)

    _ordered = is_ordered(_modified_report)
    _unique = is_unique(_modified_report)
    _incrementing = is_appropriately_incrementing(_modified_report)
    return _ordered and _unique and _incrementing


def attempt_issue_dampening(report_line: report) -> bool:
    return any([dampen_issue(report_line, i)
                for i, _ in enumerate(report_line)])


def determine_strict_safety(report_line: report) -> bool:
    _ordered: bool = is_ordered(report_line)
    _unique: bool = is_unique(report_line)
    _incrementing: bool = is_appropriately_incrementing(report_line)
    return _ordered and _unique and _incrementing


def determine_dampened_safety(report_line: report) -> bool:
    _ordered: bool = is_ordered(report_line)
    _unique: bool = is_unique(report_line)
    _incrementing: bool = is_appropriately_incrementing(report_line)
    _conditions_met = _ordered + _unique + _incrementing

    _safe: bool = False
    if _conditions_met == 3:
        _safe = True
    else:
        _safe = attempt_issue_dampening(report_line)
    return _safe


def parse_input(corpus: str) -> tuple[tuple[int, ...], ...]:
    _contents = corpus.splitlines()
    return tuple(tuple(map(int, _line.split(" "))) for _line in _contents)


def main():
    contents = read_data_file("level_reports.txt")
    parsed_contents = parse_input(contents)

    print("\nPart 1\n------")
    strictly_safe_reports = [determine_strict_safety(_line)
                             for _line in parsed_contents]
    print("The total number of safe reports is "
          f"{sum(strictly_safe_reports):,}.")

    print("\nPart 2\n------")
    dampened_safe_reports = [determine_dampened_safety(_line)
                             for _line in parsed_contents]
    print("The total number of safe reports is "
          f"{sum(dampened_safe_reports):,}.")


if __name__ == "__main__":
    main()
