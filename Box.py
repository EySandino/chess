from tkinter import Label, PhotoImage
from Images import *

class Box():

    def __init__(self, boardFrame, boxColor, boardRow, boardColumn):
        self.boardBox = Label(boardFrame, width=48, height=48, bg=boxColor)

        if (boardRow not in range(2, 6)):
            self.boardBox.config(cursor="hand2")

            #Pawn
            if (boardRow == 1):
                self.photo = PhotoImage(file=imgBlackPawn)
            elif (boardRow == 6):
                self.photo = PhotoImage(file=imgWhitePawn)

            #Rook
            elif ((boardColumn == 0) or (boardColumn == 7)):
                if (boardRow == 0):
                    self.photo = PhotoImage(file=imgBlackRook)
                elif (boardRow == 7):
                    self.photo = PhotoImage(file=imgWhiteRook)

            #Knight
            elif ((boardColumn == 1) or (boardColumn == 6)):
                if (boardRow == 0):
                    self.photo = PhotoImage(file=imgBlackKnight)
                elif (boardRow == 7):
                    self.photo = PhotoImage(file=imgWhiteKnight)

            #Bishop
            elif ((boardColumn == 2) or (boardColumn == 5)):
                if (boardRow == 0):
                    self.photo = PhotoImage(file=imgBlackBishop)
                elif (boardRow == 7):
                    self.photo = PhotoImage(file=imgWhiteBishop)

            #Queen
            elif ((boardColumn == 3)):
                if (boardRow == 0):
                    self.photo = PhotoImage(file=imgBlackQueen)
                elif (boardRow == 7):
                    self.photo = PhotoImage(file=imgWhiteQueen)

            #King
            elif ((boardColumn == 4)):
                if (boardRow == 0):
                    self.photo = PhotoImage(file=imgBlackKing)
                elif (boardRow == 7):
                    self.photo = PhotoImage(file=imgWhiteKing)
            
        else:
            if (boxColor == "white"):
                self.photo = PhotoImage(file=imgWhiteBox)
            elif (boxColor == "#76ABAE"):
                self.photo = PhotoImage(file=imgBlackBox)

        self.boardBox.config(image=self.photo)
        self.boardBox.grid(row=boardRow, column=boardColumn)