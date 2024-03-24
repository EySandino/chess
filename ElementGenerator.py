from BoardCoordinates import boardCoordinatesList
from Box import Box

#Color of the squares of the board. This will change when needed to generate the board
boxColor = "#FFFFFF"

#Change the color of the board's squares to generate the board
def changeboxColor():
    global boxColor

    if (boxColor == "#FFFFFF"):
        boxColor = "#76ABAE"
    elif (boxColor == "#76ABAE"):
        boxColor = "#FFFFFF"

#Generates the squares where the pieces will move during the game
def generateBoardSquares(boardFrame):
    for boardRow in range(0,8):
        for boardColumn in range(0,8):
            boardCoordinatesList[boardRow][boardColumn] = Box(boardFrame, boxColor, boardRow, boardColumn)

            changeboxColor()
        changeboxColor()