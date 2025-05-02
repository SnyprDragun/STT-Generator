#!/opt/homebrew/bin/python3.11
'''Class for 'eventually' STL semantic'''
from Root.Solver import*
from Semantics.STL import*
from Specification.Specification import*

class EVENTUALLY(STL):
    def __init__(self, identifier, t1, t2, task):
        task.eventually = True
        task.t1 = t1
        task.t2 = t2
        self.task = task
        self.return_value = True
        self.identifier = identifier
        a_instance = STL.get_instance(identifier)
        if a_instance:
            self.main = a_instance.main
        else:
            raise ValueError(f"No instance of A found for identifier '{identifier}'")

    def add_resultant(self):
        '''adds constraints'''
        from Semantics.Semantics import ALWAYS, IMPLIES, UNTIL, NOT
        if isinstance(self.task, REACH) or isinstance(self.task, AVOID) or isinstance(self.task, STAY):
            constraints = self.task.call()
            for constraint in constraints:
                self.main.solver.add(constraint)
        elif isinstance(self.task, ALWAYS):
            always = self.task
            if isinstance(always.task, REACH) or isinstance(always.task, STAY):
                if self.main.dimension == 1:
                    constraints = EVENTUALLY(self.identifier, always.t1, always.t2, STAY(always.task.main, always.task.x1, always.task.x2)).call()
                elif self.main.dimension == 2:
                    constraints = EVENTUALLY(self.identifier, always.t1, always.t2, STAY(always.task.main, always.task.x1, always.task.x2, always.task.y1, always.task.y2)).call()
                else:
                    constraints = EVENTUALLY(self.identifier, always.t1, always.t2, STAY(always.task.main, always.task.x1, always.task.x2, always.task.y1, always.task.y2, always.task.z1, always.task.z2)).call()
            elif isinstance(always.task, AVOID):
                if self.main.dimension == 1:
                    constraints = EVENTUALLY(self.identifier, always.t1, always.t2, AVOID(always.task.main, always.task.x1, always.task.x2)).call()
                elif self.main.dimension == 2:
                    constraints = EVENTUALLY(self.identifier, always.t1, always.t2, AVOID(always.task.main, always.task.x1, always.task.x2, always.task.y1, always.task.y2)).call()
                else:
                    constraints = EVENTUALLY(self.identifier, always.t1, always.t2, AVOID(always.task.main, always.task.x1, always.task.x2, always.task.y1, always.task.y2, always.task.z1, always.task.z2)).call()

            for constraint in constraints:
                self.main.solver.add(constraint)
        elif isinstance(self.task, EVENTUALLY) or isinstance(self.task, IMPLIES) or isinstance(self.task, UNTIL) or isinstance(self.task, NOT):
            print(self.task.__class__.__name__, "not handeled for EVENTUALLY")
        else:
            print("Unknown Instance")

    def return_resultant(self):
        '''returns constraints'''
        all_constraints =[]
        from Semantics.Semantics import ALWAYS, IMPLIES, UNTIL, NOT
        if isinstance(self.task, REACH) or isinstance(self.task, AVOID) or isinstance(self.task, STAY):
            constraints = self.task.call()
            for constraint in constraints:
                all_constraints.append(constraint)
        elif isinstance(self.task, ALWAYS):
            always = self.task
            if isinstance(always.task, REACH) or isinstance(always.task, STAY):
                if self.main.dimension == 1:
                    constraints = EVENTUALLY(self.identifier, always.t1, always.t2, STAY(always.task.main, always.task.x1, always.task.x2)).call()
                elif self.main.dimension == 2:
                    constraints = EVENTUALLY(self.identifier, always.t1, always.t2, STAY(always.task.main, always.task.x1, always.task.x2, always.task.y1, always.task.y2)).call()
                else:
                    constraints = EVENTUALLY(self.identifier, always.t1, always.t2, STAY(always.task.main, always.task.x1, always.task.x2, always.task.y1, always.task.y2, always.task.z1, always.task.z2)).call()
            elif isinstance(always.task, AVOID):
                if self.main.dimension == 1:
                    constraints = EVENTUALLY(self.identifier, always.t1, always.t2, AVOID(always.task.main, always.task.x1, always.task.x2)).call()
                elif self.main.dimension == 2:
                    constraints = EVENTUALLY(self.identifier, always.t1, always.t2, AVOID(always.task.main, always.task.x1, always.task.x2, always.task.y1, always.task.y2)).call()
                else:
                    constraints = EVENTUALLY(self.identifier, always.t1, always.t2, AVOID(always.task.main, always.task.x1, always.task.x2, always.task.y1, always.task.y2, always.task.z1, always.task.z2)).call()

            for constraint in constraints:
                all_constraints.append(constraint)
        elif isinstance(self.task, EVENTUALLY) or isinstance(self.task, IMPLIES) or isinstance(self.task, UNTIL) or isinstance(self.task, NOT):
            print(self.task.__class__.__name__, "not handeled for EVENTUALLY")
        else:
            print("Unknown Instance")
        return all_constraints

    def call(self):
        if self.return_value == True:
            return self.return_resultant()
        else:
            self.add_resultant()
