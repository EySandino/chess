from BoardCoordinates import boardCoordinatesList
import tkinter as tk

#Color of the squares of the board. This will change when needed to generate the board
squareColor = "white"
photo = None

#Change the color of the board's squares to generate the board
def changeSquareColor():
    global squareColor

    if (squareColor == "white"):
        squareColor = "#76ABAE"
    elif (squareColor == "#76ABAE"):
        squareColor = "white"

#Generates the squares where the pieces will move during the game
def generateBoardSquares(boardFrame):
    global photo
    photo = tk.PhotoImage(file='img\\pieces\\bishop-black.png')
    #Make all the variables inside the board coordinates list actual frames we can work on
    for boardRow in range(0,8):
        for boardColumn in range(0,8):
            boardCoordinatesList[boardRow][boardColumn] = tk.Label(boardFrame, bg=squareColor, image=photo)

            changeSquareColor()
        changeSquareColor()
    
    for boardRow in range(0,8):
        for boardColumn in range(0,8):
            boardCoordinatesList[boardRow][boardColumn].grid(row=boardRow, column=boardColumn)

#Change the color of the board's squares to generate the board
def changeSquareColor():
    global squareColor

    if (squareColor == "white"):
        squareColor = "#76ABAE"
    elif (squareColor == "#76ABAE"):
        squareColor = "white"