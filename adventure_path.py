# Adventurer Path to Calculate

# *The directions are provided in the number of steps first and the direction second. For example, 6F indicates 6 steps forward. Other possible directions are B for backward, R for to the right, and finally, L for to the left.*

## Directions to Use

# `15F6B6B5L16R8B16F20L6F13F11R`

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
directions_to_parse = "15F6B6B5L16R8B16F20L6F13F11R"
possible_directions = "LRFB"

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
    for direction in result_list:
        print(direction)

direction_splitter(directions_to_parse, possible_directions)
