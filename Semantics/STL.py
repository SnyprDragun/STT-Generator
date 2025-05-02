#!/opt/homebrew/bin/python3.11
'''Parent class for AND, OR, NOT, EVENTUALLY, ALWAYS, UNTIL and IMPLIES classes '''
from Root.Solver import*
from Specification.Specification import*

class STL():
    '''This class initializes the solver and adds STL specification constraints to the it.
    \n Also keeps track of semantics pertaining to particular specification using identifiers.'''

    _instances = {}

    def __init__(self, identifier, main):
        self.main = main
        STL._instances[identifier] = self

    @classmethod
    def get_instance(cls, identifier):
        return cls._instances.get(identifier)

    def plotter(self):
        '''Runs the solver and plots the solution found.'''
        self.main.find_solution()
