"""
Yahara Software: Adventure Journey - Back End

Methods to run Adventure Journey

Vaughn Neidert
"""


import re
import math

VALID_STRING_PATTERN = r'^(\d+[FBLR])+$'
VALID_SUBSTRING_PATTERN = r'\d+[FBLR]'


def _get_input_from_file() -> str:
    """
    Gets the direction input from the user via a file
    """
    file_name = input("Enter the file name:\n")
    file_contents = ""
    with open(file_name) as file:
        file_contents = file.read()
    return file_contents


def _get_input_from_terminal() -> str:
    """
    Gets the direction input from the user via the terminal
    """
    return input("Enter the directions to use:\n")


def get_direction_input():
    """
    Gets the direction input from the user
    """
    valid_entry = False
    direction_input = ""
    while not valid_entry:
        selection = input("Select input type: File (enter 0) or terminal input (enter 1)\n")
        if selection == "0":
            direction_input = _get_input_from_file()
            valid_entry = True
        elif selection == "1":
            direction_input = _get_input_from_terminal()
            valid_entry = True
        else:
            print("Please select valid entry type")
    return direction_input


def _valid_input(direction_input : str) -> bool:
    """
    Determines if a string is a valid input by
    matching the following regex pattern: ^(\d+[FBLR])+$

    Args:
    direction_input: the input string to compute distance from
    """
    return re.fullmatch(VALID_STRING_PATTERN, direction_input)


def validate_input(direction_input : str):
    """
    Validates a string is a valid input

    Args:
    direction_input: the input string to compute distance from
    """
    if not _valid_input(direction_input):
        raise Exception(f"Input {direction_input} is invalid!")
    

def _split_input_into_steps(direction_input : str):
    """
    Splits the direction input into individual steps for processing
    by the following regex pattern: \d+[FBLR]

    Args: 
    """
    return re.findall(VALID_SUBSTRING_PATTERN, direction_input)


def get_euclidean_distance(x, y):
    """
    Computes the Euclidean distance between two points

    Args:
    x: the x coordinate of the point
    y: the y coordinate of the point
    """
    x_2 = math.pow(x, 2)
    y_2 = math.pow(y, 2)
    return math.sqrt(x_2 + y_2)


def compute_distance(direction_input : str) -> float:
    """
    Computes the total distance covered by the direction input

    Args:
    direction_input: the input string to compute distance from
    """
    validate_input(direction_input)
    components = _split_input_into_steps(direction_input)
    vertical_distance = 0
    horizontal_distance = 0
    for component in components:
        distance = int(component[:-1])
        match component[-1]:
            case 'F':
                vertical_distance += distance
            case 'B':
                vertical_distance -= distance
            case 'L':
                horizontal_distance -= distance
            case 'R':
                horizontal_distance += distance
    return get_euclidean_distance(horizontal_distance, vertical_distance)