"""
Yahara Software: Adventure Journey - Back End Tests

Tests to validate functionality

Vaughn Neidert
"""

from adventure_journey import *
import unittest


def get_input_from_file(file_name):
    with open(file_name) as file:
        file_contents = file.read()
    return file_contents


class AdventureJourneyTests(unittest.TestCase):

    def test_input_no_distance(self):
        direction_input = "1F1L1B1R"
        self.assertEquals(compute_distance(direction_input), 0)


    def test_3_4_5(self):
        direction_input = "3R4F"
        self.assertEquals(compute_distance(direction_input), 5)


    def test_only_horizontal(self):
        left = 5
        right = 3
        direction_input = f"{left}L{right}R"
        self.assertEquals(compute_distance(direction_input),abs((-left + right)))


    def test_only_vertical(self):
        forward = 5
        backward = 3
        direction_input = f"{forward}F{backward}B"
        self.assertEquals(compute_distance(direction_input), abs((-forward + backward)))

    def test_bad_input_ending(self):
        direction_input = get_input_from_file("inputs/given_input_bad.txt")
        with self.assertRaises(Exception):
            compute_distance(direction_input)

    def test_bad_input_middle(self):
        direction_input = get_input_from_file("inputs/given_input_bad_middle.txt")
        with self.assertRaises(Exception):
            compute_distance(direction_input)



if __name__ == "__main__":
    unittest.main()