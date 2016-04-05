# Description #

This an engine for analyzing games of Fox(es) & Geese. This is a port of an engine I wrote originally in Objective-C.

### Requirements ###

* Python 2.7
* Virtualenv
* Make
* Pylint
* Coverage

### Setting Up ###

Copy over the template to your project directory. Move your source code to to the src directory, and unittest tests to the test folder. In the root folder of the project do the following:
```
virtualenv env
pip install -r requirements.txt
. env/bin/activate
make status
```
The status command will run PyLint over code in the src folder and then (if no lint issues are found) execute all unittest files in the test folder.

### Status ###

0/8 components ported
* AI
* Connection
* FileController
* Foxes_and_GeeseAppDelegate
* GameInterface
* GameNode
* HistoryNode
* Rules