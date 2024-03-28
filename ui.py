import tkinter as tk
from PIL import ImageTk, Image, ImageDraw, ImageOps

IMG_PATH = "./photos/photo.jpg"

def updateScore(label, posScore):
    label["text"] = f"{posScore}"
    
def init():
    
    window = tk.Tk();
    window.title("FaceBook Positivity Reader")

    img = ImageTk.PhotoImage(Image.open(IMG_PATH))

    imgLabel = tk.Label(window, image = img)
    imgLabel.pack(side = "bottom", fill = "both", expand = "yes")

    window.mainloop()

    
    

init()