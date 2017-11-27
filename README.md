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
* Install Make to run the makefile commands

### Game Overview ###
The goal of the game is to move 9 goose pieces into the Victory area:
7         . - . - .
          | \ | / |
6         . - . - .
          | / | \ |
5 . - . - . - . - . - . - .
  | \ | / | \ | / | \ | / |
4 . - . - . - . - . - . - .
  | / | \ | / | \ | / | \ |
3 . - . - x - x - x - . - .
          | \ | / |
2         x - x - x
          | / | \ |
1         x - x - x
  1   2   3   4   5   6   7

### Examples Moves:

Goose can move towards the victory area or to the side. Example move:
7         . - . - .
          | \ | / |
6         . - . - .
          | / | \ |
5 . - . - . - . - . - . - .
  | \ | / | \ | / | \ | / |
4 . - . - x - G - x - . - .
  | / | \ | / | \ | / | \ |
3 . - . - x - x - x - . - .
          | \ | / |
2         . - . - .
          | / | \ |
1         . - . - .
  1   2   3   4   5   6   7

Super goose move:
7         . - . - .
          | \ | / |
6         . - . - .
          | / | \ |
5 . - . - x - x - x - . - .
  | \ | / | \ | / | \ | / |
4 . - . - x - S - x - . - .
  | / | \ | / | \ | / | \ |
3 . - . - x - x - x - . - .
          | \ | / |
2         . - . - .
          | / | \ |
1         . - . - .
  1   2   3   4   5   6   7


Fox move:
7         . - . - .
          | \ | / |
6         . - . - .
          | / | \ |
5 . - . - x - x - x - . - .
  | \ | / | \ | / | \ | / |
4 . - . - x - F - x - . - .
  | / | \ | / | \ | / | \ |
3 . - . - x - x - x - . - .
          | \ | / |
2         . - . - .
          | / | \ |
1         . - . - .
  1   2   3   4   5   6   7
