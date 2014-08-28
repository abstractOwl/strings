# Strings
Implementations/experiments of various string algorithms

## distance.py
Demonstrates using string distance metrics to correct typos in command input.

### Examples

    $ python distance.py 
    distance.py: calculates the distance between a word and a set predefined commands.
    usage: python distance.py <word>

    Commands:
      abort
      help
      pause
      quit
      resume
      start
      stop

    $ python distance.py abort
    Levenstein: Got abort, which is a valid command (0 units away).

    $ python distance.py stopping
    Levenstein: Did you mean stop (4 units away)?
