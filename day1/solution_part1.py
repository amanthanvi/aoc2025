# Init "lock dial" array
# Dial is from 0 to 99
dial_array = list(range(100))

# Dial position starts at 50 always, dial is 0-99 so 50 is idx 50
dial_position = dial_array[50]

# Dial is circular, so moving left from 0 goes to 99 and moving right from 99 goes to 0
# Python lists handle this naturally with negative indexing and modulo operations

print(dial_array)
print("Initial dial position:", dial_position)

# The actual password we are trying to find is the number of times the dial is
# left pointing at 0 after any rotation in the sequence

# From the example suppose the attached document contained the following rotations:
# L68 L30 R48 L5 R60 L55 L1 L99 R14 L82
# Using the first rotation as an example
#
# The dial starts by pointing at 50. The dial is rotated L68 to point at 82.
# We try: dial_position = dial_array[dial_position - 68]
# print("Dial position after L68:", dial_position) : Dial position after L68: 82

# However this does not work for all cases because of the circular nature of the dial.
# For example, if we try to rotate L60 from 10:
# dial_position = dial_array[10 - 60] would give us dial_array[-50] which is 50, not 50 positions left of 10.
# Instead we need to use modulo to wrap around the dial correctly.

# For example, if we try to rotate L151 from 50:
# dial_position = dial_array[(50 - 151) % 100]] would give us dial_array[-101]
# which is out of bounds given the size of the dial_array, which is 100.

# Instead we need to use modulo to wrap around the dial correctly.
# dial_array[(50 - 151) % 100] = dial_array[the remainder of -101 divided by 100] which = dial_array[-1] = 99


# We can implement a function to handle the rotations
def rotate_dial(direction, distance):
    return (
        dial_array[(dial_position - distance) % 100]
        if direction == "L"
        else dial_array[(dial_position + distance) % 100]
    )


# We need to read the input from a file
with open("input.txt", "r") as file:
    rotations = file.read().strip().split()

# Initialize count of times dial points at 0
count_dial_at_zero = 0

for rotation in rotations:
    direction, distance = rotation[0], int(rotation[1:])
    dial_position = rotate_dial(direction, distance)
    if dial_position == dial_array[0]:
        count_dial_at_zero += 1

print(
    "Number of times dial points at 0:", count_dial_at_zero
)  # Result is 1172 which is correct!
