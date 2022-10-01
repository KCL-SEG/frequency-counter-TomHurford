"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

# Pass a list of items to the function convert the list to a dictionary with the frequency of each item in the list convert all items in the list to strings

def frequencies(items):
    frequencies = {}
    
    for item in items:
        if str(item) in frequencies:
            frequencies[str(item)] += 1
        else:
            frequencies[str(item)] = 1
            
    return frequencies
