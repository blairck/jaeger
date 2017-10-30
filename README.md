### Description ###
Jaeger is a game for playing Foxes & Geese. This is a port of a game I wrote
originally in Objective-C in 2011. See: https://en.wikipedia.org/wiki/Fox_games

Project Status: Version 1.0.0 is released. This project is now in maintenance.

### Requirements ###
To use:
* Python 3.5 or later required
* Python 2 is not supported

### Setting Up For Players ###
Setting up:
* Install Python 3
* Download this repo (Green download button, upper right corner)

### Setting Up For Developers ###
Install extra requirements:
* Install Git
* Clone this repo
* Install Make to run the makefile
In the root folder of the project do the following:
```
virtualenv env
pip install -r requirements.txt
. env/bin/activate
make status
```
The status command will run PyLint over code in the src folder and then (if no
lint issues are found) execute all unittest files in the test folder.

