OUTSIDE = -1
EMPTY = 0
GOOSE = 1
FOX = 2
SUPERGOOSE = 3

def getPieceAbbreviation(inputType):
    if int(inputType)==EMPTY:
        return '.'
    elif int(inputType)==GOOSE:
        return 'G'
    elif int(inputType)==FOX:
        return 'F'
    elif int(inputType)==SUPERGOOSE:
        return 'S'
    else:
        return None