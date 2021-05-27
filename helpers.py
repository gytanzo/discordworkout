# This python file just contains the various helper functions. 
import re

# Thanks to Matt from this Stackoverflow post: https://stackoverflow.com/questions/30926840/how-to-check-change-between-two-values-in-percent/30926930
def get_change(current, previous):
    if current == previous:
        return 0
    try:
        return round((abs(current - previous) / previous) * 100.0, 2)
    except ZeroDivisionError:
        return float('inf')

# Determins if a string contains numbers. 
def has_numbers(input_string):
    return any(char.isdigit() for char in input_string)

# Given a TM and a percentage, returns how much to do. 
def convert(x, percentage, reps, base=5):
    decimal_percent = percentage * .01
    val = x * decimal_percent
    rounded = str(base * round(val / base))
    return rounded + " x" + str(reps)

# Checks if the user sent a valid unit of measurement.
def check_unit(m):
    if m.content.lower() in ("kg", "lb"):
        return True

# Checks for a yes or a no. 
def check_confirmation(m):
    if m.content.lower() in ("yes", "no"):
        return True

# Checks if the user sent a valid number. 
def check_number(m):
    return m.content.isnumeric()

# Checks what kind of workout the user wants. 
def check_day(m):
    if m.content.lower() in ("four", "five", "six", "4", "5", "6"):
        return True

def convert_day_to_int(val):
    if val == "4":
        return "four"
    elif val == "5":
        return "five"
    elif val == "6":
        return "six"
    return val

# A check function to ensure a valid number of reps was sent. 
def check_reps(m):
    # This will support two formats: [int] or [int] rep/reps. 

    # Let's check for just an integer first. 
    if m.content.isnumeric():
        return True

    # Next, check for if the user sent something in the format of [int] rep. 
    elif has_numbers(m.content) and re.search('rep', m.content, re.IGNORECASE) is not None:
        return True

    return False