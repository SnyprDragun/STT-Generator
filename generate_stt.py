#!/opt/homebrew/bin/python3.11
from Root.Solver import*
from Semantics.Semantics import*
from Specification.Specification import*


#---------------------------------- RANDOM EXAMPLE ----------------------------------#

# semantic: ◊S ∧ (◊T1 ∨ ◊T2) ∧ ◊G ∧ (□ ¬O)

stl_obj = STL(1, STT_Solver(5, 3, 0.5, 2.5, 3))
specification = AND(1, EVENTUALLY(1, 0, 1, REACH(stl_obj.main, -1, 2, -1, 2, 1, 4)), 
                        EVENTUALLY(1, 14, 15, REACH(stl_obj.main, 12, 15, 12, 15, 12, 15)),
                        OR(1, 
                            EVENTUALLY(1, 7, 8, REACH(stl_obj.main, 9, 12, 6, 9, 6, 9)), 
                            EVENTUALLY(1, 7, 8, REACH(stl_obj.main, 3, 6, 6, 9, 6, 9))
                        ),
                        ALWAYS(1, 0, 15, AVOID(stl_obj.main, 6, 9, 6, 11, 0, 15)),
                    )

specification.return_value = False
specification.call()
stl_obj.plotter()

#------------------------------------------------------------------------------------#

