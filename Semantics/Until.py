#!/opt/homebrew/bin/python3.11
'''Class for 'until' STL semantic'''
from Root.Solver import*
from Semantics.STL import*
from Specification.Specification import*

class UNTIL(STL):
    def __init__(self, identifier, instance_a, instance_b):
        self.instance_a = instance_a
        self.instance_b = instance_b
        self.return_value = True
        a_instance = STL.get_instance(identifier)
        if a_instance:
            self.main = a_instance.main
        else:
            raise ValueError(f"No instance of A found for identifier '{identifier}'")

    def add_resultant(self):
        '''adds constraints'''
        pass

    def return_resultant(self):
        '''returns constraints'''
        pass

    def call(self):
        if self.return_value == True:
            return self.return_resultant()
        else:
            self.add_resultant()
