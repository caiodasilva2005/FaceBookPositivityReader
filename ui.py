import tkinter as tk
from PIL import ImageTk, Image, ImageDraw, ImageOps
import score_calculator as sc

IMG_PATH = "./photos/photo.jpg"
POS_SCORE_DISPLAY = "Positivity Score"
POS_POST_DISPLAY = "Most Positive Post"

__all_displays__ = []

class InfoDisplay:
    def __init__(self, frame, topic, topic_row, topic_col):
        self.frame = frame
        self.topic = topic
        self.topic_row = topic_row
        self.topic_col = topic_col
        self.infoLabel = self.makeDisplay()
    
    def makeDisplay(self):
        topicLabel = tk.Label(self.frame, text=self.topic + ": ")
        topicLabel.grid(row=self.topic_row, column=self.topic_col, sticky="e")

        infoLabel = tk.Label(self.frame)
        infoLabel.grid(row=self.topic_row, column=self.topic_col+1, sticky="ew")

        __all_displays__.append(self)

        return infoLabel

def updateDisplays(page):
    for display in __all_displays__:
        if display.topic == POS_SCORE_DISPLAY:
            display.infoLabel['text'] = sc.getPagePositivityScore(page) 
        elif display.topic == POS_POST_DISPLAY:
            display.infoLabel['text'] = sc.getMostPositiveMedia(sc.__all_posts__)
    
def init(page):
    
    window = tk.Tk();
    window.title("FaceBook Positivity Reader")
    frame = tk.Frame(window, width=100, height=100)
    frame.grid(row=0, column=0, sticky="nsew")

    img = ImageTk.PhotoImage(Image.open(IMG_PATH))

    #imgLabel = tk.Label(frame, image = img)
    #imgLabel.grid(row=0, column=0, sticky="nsew")

    img_label = tk.Label(frame, text="IMAGE")
    img_label.pack()
    pageNameLabel = tk.Label(frame, text="PAGE NAME")
    pageNameLabel.pack()

    infoFrame = tk.Frame(window, width=300, height=300)
    infoFrame.grid(row=1, column=0, sticky="nsew")

    InfoDisplay(infoFrame, POS_SCORE_DISPLAY, 0, 0)
    InfoDisplay(infoFrame, POS_POST_DISPLAY, 1, 0)

    posButton = tk.Button(window, text="Get Positivity", command=lambda: updateDisplays(page))
    posButton.grid(row=2, column=0, sticky="ew", padx=5, pady=5)


    window.mainloop()
