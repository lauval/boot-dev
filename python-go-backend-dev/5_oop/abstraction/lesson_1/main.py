"""Assignment
We don't want our coworkers at Age of Dragons Studios™ to have to worry about
how Humans move. We'll abstract that away from them by encapsulating the
private __pos_x, __pos_y, and __speed variables behind some simple methods.

Complete the following methods in the Human class:

move_right(): Adds the human's speed to its x position.
move_left(): Subtracts the human's speed from its x position.
move_up(): Adds the human's speed to its y position.
move_down(): Subtracts the human's speed from its y position.
get_position(): Returns the x position and y position as a tuple."""


class Human:
    def __init__(self, pos_x, pos_y, speed):
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__speed = speed

    def move_right(self):
        self.__pos_x += self.__speed

    def move_left(self):
        self.__pos_x -= self.__speed

    def move_up(self):
        self.__pos_y += self.__speed

    def move_down(self):
        self.__pos_y -= self.__speed

    def get_position(self):
        return (self.__pos_x, self.__pos_y)


###########################
# test our implementation #
###########################

run_cases = [
    (0, 0, 5, "left", -5, 0),
    (0, 0, 5, "right", 5, 0),
    (0, 0, 5, "up", 0, 5),
]

submit_cases = run_cases + [
    (0, 0, 5, "down", 0, -5),
    (10, 10, 2, "left", 8, 10),
    (10, 10, 2, "right", 12, 10),
    (10, 10, 2, "up", 10, 12),
    (10, 10, 2, "down", 10, 8),
]


def test(pos_x, pos_y, speed, move_direction, expected_output_x, expected_output_y):
    print("---------------------------------")
    print("Inputs:")
    print(f" * pos_x: {pos_x}")
    print(f" * pos_y: {pos_y}")
    print(f" * speed: {speed}")
    print(f" * move_direction: {move_direction}")
    expected_output = (expected_output_x, expected_output_y)
    human = Human(pos_x, pos_y, speed)
    if move_direction == "left":
        human.move_left()
    elif move_direction == "right":
        human.move_right()
    elif move_direction == "up":
        human.move_up()
    elif move_direction == "down":
        human.move_down()
    result = human.get_position()
    print(f"Expected x: {expected_output_x}")
    print(f"Actual   x: {result[0]}")
    print(f"Expected y: {expected_output_y}")
    print(f"Actual   y: {result[1]}")
    if result == expected_output:
        return True
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            print("Pass")
            passed += 1
        else:
            print("Fail")
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
