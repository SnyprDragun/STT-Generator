# STT Generator
This toolbox follows a data-driven approach for generating Spatiotemporal Tubes. Signal Temporal Logic semantic is collected from user and z3 solver is used to solve for the constraints for reach-avoid-stay specifications.

## System Requirements
* Python 3.8 or greater
* Numpy, Matplotlib, PyTorch, Z3, Mpl_toolkits
* Windows/MacOS/Linux

## Start locally
* Clone the repo into your system.
* IMPORTANT: Change the shebang in all the files according to your system if different.
* Download and install system requirements if you are missing any. Quick way to find missing packages is by checking if all imports are seemless in `Root/Dependencies.py`.
* `generate_stt.py` is the main executable file, where user has to call relevant functions in proper format.
* An example snippet is given in `generate_stt.py` which should run seemlessly.

## More about the code
* `Solver.py` consists of various utility functions under `STT_Solver` class, containing the solver, plotter, etc., and some z3 skeletal code.
* `Specification` folder consists of `REACH`, `AVOID` and `STAY` classes. Objects of these classes have input parameters like x1, x2, y1, y2, ..... , t1, t2 along with an object reference of `STT_Solver` class. This is evident in the example code snippet.
* `Semantics` folder consists of various operators like `AND`, `EVENTUALLY`, `NOT`, etc., all child of class `STL`. These `STL` classes can have varied number and type of input parameters, along with a few fixed ones.
    * Required parameters include an `identifier` (integer), which must be same for all these class references and objects for a particular specification. (in the example code, all `STL` classes have identifier=1)
    * Next parameters can be instances of any other `STL` class. For exampples, there can be multiple `EVENTUALLY` items inside an `AND` or an `OR` item.
    * Some exceptions are not handled for, which have been listed below:
        * `EVENTUALLY` block can not have `EVENTUALLY`, `IMPLIES`, `UNTIL`, `NOT` references as i/p parameteres
        * `ALWAYS` block can not have `ALWAYS`, `IMPLIES`, `UNTIL`, `NOT` references as i/p parameteres.
    * Meanwhile `AND`, `OR`, `NOT` can have any `STL` class reference inside it.
    * `TASK` classes like `REACH`, `AVOID`, `STAY` must be inside either `ALWAYS` or `EVENTUALLY` blocka.
* `IMPLIES` and `UNTIL` are not ready for use as of now.
-----------
### Alternatively
Just change the shebang of `Combined Toolbox/STL_STT_Toolbox.py`, add your own semantic and compile directly. 