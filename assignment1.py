# Part A


import re


def names():
    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids."""
    # YOUR CODE HERE
    name = re.findall('[A-Z][\w]{1,4}', simple_string)
    return name


if len(names()) == 4:
    print("There are four names in the simple_string")
assert len(names()) == 4, "There are four names in the simple_string"


# Part B