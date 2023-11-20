"""
Yahara Software: Adventure Journey - Back End

Main method to test

Vaughn Neidert
"""

from adventure_journey import *

def main():
    direction_input = get_direction_input()
    try:
        distance = compute_distance(direction_input)
        print("Distance to final destination", distance)
    except Exception as e:
        print(str(e))
    

if __name__ == "__main__":
    main()