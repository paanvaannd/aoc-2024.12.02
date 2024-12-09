# Red-Nosed Reports

_Advent of Code 2024, Day 2_

**Project status**:

[![UNIX (macOS & Linux)](https://github.com/paanvaannd/aoc-2024.12.02/actions/workflows/tests.yaml/badge.svg)](https://github.com/paanvaannd/aoc-2024.12.02/actions/workflows/tests.yaml)

## Puzzles

Each puzzle's task is reframed below according to my understanding of the task.

### Puzzle 1

An input file (`data/levels.txt`) with rows detailing reports of levels should be scanned to report which rows ("reports") are safe and which are not. A "safe" report constitutes one in which the levels are all consecutively increasing or decreasing across the entire row by only 1-2 unit increments between consecutive levels. Anything else is "unsafe."

### Puzzle 2

The same conditions hold, but the tolerance for errors has increased such that if a single value in a level report is removed and the line is otherwise safe, this now constitutes a "safe" line.
