#!/opt/homebrew/bin/python3.11
'''Class for 'not' STL semantic'''
from Root.Solver import*
from Semantics.STL import*
from Specification.Specification import*

class NOT(STL):
    def __init__(self, identifier, *instances):
        self.instances = instances
        self.return_value = True
        a_instance = STL.get_instance(identifier)
        if a_instance:
            self.main = a_instance.main
        else:
            raise ValueError(f"No instance of A found for identifier '{identifier}'")

    def add_resultant(self):
        '''adds constraints'''
        from Semantics.Semantics import ALWAYS, EVENTUALLY, AND, OR
        for instance in self.instances:
            if isinstance(instance, EVENTUALLY) or isinstance(instance, ALWAYS) or isinstance(instance, AND):
                instance.return_value = True
                constraints = instance.call()
                for constraint in constraints:
                    self.main.solver.add(z3.Not(constraint))
            elif isinstance(instance, OR):
                constraints = instance.call()
                self.main.solver.add(z3.Not(constraints))
            else:
                print("Unknown Instance")

    def return_resultant(self):
        '''returns constraints'''
        all_constraints =[]
        from Semantics.Semantics import ALWAYS, EVENTUALLY, AND, OR
        for instance in self.instances:
            if isinstance(instance, EVENTUALLY) or isinstance(instance, ALWAYS) or isinstance(instance, AND):
                instance.return_value = True
                constraints = instance.call()
                for constraint in constraints:
                    all_constraints.append(z3.Not(constraint))
            elif isinstance(instance, OR):
                constraints = instance.call()
                all_constraints.append(z3.Not(constraints))
            else:
                print("Unknown Instance")
        return all_constraints

    def call(self):
        if self.return_value == True:
            return self.return_resultant()
        else:
            self.add_resultant()
