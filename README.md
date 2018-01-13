### Description ###
Jaeger is a console-based implementation of the board game Foxes & Geese. Foxes
& Geese is a 2-player turn-based game where one player plays as the Foxes and
the other plays as the Geese. Foxes and Geese pieces move differently and have
different goals so the gameplay is asymmetric.

Project Status: Version 1.0.0 is released. This project is now in maintenance.

### Requirements ###
To use:
* Python 3.6 or later required
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

### Quick start ###
Here is how to quickly get into a game:
* Follow the 'Setting Up For Players' instructions
* In the jaeger directory, run the command "python main.py"
* This what you'll see:
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
Enter a move:
```
* By default, you'll be playing as the Geese. To make a move you'll need to
provide the starting location and the ending location. For example, the move
"23-33" would result in this board position:
```
7         G - G - G
          | \ | / |
6         G - G - G
          | / | \ |
5 G - G - G - G - G - G - G
  | \ | / | \ | / | \ | / |
4 G - G - G - G - G - G - G
  | / | \ | / | \ | / | \ |
3 G - . - G - . - . - G - G
          | \ | / |
2         . - . - .
          | / | \ |
1         F - . - F
  1   2   3   4   5   6   7
```
* Tip: If there is only 1 possible move with the ending location, you can just
type that. For example, you could type "43" which would make this move:
```
7         G - G - G
          | \ | / |
6         G - G - G
          | / | \ |
5 G - G - G - G - G - G - G
  | \ | / | \ | / | \ | / |
4 G - G - G - . - G - G - G
  | / | \ | / | \ | / | \ |
3 G - G - . - G - . - G - G
          | \ | / |
2         . - . - .
          | / | \ |
1         F - . - F
  1   2   3   4   5   6   7
```
* To quit, type "quit()" or Ctrl-D.
* Feel free to change game settings in the settings.py file and play again.

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
Foxes can move to any adjacent space that is connected by a line. Below, the
fox at (4,4) can move to the 8 highlighted spaces.
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

Foxes can capture Goose pieces that are adjacent. The fox will end up on the
space on the other side in a straight line. If there are multiple captures
available, the Fox player can choose any capture to make. However, if there
is a capture available the Fox player must make a capture.
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

This is an example of legal moves for the fox player with multiple captures.
Note how the 2nd fox piece at (2,4) is unable to move. The fox at (5,4) is able
to make 3 different capture moves. If the fox moves to (3,2), the fox will
capture the geese at (4,2) and (5,3).
```
7         . - . - .
          | \ | / |
6         . - . - .
          | / | \ |
5 . - . - . - . - . - . - .
  | \ | / | \ | / | \ | / |
4 . - F - . - . - F - G - x
  | / | \ | / | \ | / | \ |
3 . - . - . - . - G - . - .
          | \ | / |
2         x - G - x
          | / | \ |
1         . - . - .
  1   2   3   4   5   6   7
```

### Goose Movement ###
Goose can move an adjacent space but it has to be in the direction of the
victory area or to the side. Here is an example:
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

When a Goose moves into the victory area, it is promoted into a Supergoose. A
Supergoose can move in any direction, like a Fox.
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
