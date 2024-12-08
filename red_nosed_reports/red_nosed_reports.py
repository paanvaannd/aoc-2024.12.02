#!/usr/bin/env python

# Built-in modules
import os

# Globals
SCRIPT_PATH = os.path.abspath(__file__)
SCRIPT_ROOT = os.path.dirname(SCRIPT_PATH)
PROJECT_ROOT = os.path.dirname(SCRIPT_ROOT)


def read_data_file(filename: str) -> str:
    _data_file = os.path.join(PROJECT_ROOT, "data", filename)
    with open(_data_file, mode="r") as _file:
        return _file.read()


def is_ordered(report: tuple[int, ...]) -> bool:
    return (tuple(sorted(report, reverse=False)) == report
            or tuple(sorted(report, reverse=True)) == report)


def is_unique(report: tuple[int, ...]) -> bool:
    return len(set(report)) == len(report)


def is_appropriately_incrementing(report: tuple[int, ...]) -> bool:
    _appropriate_increment = True
    for i, _level in enumerate(report):
        _prior = report[i-1] if i > 0 else report[i]
        if _level > _prior + 3 or _level < _prior - 3:
            _appropriate_increment = False
            break
    return _appropriate_increment


def determine_safety(report: tuple[int, ...]) -> bool:
    _ordered: bool = is_ordered(report)
    _unique: bool = is_unique(report)
    _incrementing: bool = is_appropriately_incrementing(report)
    return _ordered and _unique and _incrementing


def parse_input(corpus: str) -> tuple[tuple[int, ...], ...]:
    _contents = corpus.splitlines()
    return tuple(tuple(map(int, _line.split(" "))) for _line in _contents)


def main():
    contents = read_data_file("level_reports.txt")
    parsed_contents = parse_input(contents)
    safe_reports = [determine_safety(_report) for _report in parsed_contents]
    print("\nPart 1\n------")
    print(f"The total number of safe reports is {sum(safe_reports):,}.")


if __name__ == "__main__":
    main()
