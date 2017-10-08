# alan
Simple simulator of a Turing Machine implemented in Python

## Installation 

``
pip install git+https://github.com/mprzewie/alan.git
``

## Representation of settings in a .csv file

* the first cell (first row, first column) remains empty
* columns 2+ in the first row in the .csv settings file denote the possible signs to be written and read from the 'tape' by the machine
* rows 2+ in the first column denote the possible states of the Turing Machine
    * names **s**, **y** and **n** are reserved for **start**, **yes** and **no** states, respectively
    * as **y** and **n** are two possible final states of the machine, they shouldn't be denoted in the first column of the file
* cells identified by a given sign and state define the behavior of the machine in that particular state when that particular sign has been encountered
    * behavior is made up of three parts separated by semicolons (;) **without** spaces
        * new sign - the sign that should be written in the current position onf the tape
            * if left blank, sign remains unchanged
        * new state - the state that the Machine should now assume
            * if left blank, state remains unchanged
        * direction of the movement, denoted by a **-** or a **+**
            * if **-**, the Machine moves to the cell on the left in the next step
            * if **+**, the Machine moves to the cell on the right in th next step
            * **cannot** be left blank
    * names of the signs and the states are not validated in any way, so be careful not to misspell them
    * **do not** use spaces
* if you think that a given combintation of sign and state will never occur, you can leave the cell blank. However, if the Machine *does* reach that combination, it will crash.
* example settings can be found in the  `machines/` directory

## Usage

* use Python 3+

### Executable

The easiest way to run the simulator is through an executable which installs with the library through `pip`.

Execute:

``
alan -h
``

to learn the syntax.

#### Important notes:

* *SETTINGS_SRC* and *WORD* parameters are compulsory. The rest is optional
* signs in the *WORD* parameter must be comma-separated (and therefore cannot be commas, of course). 
This, while less convenient, allows signs to take multi-character values.

### Library

For how to use the library, explore the code yourself. `alan/machine.py` is probably the best place to start
 

