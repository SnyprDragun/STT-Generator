#!/opt/homebrew/bin/python3.11
'''Class for 'always' STL semantic'''
from Root.Solver import*
from Semantics.STL import*
from Specification.Specification import*

class ALWAYS(STL):
    def __init__(self, identifier, t1, t2, task):
        task.always = True
        self.identifier = identifier
        task.t1 = t1
        task.t2 = t2
        self.task = task
        self.return_value = True
        a_instance = STL.get_instance(identifier)
        if a_instance:
            self.main = a_instance.main
        else:
            raise ValueError(f"No instance of A found for identifier '{identifier}'")

    def add_resultant(self):
        '''adds constraints'''
        from Semantics.Semantics import EVENTUALLY, IMPLIES, UNTIL, NOT
        if isinstance(self.task, REACH) or isinstance(self.task, AVOID) or isinstance(self.task, STAY):
            constraints = self.task.call()
            for constraint in constraints:
                self.main.solver.add(constraint)
        elif isinstance(self.task, EVENTUALLY):
            eventually = self.task
            eventually_duration = eventually.task.t2 - eventually.task.t1
            current_time = eventually.t1

            while current_time < eventually.t2:
                next_time = min(current_time + eventually_duration, eventually.t2)
                constraints = EVENTUALLY(self.identifier, current_time, next_time, eventually.task).call()
                for constraint in constraints:
                    self.main.solver.add(constraint)
                current_time = next_time

        elif isinstance(self.task, ALWAYS) or isinstance(self.task, IMPLIES) or isinstance(self.task, UNTIL) or isinstance(self.task, NOT):
            print(self.task.__class__.__name__, "not handeled for ALWAYS")
        else:
            print("Unknown Instance")

    def return_resultant(self):
        '''returns constraints'''
        all_constraints =[]
        from Semantics.Semantics import EVENTUALLY, IMPLIES, UNTIL, NOT
        if isinstance(self.task, REACH) or isinstance(self.task, AVOID) or isinstance(self.task, STAY):
            constraints = self.task.call()
            for constraint in constraints:
                all_constraints.append(constraint)
        elif isinstance(self.task, EVENTUALLY):
            eventually = self.task
            eventually_duration = eventually.task.t2 - eventually.task.t1
            current_time = eventually.t1

            while current_time < eventually.t2:
                next_time = min(current_time + eventually_duration, eventually.t2)
                all_constraints.append(EVENTUALLY(self.identifier, current_time, next_time, eventually.task).call())
                current_time = next_time

        elif isinstance(self.task, ALWAYS) or isinstance(self.task, IMPLIES) or isinstance(self.task, UNTIL) or isinstance(self.task, NOT):
            print(self.task.__class__.__name__, "not handeled for ALWAYS")
        else:
            print("Unknown Instance")
        return all_constraints

    def call(self):
        if self.return_value == True:
            return self.return_resultant()
        else:
            self.add_resultant()
