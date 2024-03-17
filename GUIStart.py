import ttkbootstrap as ttk
import ElementGenerator

#Main window where all the game will display
root = ttk.Window(title="Sandi Chess", themename="darkly", size=(550, 800), resizable=(False, False))
root.iconbitmap("img\\ico\\chess.ico")

#Frame on which the chess pieces will be and move
boardFrame = ttk.Frame(root, bootstyle="dark")
boardFrame.place(x=35, y=30)

#Frames that show the players what pieces they have capture so far
whiteCapturesFrame = ttk.Frame(root, bootstyle="light", height=100, width=250)
blackCapturesFrame = ttk.Frame(root, bootstyle="light", height=100, width=250)

#Entry that shows the players what was the last move
lastMoveEntry = ttk.Entry(root, bootstyle="light", state="disabled")

#Button to confirm when a player is ready to continue the game
confirmButton = ttk.Button(root, bootstyle="default", text="Confirm Move")

#Initate the game GUI
def startGame():
    generateElements()
    root.mainloop()

#Generate the basic elements of the game
def generateElements():
    ElementGenerator.generateBoardSquares(boardFrame)

    #Generate the capture frames
    whiteCapturesFrame.place(x=35, y=540)
    blackCapturesFrame.place(x=35, y=670)

    #Generate the last move entry
    lastMoveEntry.place(x=300, y=540)

    #Generate the confirm button
    confirmButton.place(x=300, y=600)

    #Generate labes to display in the game GUI
    ttk.Label(bootstyle="light", text="White's captures", font=("Arial", 10)).place(x=35, y=520)
    ttk.Label(bootstyle="light", text="Black's captures", font=("Arial", 10)).place(x=35, y=650)
    ttk.Label(bootstyle="light", text="Last Move", font=("Arial", 10)).place(x=300, y=520)