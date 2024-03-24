from tkinter import Label, PhotoImage
from Images import imgWhiteBox, imgBlackBox
from Pieces import *

class Box():
    img = None

    def __init__(self, boardFrame, boxColor, boardRow, boardColumn):
        self.generateBox(boardFrame)
        self.setPosition(boardRow, boardColumn)
        self.setColor(boxColor)
        self.setPiece()
        self.setBoxPhoto(boxColor)
        self.placeBox()

    #Get box properties
    def getPosition(self):
        return self.boxPosition

    #Set box properties
    def setCursor(self, cursorInput):
        self.boardBox.config(cursor=cursorInput)

    def setBoxPhoto(self, boxColor):
        global img

        if (self.piece != None):
            img = PhotoImage(file=self.piece.getPieceImage())
            self.boardBox.config(image=img)
        else:
            if (boxColor == "#FFFFFF"):
                img = PhotoImage(file=imgWhiteBox)
                self.boardBox.config(image=img)
            elif (boxColor == "#76ABAE"):
                img = PhotoImage(file=imgBlackBox)
                self.boardBox.config(image=img)

    def setPosition(self, x, y):
        self.boxPosition = (x, y)
    
    def setColor(self, boxColor):
        self.boardBox.config(bg=boxColor)

    def setPiece(self):
        #Generate the "piece" object that will occupy the box
        if (self.boxPosition[0] not in range(2, 6)):
            self.setCursor("hand2")

            #Define Pawn
            if ((self.boxPosition[0] == 1) or (self.boxPosition[0] == 6)):
                self.piece = Pawn(self.getPosition())

            #Define Rook
            elif ((self.boxPosition[1] == 0) or (self.boxPosition[1] == 7)):
                self.piece = Rook(self.getPosition())

            #Define Knight
            elif ((self.boxPosition[1] == 1) or (self.boxPosition[1] == 6)):
                self.piece = Knight(self.getPosition())

            #Define Bishop
            elif ((self.boxPosition[1] == 2) or (self.boxPosition[1] == 5)):
                self.piece = Bishop(self.getPosition())

            #Define Queen
            elif ((self.boxPosition[1] == 3)):
                self.piece = Queen(self.getPosition())

            #Define King
            elif ((self.boxPosition[1] == 4)):
                self.piece = King(self.getPosition())
        #If the box is empty the object won't be generated
        else:
            self.setCursor("arrow")
            self.piece = None
    
    #Generate methods
    def generateBox(self, boardFrame):
        self.boardBox = Label(boardFrame, width=48, height=48)

    def placeBox(self):
        self.boardBox.grid(row=self.boxPosition[0], column=self.boxPosition[1])