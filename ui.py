import tkinter as tk
from PIL import ImageTk, Image, ImageDraw, ImageOps

IMG_PATH = "./photos/photo.jpg"

def updateScore(label, posScore):
    label["text"] = f"{posScore}"
    
def init():
    
    window = tk.Tk();
    window.title("FaceBook Positivity Reader")
    window.geometry("500x500")

    img = ImageTk.PhotoImage(Image.open(IMG_PATH))

    #imgLabel = tk.Label(window, image = img)
    #imgLabel.grid(row=0, column=0, sticky="nsew")

    label = tk.Label(window, text="IMAGE")
    label.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

    pageNameLabel = tk.Label(window, text="PAGE NAME")
    pageNameLabel.grid(row=0, column=1, sticky="n", padx=5, pady=5)

    posScoreLabel = tk.Label(window, text="0")
    posScoreLabel.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

    posButton = tk.Button(window, text="Get Positivity Score", command=lambda: updateScore(posScoreLabel, "10"))
    posButton.grid(row=1, column=0, sticky="e", padx=5, pady=5)


    window.mainloop()

    
    

init()