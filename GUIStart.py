import ElementGenerator
import tkinter as tk

#Main window where all the game will display
root = tk.Tk()
root.geometry("485x550")
root.title("Sandi Chess")
root.resizable(False, False)
root.configure(background="#31363F")
root.iconbitmap("img\\ico\\chess.ico")

#Frame on which the chess pieces will be and move
boardFrame = tk.Frame(root)
boardFrame.place(x=35, y=30)

#Entry that shows the players what was the last move
lastMoveEntry = tk.Entry(root, bg="#FFFFFF", state="disabled", cursor="arrow")

#Button to confirm when a player is ready to continue the game
confirmButton = tk.Button(root, bg="#FFFFFF", text="Confirm Move", background="#76ABAE", foreground="white", cursor="hand2")

#Initate the game GUI
def startGame():
    generateElements()
    root.mainloop()

#Generate the basic elements of the game
def generateElements():
    #Generate main board
    ElementGenerator.generateBoardSquares(boardFrame)

    #Generate the last move entry
    lastMoveEntry.place(x=35, y=475)
    tk.Label(root, bg="#31363F", fg="white", text="Last Move", font=("Arial", 10)).place(x=35, y=450)

    #Generate the confirm button
    confirmButton.place(x=330, y=470)

if (__name__ == "__main__"):
    startGame()