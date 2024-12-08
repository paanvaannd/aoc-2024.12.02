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


contents = read_data_file("levels.txt")
