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
Jaeger is a console-based implementation of the board game Foxes & Geese. Foxes
& Geese is a 2-player game where one player plays as the Foxes and the other
plays as the Geese. Foxes and Geese pieces move differently and have different
goals so the gameplay is asymmetric. 

### Setup ###
This is the default setup of the board. The letter 'G' represents Goose pieces,
and the letter 'F'  represents Fox pieces. Dots '.' are empty spaces. Pieces
rest on the spaces and can only move between them along the solid lines. Notice
that some spaces have only 4 connecting lines, such as (4,3). Other spaces have
8 connecting lines, such as (4,4). This makes some spaces more valuable than
others.
```
7         G - G - G
          | \ | / |
6         G - G - G
          | / | \ |
5 G - G - G - G - G - G - G
  | \ | / | \ | / | \ | / |
4 G - G - G - G - G - G - G
  | / | \ | / | \ | / | \ |
3 G - G - . - . - . - G - G
          | \ | / |
2         . - . - .
          | / | \ |
1         F - . - F
  1   2   3   4   5   6   7
```

### Goal ###
The goal of the game is to move 9 goose pieces into the Victory area:
```
7         . - . - .
          | \ | / |
6         . - . - .
          | / | \ |
5 . - . - . - . - . - . - .
  | \ | / | \ | / | \ | / |
4 . - . - . - . - . - . - .
  | / | \ | / | \ | / | \ |
3 . - . - G - G - G - . - .
          | \ | / |
2         G - G - G
          | / | \ |
1         G - G - G
  1   2   3   4   5   6   7
```

When this happens, the Geese will have won the game. If the Geese have 8 or
fewer pieces left, then the Foxes win because the Geese are incapable of
occupying the victory area. The game ends in a tie if either player is unable
to move.

### Starting the Game ###
Geese move first. Play alternates between geese and foxes until a player wins
the game. 

### Fox Movement ###
Fox move:
```
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
```

Fox capture:
```
7         . - . - .
          | \ | / |
6         . - . - .
          | / | \ |
5 . - . - . - . - . - . - .
  | \ | / | \ | / | \ | / |
4 . - . - . - F - G - x - .
  | / | \ | / | \ | / | \ |
3 . - . - . - . - . - . - .
          | \ | / |
2         . - . - .
          | / | \ |
1         . - . - .
  1   2   3   4   5   6   7
```

### Goose Movement ###
Goose can move towards the victory area or to the side. Example move:
```
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
```

Super goose move:
```
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
```
