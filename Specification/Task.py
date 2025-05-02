#!/opt/homebrew/bin/python3.11
'''Parent class for REACH, AVOID and STAY classes '''
from Root.Dependencies import*

class TASK():
    '''This class helps you select depth of computation for generating STTs, for given reach-avoid-stay specification.
    \nDepth - "minimum" : for fastest result generation, ensures only midpoint of Tube satisfies all constraints; highly inaccurate for formal purposes.
    \nDepth - "partial" : recommended for pratical purposes, ensures all boundary points of Tube satisfy all constraints; near accurate results.
    \nDepth - "full" : highly time consuming even for simple examples, ensures all interior and boundary points of Tube satisfy all constraints.'''

    depths = ["full", "partial", "minimum"]

    def __init__(self):
        self.eventually = False
        self.always = False
        self.implies = False
        self.start = time.time()
        self.depth = "partial"
