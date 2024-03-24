from Images import *
from BoardCoordinates import boardCoordinatesList

class Piece():

    def __init__(self, boxPosition):
        self.setPosition(boxPosition)
        self.setColor()
        self.setPieceImage()

    def setPosition(self, boxPosition):
        self.piecePosition = boxPosition

    def getPosition(self):
        return self.piecePosition

    def getPieceImage(self):
        return self.pieceImage

    #Overridable methods
    def setColor(self):
        if (self.getPosition()[0] == 0):
            self.color = "black"
        elif (self.getPosition()[0] == 7):
            self.color = "white"
    
    def setPieceImage(self):
        pass

    def displayMoveSet(self):
        pass

class Pawn(Piece):

    def setColor(self):
        if (self.getPosition()[0] == 1):
            self.color = "black"
        elif (self.getPosition()[0] == 6):
            self.color = "white"

    def setPieceImage(self):
        if (self.color == "black"):
            self.pieceImage = imgBlackPawn
        elif (self.color == "white"):
            self.pieceImage = imgWhitePawn

    def displayMoveSet(self):
        #Pawns can only move one box forward
        #It captures one box diagonal
        #If the pawn is in its initial row, it can move two boxes forward
        #Pawns can do "en passant capture" if the enemy pawn next to them just moved from its starting box

        self.moveSetList = []

        #Current Position
        x = self.getPosition()[0]
        y = self.getPosition()[1]

        moveFactor = 0
        if (self.color == "white"):
            moveFactor = -1
        elif (self.color == "black"):
            moveFactor = 1

        #Move ahead
        if (boardCoordinatesList[x + moveFactor][y].piece == None):
            self.moveSetList.append((x + moveFactor, y))

            if (((x == 1) and (self.color == "black")) or ((x == 6) and (self.color == "white"))):
                self.moveSetList.append((x + (moveFactor * 2), y))
        
        #Regular Capure

        #En passant capture

        #Apply color changes to available boxes
        for position in self.moveSetList:
            boardCoordinatesList[position[0]][position[1]].setColor("#FFF455")
        
class Rook(Piece):

    def setPieceImage(self):
        if (self.color == "black"):
            self.pieceImage = imgBlackRook
        elif (self.color == "white"):
            self.pieceImage = imgWhiteRook

    def displayMoveSet(self):
        pass

class Knight(Piece):

    def setPieceImage(self):
        if (self.color == "black"):
            self.pieceImage = imgBlackKnight
        elif (self.color == "white"):
            self.pieceImage = imgWhiteKnight

    def displayMoveSet(self):
        pass

class Bishop(Piece):

    def setPieceImage(self):
        if (self.color == "black"):
            self.pieceImage = imgBlackBishop
        elif (self.color == "white"):
            self.pieceImage = imgWhiteBishop

class Queen(Piece):

    def setPieceImage(self):
        if (self.color == "black"):
            self.pieceImage = imgBlackQueen
        elif (self.color == "white"):
            self.pieceImage = imgWhiteQueen

    def displayMoveSet(self):
        pass

class King(Piece):

    def setPieceImage(self):
        if (self.color == "black"):
            self.pieceImage = imgBlackKing
        elif (self.color == "white"):
            self.pieceImage = imgWhiteKing

    def displayMoveSet(self):
        pass