from tkinter import Label, PhotoImage
from Images import imgWhiteBox, imgBlackBox
from Pieces import *

class Box():

    def __init__(self, boardFrame, boxColor, boardRow, boardColumn):
        #Generate the board box label object
        self.generateBox(boardFrame)

        #Set the board x, y coordinates
        self.setPosition(boardRow, boardColumn)

        #Set color value variable and color of the box
        self.setBoxColorValue(boxColor)
        self.setColor(self.boxColor)

        #Create the piece object if needed
        self.setPiece()
        self.setBoxPhoto(self.boxColor)

        #Set the label in the boardFrame grid
        self.placeBox()

    #Get box properties
    def getPosition(self):
        return self.boxPosition

    #Set box properties
    def setCursor(self, cursorInput):
        self.boardBox.config(cursor=cursorInput)

    def setBoxPhoto(self, boxColor):
        if (self.piece != None):
            self.img = PhotoImage(file=self.piece.getPieceImage())
            self.boardBox.config(image=self.img)
        else:
            if (boxColor == "#FFFFFF"):
                self.img = PhotoImage(file=imgWhiteBox)
                self.boardBox.config(image=self.img)
            elif (boxColor == "#76ABAE"):
                self.img = PhotoImage(file=imgBlackBox)
                self.boardBox.config(image=self.img)

    def setPosition(self, x, y):
        self.boxPosition = (x, y)

    def setBoxColorValue(self, colorValue):
        self.boxColor = colorValue
    
    def setColor(self, boxColor):
        self.boardBox.config(bg=boxColor)

    def setPiece(self):
        #Generate the "piece" object that will occupy the box
        if (self.getPosition()[0] not in range(2, 6)):
            self.enableTriggerAction()

            #Define Pawn
            if ((self.getPosition()[0] == 1) or (self.getPosition()[0] == 6)):
                self.piece = Pawn(self.getPosition())

            #Define Rook
            elif ((self.getPosition()[1] == 0) or (self.getPosition()[1] == 7)):
                self.piece = Rook(self.getPosition())

            #Define Knight
            elif ((self.getPosition()[1] == 1) or (self.getPosition()[1] == 6)):
                self.piece = Knight(self.getPosition())

            #Define Bishop
            elif ((self.getPosition()[1] == 2) or (self.getPosition()[1] == 5)):
                self.piece = Bishop(self.getPosition())

            #Define Queen
            elif ((self.getPosition()[1] == 3)):
                self.piece = Queen(self.getPosition())

            #Define King
            elif ((self.getPosition()[1] == 4)):
                self.piece = King(self.getPosition())
        #If the box is empty the object won't be generated
        else:
            self.setCursor("arrow")
            self.piece = None

    def movePiece(self, event):
        self.setColor("#FFC700")
        self.piece.displayMoveSet()

    def doNothing(self, event):
        pass


    #Generate methods
    def generateBox(self, boardFrame):
        self.boardBox = Label(boardFrame, width=48, height=48)

    def placeBox(self):
        self.boardBox.grid(row=self.getPosition()[0], column=self.getPosition()[1])
        
    def enableTriggerAction(self):
        self.setCursor("hand2")
        self.boardBox.bind("<Button-1>", self.movePiece)

    def disableTriggerAction(self):
        self.setCursor("arrow")
        self.setColor(self.boxColor)
        self.boardBox.bind("<Button-1>", self.doNothing)