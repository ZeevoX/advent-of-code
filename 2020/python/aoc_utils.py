import inspect
import os


def _top_level_caller():
    """get the filename of the original script that called this up"""
    return inspect.stack()[-1].filename


def get_day():
    """
    get the day of the python script calling this function
    NB: no validation for filename, it is assumed to be DayXX.py
    """
    return os.path.basename(_top_level_caller())[3:5]


def filepath():
    """get the filepath of the input"""
    return os.path.abspath(
        f"{os.path.dirname(_top_level_caller())}/../inputs/{get_day()}.txt"
    )


def input():
    """get a reference straight to the input file"""
    return open(filepath(), "r")


def input_int_list():
    """parse input into a list of ints"""
    return [int(line.rstrip()) for line in open(filepath(), "r")]


def input_string_list():
    """parse input into a list of strings"""
    return [line.rstrip() for line in open(filepath(), "r")]


def input_block_list():
    """input split by paragraph i.e. two newlines"""
    return open(filepath(), "r").read().split("\n\n")


def filter_empty(li):
    """remove empty entries (e.g. when splitting a string)"""
    return list(filter(None, li))
