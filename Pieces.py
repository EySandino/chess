from Images import *

class Piece():

    def __init__(self, boxPosition):
        self.setPosition(boxPosition)
        self.setColor()
        self.setPieceImage()

    def setPosition(self, boxPosition):
        self.piecePosition = boxPosition

    def getPieceImage(self):
        return self.pieceImage

    #Overridable methods
    def setColor(self):
        if (self.piecePosition[0] == 0):
            self.color = "black"
        elif (self.piecePosition[0] == 7):
            self.color = "white"
    
    def setPieceImage(self):
        pass

class Pawn(Piece):

    def setColor(self):
        if (self.piecePosition[0] == 1):
            self.color = "black"
        elif (self.piecePosition[0] == 6):
            self.color = "white"

    def setPieceImage(self):
        if (self.color == "black"):
            self.pieceImage = imgBlackPawn
        elif (self.color == "white"):
            self.pieceImage = imgWhitePawn
        
class Rook(Piece):

    def setPieceImage(self):
        if (self.color == "black"):
            self.pieceImage = imgBlackRook
        elif (self.color == "white"):
            self.pieceImage = imgWhiteRook

class Knight(Piece):

    def setPieceImage(self):
        if (self.color == "black"):
            self.pieceImage = imgBlackKnight
        elif (self.color == "white"):
            self.pieceImage = imgWhiteKnight

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

class King(Piece):

    def setPieceImage(self):
        if (self.color == "black"):
            self.pieceImage = imgBlackKing
        elif (self.color == "white"):
            self.pieceImage = imgWhiteKing