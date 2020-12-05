#!/usr/bin/env python3

# Created by: Wenda Zhao
# Created on: Dec 2020
# This program guessing random number


import random


def main():
    # this function guessing random number
    some_variable = str(random.randint(0, 1))   # a number between 0 and 1

    # input
    your_number = input("Enter your number (between 0 and 1): ")
    print("")

    # process
    if your_number == some_variable:
        # output
        print("You are correct!")
    else:
        print("You are wrong, the answer is {0}".format(some_variable))
    try:
        integer_as_number = int(your_number)
        print("You entered an integer correctly")
    except Exception:
        print("This was not an integer")
    finally:
        print("Thanks for playing")


if __name__ == "__main__":
    main()
