#################################
# File: asgn4_module.py
# Name: Brady Peneton
# Assignment: 4
#################################

"""
This module tests whether a field is a number or is blank
"""

def is_field_blank(varfield):
    if varfield == "":
        return True
    else:
        return False


def is_field_a_number(numfield):
    if numfield.isnumeric() == True:
        return True
    else:
        return False
