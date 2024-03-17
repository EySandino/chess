import BoardCoordinates
import ttkbootstrap as ttk
from ttkbootstrap.icons import Icon

#Color of the squares of the board. This will change when needed to generate the board
squareColor = "light"

#Change the color of the board's squares to generate the board
def changeSquareColor():
    global squareColor

    if (squareColor == "light"):
        squareColor = "dark"
    elif (squareColor == "dark"):
        squareColor = "light"

#Generates the squares where the pieces will move during the game
def generateBoardSquares(boardFrame):
    #img = ImageTk.PhotoImage(Image.open("img\\pieces\\bishop-black.png"))
    #Make all the variables inside the board coordinates list actual frames we can work on
    for boardRow in range(0,8):
        for boardColumn in range(0,8):
            BoardCoordinates.boardCoordinatesList[boardRow][boardColumn] = ttk.Frame(boardFrame, height=60, width=60, image=img)

            changeSquareColor()
        changeSquareColor()
    
    for boardRow in range(0,8):
        for boardColumn in range(0,8):
            BoardCoordinates.boardCoordinatesList[boardRow][boardColumn].grid(row=boardRow, column=boardColumn)