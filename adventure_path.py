# Split into individual directions (split apart at each letter)
# POSITIVE DIRECTIONS:
    # F, R
# NEGATIVE DIRECTIONS:
    # B, L
# With this in mind, aggregate vertical & horizontal directions, and add them together
# Use this to create a triangle, calculate hypotenuse for final directions

# Doin' it manually for a sanity check
# 15F : +15 vertical
# 6B : -6 vertical
# 6B : -6 vertical
    # 5L : -5 horizontal
    # 16R : +16 horizontal
# 8B : -8 vertical
# 16F : +16 vertical
    # 20L : -20 horizontal
# 6F : +6 vertical
# 13F : +13 vertical
    # 11R : +11 horizontal

# IN TOTAL: +30 vertical, +2 horizontal --> 30.0665927567

from math import sqrt


def direction_splitter(directions, letter_options):
    result_list = []
    current_direction = {
        "steps": "",
        "direction": ""
    }

    for value in directions:
        #check if value is a letter
        if value in letter_options:
            # if it is, append it to current_direction[direction]
            #Append current_direction to result_list
            #Reset current direction
            current_direction["direction"] = value
            result_list.append(current_direction)
            current_direction = {
                "steps": "",
                "direction": ""
            }
        # else, we're still working on a direction
            #append the value to current_direction[steps]
            #append like a string for now, will convert to int later
        else:
            current_direction["steps"] += value
    return result_list

def calculate_distance(list_of_steps):
    # At this point, list_of_steps is a list of dictionaries
    # Each has DIRECTION (str) and STEPS (str)
    # Iterate through list, determine if + or -, and vertical or horizontal
    total_steps = {
        "vertical": 0,
        "horizontal": 0
    }
    for individual_step in list_of_steps:
        direction = individual_step["direction"]
        steps = int(individual_step["steps"])
        match direction:
            case "B":
                total_steps["vertical"] -= steps
            case "F":
                total_steps["vertical"] += steps
            case "R":
                total_steps["horizontal"] += steps
            case "L":
                total_steps["horizontal"] -= steps
    return total_steps

def hypotenuse_calculator(a, b):
    c_squared = a ** 2 + b ** 2
    c = sqrt(c_squared)
    return c

def run_simulation(directions_string):
    possible_directions = "LRFB"
    split_directions = direction_splitter(directions_string, possible_directions)
    total_distance_dict = calculate_distance(split_directions)
    total_distance_value = hypotenuse_calculator(total_distance_dict["horizontal"], total_distance_dict["vertical"])
    return total_distance_value