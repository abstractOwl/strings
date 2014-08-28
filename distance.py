#!/usr/bin/env python

"""
Demonstrates the use of the Levenstein distance for command suggestion.
"""

def levenstein(first, second):
    """
    Returns the Levenstein distance between two given strings.

    @param {string} first   - First string
    @param {string} second  - Second string
    """
    if min(len(first), len(second)) == 0:
        return max(len(first), len(second))

    cost = 0 if first[-1:] == second[-1:] else 1

    return min(levenstein(first[:-1], second) + 1,
               levenstein(first, second[:-1]) + 1,
               levenstein(first[:-1], second[:-1]) + cost)

def usage(commands):
    """
    Prints the usage information.

    @param {list} commands - List of commands
    """
    print "distance.py: calculates the distance between a word and a set " + \
            "predefined commands."
    print "usage: python distance.py <word>"
    print "\nCommands:"
    for command in commands:
        print "  %s" % command

def test(func, test_str, commands):
    """
    Returns a list of distances between a specified word and the given set of
    commands.

    @param {function} fn       - Distance metric to use
    @param {string}   test_str - String to test
    @param {list}     commands - Given list of commands
    """
    return [(command, func(test_str, command)) for command in commands]

def main(commands):
    """
    The driver function.

    @param {list} commands - List of commands to check distances against
    """
    same_cmd = "Got %s, which is a valid command (%d units away)."
    diff_cmd = "Did you mean %s (%d units away)?"

    print "Levenstein:",
    closest = min(test(levenstein, sys.argv[1], commands), key=lambda x: x[1])
    print (same_cmd if closest[1] == 0 else diff_cmd) % closest

if __name__ == '__main__':
    import sys

    COMMANDS = ['abort', 'help', 'pause', 'quit', 'resume', 'start', 'stop']

    if len(sys.argv) != 2:
        usage(COMMANDS)
    else:
        main(COMMANDS)

    print

