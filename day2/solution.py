### --- START PART 1 --- ###
import re

# Read in the input file, save the ranges as a list of tuples to make it easier
# to work with
with open("input.txt", "r") as file:
    ranges_list = file.read().strip().split(",")
# print(ranges_list)

# Convert the ranges to tuples
# The ranges are separated by commas, each range gives its first ID and last
# ID separated by a dash.
ranges_tuples = [tuple(map(int, range.split("-"))) for range in ranges_list]
# print(ranges_tuples)

# Any ID is invalid if it is made only of some sequence of digits repeated twice
# Examples: 55 (5 twice), 6464 (64 twice), and 123123 (123 twice) would all be
# invalid IDs

# None of the numbers have leading zeroes; 0101 isn't an ID at all
# (101 is a valid ID that we would ignore)

# We need to find all of the invalid IDs that appear in the given ranges.
invalid_ids = []


def is_invalid_id(id):
    # If any sequence of stringified digits is repeated twice (hence the * 2),
    # then the ID is invalid.
    # The range(2) is because we want to check if the sequence is strictly
    # repeated twice.
    # We will use regex to check for this pattern

    # First, convert the ID to a string
    id_str = str(id)

    # Make the regex pattern to check for repeated sequences
    # Re pseudo-code: pattern = if any sequence of digits is repeated exactly twice
    # Pattern: entire string is some sequence repeated exactly twice
    # (.+) captures any sequence, \1 matches the same sequence again

    # From https://regex101.com/, I used the builder and pulled the following explanations:
    # ^ asserts position at start of a line
    # 1st Capturing Group (.+)
    # . matches any character (except for line terminators)
    # + matches the previous token between one and unlimited times, as many
    # times as possible, giving back as needed (greedy)
    # \1 matches the same text as most recently matched by the 1st capturing group
    # $ asserts position at the end of a line
    pattern = r"^(.+)\1$"

    # Use re.match to see if the pattern matches the entire ID string
    if re.match(pattern, id_str):
        return True
    else:
        return False


for x, y in ranges_tuples:
    # Step through each ID in the range by incrementing by 1, inclusive of the last ID
    for i in range(x, y + 1):
        if is_invalid_id(i):
            invalid_ids.append(i)

print("Invalid IDs:", len(invalid_ids))
print(invalid_ids)
print("Sum of invalid IDs:", sum(invalid_ids))

# Yields 15873079081 which is the correct answer!

### --- END PART 1 --- ###

### --- START PART 2 --- ###
# Reset our variables
invalid_ids = []
