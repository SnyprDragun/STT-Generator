#!/opt/homebrew/bin/python3.11
'''Class for 'implies' STL semantic'''
from Root.Solver import*
from Semantics.STL import*
from Specification.Specification import*

class IMPLIES(STL):
    def __init__(self, identifier, instance_a, instance_b):
        self.instance_a = instance_a
        self.instance_b = instance_b
        self.return_value = True
        a_instance = STL.get_instance(identifier)
        if a_instance:
            self.main = a_instance.main
        else:
            raise ValueError(f"No instance of A found for identifier '{identifier}'")

    def call(self):
        all_constraints_a = []
        all_constraints_b = []
        implies_constraint = []

        from Semantics.Semantics import ALWAYS, EVENTUALLY, AND, OR
        if isinstance(self.instance_a, EVENTUALLY) or isinstance(self.instance_a, ALWAYS):
            constraints = self.instance_a.call()
            for constraint in constraints:
                all_constraints_a.append(constraint)
        elif isinstance(self.instance_a, AND):
            self.instance_a.return_value = True
            constraints = self.instance_a.call()
            for constraint in constraints:
                all_constraints_a.append(constraint)
        elif isinstance(self.instance_a, OR):
            constraints = self.instance_a.call()
            all_constraints_a.append(constraints)
        else:
            print("Unknown Instance")

        if isinstance(self.instance_b, EVENTUALLY) or isinstance(self.instance_b, ALWAYS):
            constraints = self.instance_b.call()
            for constraint in constraints:
                all_constraints_b.append(constraint)
        elif isinstance(self.instance_b, AND):
            self.instance_b.return_value = True
            constraints = self.instance_b.call()
            for constraint in constraints:
                all_constraints_b.append(constraint)
        elif isinstance(self.instance_b, OR):
            constraints = self.instance_b.call()
            all_constraints_b.append(constraints)
        else:
            print("Unknown Instance")

        for i in range(len(all_constraints_a)):
            for j in range(len(all_constraints_b)):
                implies_constraint.append(z3.Or(z3.Not(all_constraints_a[i]), all_constraints_b[j]))

        if self.return_value == True:
            return implies_constraint
        else:
            for i in implies_constraint:
                self.main.solver.add(i)
