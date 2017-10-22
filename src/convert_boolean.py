"""Convert boolean - Return for True a Yes string and False a No string

#1 Best Practices Solution by jamiecollinson, thecodeboss, warwickwang, Bandicoot, cvk77, zerothehero33 (plus 685 more warriors)

def bool_to_word(bool):
    return "Yes" if bool else "No"
"""

def bool_to_word(bool):
    if bool == True:
        return 'Yes'
    else:
        return 'No'