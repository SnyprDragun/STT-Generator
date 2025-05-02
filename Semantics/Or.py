#!/opt/homebrew/bin/python3.11
'''Class for 'or' STL semantic'''
from Root.Solver import*
from Semantics.STL import*
from Specification.Specification import*

class OR(STL):
    def __init__(self, identifier, *instances):
        self.choice = None
        self.instances = instances
        self.return_value = True
        a_instance = STL.get_instance(identifier)
        if a_instance:
            self.main = a_instance.main
        else:
            raise ValueError(f"No instance found for identifier '{identifier}'")

        self.reach_or_targets = []
        self.avoid_or_targets = []
        self.stay_or_targets = []

        from Semantics.Semantics import EVENTUALLY, ALWAYS
        for instance in self.instances:
            if isinstance(instance, EVENTUALLY) or isinstance(instance, ALWAYS):
                if isinstance(instance.task, REACH):
                    self.reach_or_targets.append(instance.task.local_setpoint)
                elif isinstance(instance.task, AVOID):
                    self.avoid_or_targets.append(instance.task.local_obstacle)
                elif isinstance(instance.task, STAY):
                    self.stay_or_targets.append(instance.task.local_setpoint)
                else:
                    print("Other instance: ", self.instances)

        self.all_or_targets = self.reach_or_targets + self.avoid_or_targets + self.stay_or_targets
        self.choice = random.randint(0, len(self.all_or_targets) - 1)
        # self.goal = [3, 4]
        # self.goal = [12, 15, 12, 15, 12, 15]

    def add_resultant(self):
        from Semantics.Semantics import EVENTUALLY, ALWAYS, AND, OR, NOT, IMPLIES, UNTIL
        for instance in self.instances:
            if isinstance(instance, EVENTUALLY) or isinstance(instance, ALWAYS):
                if self.choice == self.instances.index(instance):
                    print("OR reach-target options: ", self.reach_or_targets)
                    print("choice: ", self.choice)
                    all_constraints = self.instances[self.choice].call()

                for constraint in all_constraints:
                    self.main.solver.add(constraint)

            elif isinstance(instance, AND):
                for constraint in instance.call():
                    self.main.solver.add(constraint)

            elif isinstance(instance, OR):
                self.main.solver.add(instance.call())

            elif isinstance(instance, NOT) or isinstance(instance, IMPLIES) or isinstance(instance, UNTIL) or isinstance(instance, REACH) or isinstance(instance, AVOID) or isinstance(instance, STAY):
                print(instance.__class__.__name__, "is not handeled for OR")

            else:
                print("Unknown instance")

    def return_resultant(self):
        all_constraints = []
        from Semantics.Semantics import EVENTUALLY, ALWAYS, AND, OR, NOT, IMPLIES, UNTIL
        for instance in self.instances:
            if isinstance(instance, EVENTUALLY) or isinstance(instance, ALWAYS):
                if self.choice == self.instances.index(instance):
                    print("OR reach-target options: ", self.reach_or_targets)
                    print("choice: ", self.choice)
                    all_constraints = self.instances[self.choice].call()

            elif isinstance(instance, AND):
                for constraint in instance.call():
                    all_constraints.append(constraint)

            elif isinstance(instance, OR):
                all_constraints = instance.call()

            elif isinstance(instance, NOT) or isinstance(instance, IMPLIES) or isinstance(instance, UNTIL) or isinstance(instance, REACH) or isinstance(instance, AVOID) or isinstance(instance, STAY):
                print(instance.__class__.__name__, "is not handeled for OR")

            else:
                print("Unknown instance")

        return all_constraints

    def call(self):
        if self.return_value == True:
            return self.return_resultant()
        else:
            self.add_resultant()
