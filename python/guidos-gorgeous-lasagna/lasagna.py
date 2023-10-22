"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define the 'EXPECTED_BAKE_TIME' constant.
def EXPECTED_BAKE_TIME():
    '''constant that returns how many minutes the lasagna should bake in the oven.'''
    timeCooking = 40
    return timeCooking

#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    if not elapsed_bake_time.isdigit():
        print("Value must be a digit. Try again.")
        elapsed_bake_time = input("Elapsed bake time: ")
    else:
        elapsed_bake_time = int(elapsed_bake_time)
        time_remaining = EXPECTED_BAKE_TIME() - elapsed_bake_time
        return time_remaining
    pass


#TODO: Define the 'preparation_time_in_minutes()' function below.
# You might also consider using 'PREPARATION_TIME' here, if you have it defined.
def preparation_time_in_minutes(number_of_layers):
    """This function that takes the number of layers you want to add to the lasagna as an argument and returns how many minutes you would spend making them. 1 layer = 2 minutes"""
    if not number_of_layers.isdigit():
        print("Value must be a digit. Try again.")
        number_of_layers = input("How many layers do you want to do? -> ")
    else:
        number_of_layers = int(number_of_layers)
        preparation_time = number_of_layers * 2
        return preparation_time


#TODO: define the 'elapsed_time_in_minutes()' function below.
# Remember to add a docstring (you can copy and then alter the one from bake_time_remaining.)
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """This function takes two integers representing the number of lasagna layers and thetime already spent baking and calculates the total elapsed minutes spent cooking the lasagna."""
    number_of_layers = preparation_time_in_minutes(number_of_layers)
    elapsed_bake_time = bake_time_remaining(elapsed_bake_time)
    result = number_of_layers + elapsed_bake_time
    return result

number_of_layers = input("How many layers do you want to do? -> ")
elapsed_bake_time = input("How much elapsed bake time is going on? -> ")
print(f"Time remaining: {elapsed_time_in_minutes(number_of_layers, elapsed_bake_time)}")    
