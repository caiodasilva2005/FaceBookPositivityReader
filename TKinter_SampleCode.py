
import tkinter

def drawScoreBar(score): 
    # init tk
    root = tkinter.Tk()

    # create canvas
    myCanvas = tkinter.Canvas(root, bg="white", height=340, width=80)

    arc = myCanvas.create_rectangle(0, score, 100, 350 , outline = "black", fill = "lightblue", width = 2)
    # add to window and show
    myCanvas.pack()
    root.mainloop()


drawScoreBar(100)