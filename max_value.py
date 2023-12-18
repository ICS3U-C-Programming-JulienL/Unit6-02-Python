#!/usr/bin/env python3

# Created By: Julien Lamoureux
# Date: December 17, 2023
# This program display the maximum of 10 values

import random
import constants


def max_value(list_of_int):
    max = 0
    # use a for loop when counter < ARRAY_SIZE
    for counter in range(0, len(list_of_int)):
        # if list_of_counter[] is greater than max, make list_of_int_counter the max
        if list_of_int[counter] > max:
            max = list_of_int[counter]
    # return the max
    return max


def main():
    # set random_numbers to [] and max to 0
    random_numbers = []
    max = 0

    # tell the user what the program does
    print("This program display the maximum value of the following values :")

    # use a for loop when counter < ARRAY_SIZE
    for counter in range(0, constants.ARRAY_SIZE):
        # generate a random number
        rand_num = random.randint(constants.MIN, constants.MAX)

        # append random_numbers  to the random number
        random_numbers.append(rand_num)

        # display random_numbers[counter]
        print(random_numbers[counter])

    # call the max_value function
    max = max_value(random_numbers)

    # display the max value
    print("The max is {}.".format(max))


if __name__ == "__main__":
    main()
