### Description ###
Jaeger is a game for playing Foxes & Geese. This is a port of a game I wrote
originally in Objective-C in 2011. See: https://en.wikipedia.org/wiki/Fox_games

Project Status: Active

### Goals ###
* Port game playing engine from Objective-C to Python
* Seperate UI logic from the rest of the game. Jaeger will have a minimal text
interface for playing against the computer
* Thorough unit testing coverage
* Currently the algorithm is strictly minimax. Implement alpha-beta pruning.
* Analysis of completed games, and suggest alternative lines.

### Status ###
See: https://github.com/blairck/jaeger/issues

Functions to be ported and tested, organized by component (Finished)
* AI                            6/6
* Connection                    5/5
* GameNode                      7/7
* HistoryNode                   11/11
* Rules                         14/14
* TOTAL                         43/43

### Requirements ###
To use:
* Python 3.5

### Setting Up ###
In the root folder of the project do the following:
```
virtualenv env
pip install -r requirements.txt
. env/bin/activate
make status
```
The status command will run PyLint over code in the src folder and then (if no
lint issues are found) execute all unittest files in the test folder.

