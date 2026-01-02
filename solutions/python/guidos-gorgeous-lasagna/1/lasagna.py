"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME=40
PREPARATION_TIME=2
#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(minutes):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    time_left=EXPECTED_BAKE_TIME-minutes
    return time_left


#TODO: Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.
def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes remaining.

    :param number_of_layers: int - the number of layers.
    :return: int - total minutes of preparation needed (in minutes) derived from 'PREPARATION_TIME'.

    Function that takes the layers the lasagna and the minutes it would take to prepare it as
    an argument and returns the total minutes of preparation time needed
    based on the `PREPARATION_TIME`.
    """
    total_minutes_of_preparation_needed=number_of_layers*2
    return total_minutes_of_preparation_needed


#TODO: define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed time for preparing the lasagna and the time that it has been sitting in the oven in minutes.

    :param number_of_layers: int - the number of layers.
    :param elapsed_bake_time: int - the time that the lasagna has been sitting in the oven cooking.
    :return: int - the total minutes preparaing and cooking the lasagna.

    Function that takes the layers the lasagna and the minutes it would take to prepare it as
    an argument and the elapsed baking time in minutes returns the total minutes that have passed preparing and baking.
    """
    total_min_left=preparation_time_in_minutes(number_of_layers)+elapsed_bake_time
    return total_min_left

# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
