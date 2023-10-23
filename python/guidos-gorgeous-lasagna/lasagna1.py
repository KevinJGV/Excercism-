"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

def expected_bake_time():
    '''constant that returns how many minutes the lasagna should bake in the oven.'''
    time_cooking = 40
    return time_cooking


def bake_time_remaining(elapsed_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    elapsed_time = int(elapsed_time)
    time_remaining = expected_bake_time() - elapsed_time
    return time_remaining


def preparation_time_in_minutes(time):
    """This function that takes the number of layers you want to add to the lasagna as an argument and returns how many minutes you would spend making them. 1 layer = 2 minutes"""
    time = int(time)
    preparation_time = time * 2
    return preparation_time


def elapsed_time_in_minutes(preparation, bake):
    """This function takes two integers representing the number of lasagna layers and thetime already spent baking and calculates the total elapsed minutes spent cooking the lasagna."""
    preparation = preparation_time_in_minutes(preparation)
    bake = bake_time_remaining(bake)
    result = preparation + bake
    return result


number_of_layers = input("How many layers do you want to do? -> ")
elapsed_bake_time = input("How much elapsed bake time is going on? -> ")
print(f"Time remaining: {elapsed_time_in_minutes(number_of_layers, elapsed_bake_time)}")
