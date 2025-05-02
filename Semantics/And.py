#!/opt/homebrew/bin/python3.11
'''Class for 'and' STL semantic'''
from Root.Solver import*
from Semantics.STL import*
from Specification.Specification import*

class AND(STL):
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
        for instance in self.instances:
            from Semantics.Semantics import EVENTUALLY, ALWAYS, OR, IMPLIES
            if isinstance(instance, EVENTUALLY) or isinstance(instance, ALWAYS) or isinstance(instance, AND) or isinstance(instance, IMPLIES):
                instance.return_value = True
                constraints = instance.call()
                for constraint in constraints:
                    self.main.solver.add(constraint)
            elif isinstance(instance, OR):
                constraints = instance.call()
                self.main.solver.add(constraints)
            else:
                print("Unknown Instance")

    def return_resultant(self):
        '''returns constraints'''
        all_constraints =[]
        for instance in self.instances:
            from Semantics.Semantics import EVENTUALLY, ALWAYS, OR
            if isinstance(instance, EVENTUALLY) or isinstance(instance, ALWAYS) or isinstance(instance, AND):
                instance.return_value = True
                constraints = instance.call()
                for constraint in constraints:
                    all_constraints.append(constraint)
            elif isinstance(instance, OR):
                constraints = instance.call()
                all_constraints.append(constraints)
            else:
                print("Unknown Instance")
        return all_constraints

    def call(self):
        if self.return_value == True:
            return self.return_resultant()
        else:
            self.add_resultant()
