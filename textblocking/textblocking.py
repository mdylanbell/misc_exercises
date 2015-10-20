#!/usr/bin/env python

""" Exercise to convert a list of strings listed in left to right order to
    top to bottom order
"""


def invert_text(lines):
    """ Format a list of strings so they read from top to bottom instead of
        left to right.
    """

    output = []

    for line_number, line in enumerate(lines):
        for i, character in enumerate(line):
            if line_number == 0:
                output.append(character)
            else:
                output[i] = output[i] + character

    return output


def invert_text_strict(lines):
    """ Strict version of invert_text with input checking """

    output = []

    if len(lines) > 50:
        raise ValueError("List argument contains too many elements")

    line_length = len(lines[0])

    for line_number, line in enumerate(lines):
        if not line.isupper():
            raise ValueError("List argument contains improperly formatted " +
                             "elements (case) -- line {0}"
                             .format(line_number + 1))

        if len(line) != line_length:
            raise ValueError("List argument contains improperly formatted " +
                             "elements (line length) -- line {0}"
                             .format(line_number + 1))

        for i, character in enumerate(line):
            if line_number == 0:
                output.append(character)
            else:
                output[i] = output[i] + character

    return output
