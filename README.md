### Description ###
Jaeger is an engine for analyzing games of Fox(es) & Geese. This is a port of
an engine I wrote originally in Objective-C in 2011. See:
https://en.wikipedia.org/wiki/Fox_games

Project Status: Active

### Goals ###
* Port game playing engine from Objective-C to Python (in progress, see Status)
* Seperate UI logic from the rest of the game. Jaeger will be a tool only for
  the command line.
* Thorough unit testing coverage
* Currently the algorithm is strictly minimax. Implement alpha-beta pruning.
* Analysis of completed games, and suggest alternative lines.

### Status ###
Functions to be ported and tested, organized by component
* AI                            0/11
* Connection                    0/5
* FileController                0/2
* GameInterface                 0/23
* GameNode                      0/7
* HistoryNode                   0/11
* Rules                         1/14
* TOTAL                         1/73

### Requirements ###
To use:
* Python 3.5

For developers:
* Virtualenv
* Make
* Pylint
* Coverage

### Setting Up ###
Copy over the template to your project directory. Move your source code to to
the src directory, and unittest tests to the test folder. In the root folder of
the project do the following:
```
virtualenv env
pip install -r requirements.txt
. env/bin/activate
make status
```
The status command will run PyLint over code in the src folder and then (if no
lint issues are found) execute all unittest files in the test folder.

### Todo ###
* See: https://github.com/blairck/jaeger/issues
