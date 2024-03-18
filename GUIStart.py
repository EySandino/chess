import ElementGenerator
import tkinter as tk

#Main window where all the game will display
root = tk.Tk()
root.configure(background="#31363F")
root.geometry("550x800")
root.title("Sandi Chess")
root.iconbitmap("img\\ico\\chess.ico")

#Frame on which the chess pieces will be and move
boardFrame = tk.Frame(root)
boardFrame.place(x=35, y=30)

#Frames that show the players what pieces they have capture so far
whiteCapturesFrame = tk.Frame(root, bg="#FFFFFF", height=100, width=250)
blackCapturesFrame = tk.Frame(root, bg="#FFFFFF", height=100, width=250)

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

    #Generate the capture frames
    whiteCapturesFrame.place(x=35, y=550)
    blackCapturesFrame.place(x=35, y=680)

    #Generate the last move entry
    lastMoveEntry.place(x=320, y=550)

    #Generate the confirm button
    confirmButton.place(x=320, y=600)

    #Generate labes to display in the game GUI
    tk.Label(root, bg="#31363F", fg="white", text="White's captures", font=("Arial", 10)).place(x=35, y=520)
    tk.Label(root, bg="#31363F", fg="white", text="Black's captures", font=("Arial", 10)).place(x=35, y=650)
    tk.Label(root, bg="#31363F", fg="white", text="Last Move", font=("Arial", 10)).place(x=320, y=520)

