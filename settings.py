"""Settings used for running the game in main.py"""

# Display the x-axis as 'A B C...' (True) or '1 2 3...' (False).
ALPHABETNOTATION = False

# Shows an evaluation of the board state every time it's the player's turn.
# Higher numbers favor Goose, and lower numbers favor Fox. Drawn positions are
# evaluated as 0.0
DISPLAYEVALUATION = False

# How far ahead the computer searches. Higher numbers are slower. A single ply
# is equal to a "half turn," which could either be a goose or fox move.
# Recommended values: Easy - 1, Medium - 3, Hard - 5, Very Hard - 7
# Note: Values above 5 take the AI a long time to respond (minutes or more)
SEARCHPLY = 3

#  Standard fox positions (True) or random (False).
STANDARD = True

# User plays Fox (True) or Goose (False).
USERPLAYSFOX = False
