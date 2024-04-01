import tkinter as tk
from PIL import ImageTk, Image
import score_calculator as sc

IMG_PATH = "./photos/photo.jpg"
POS_SCORE_DISPLAY = "Positivity Score"
POS_POST_DISPLAY = "Most Positive Post"
POS_COMMENT_DISPLAY = "Most Positive Comment"
TOTAL_REACTIONS_DISPLAY = "Total Reactions"

__all_displays__ = []

class InfoDisplay:
    def __init__(self, frame, topic, topic_row, topic_col):
        self.frame = frame
        self.topic = topic
        self.topic_row = topic_row
        self.topic_col = topic_col
        self.infoLabel = self.makeDisplay()
    
    def makeDisplay(self):
        topicLabel = tk.Label(self.frame, text=self.topic + ": ", bg="light blue", font=("Arial", 10, "bold"))
        topicLabel.grid(row=self.topic_row, column=self.topic_col, sticky="w", pady=10)

        infoLabel = tk.Label(self.frame, bg="light blue")
        infoLabel.grid(row=self.topic_row, column=self.topic_col+1, sticky="ew")

        __all_displays__.append(self)

        return infoLabel

def updateDisplays(page, bar_canvas):
    pos_score = sc.getPagePositivityScore(page)

    for display in __all_displays__:
        topic = display.topic
        if topic == POS_SCORE_DISPLAY:
            display.infoLabel['text'] = pos_score 
        elif topic == POS_POST_DISPLAY:
            display.infoLabel['text'] = sc.getMostPositiveMedia(sc.__all_posts__)
        elif topic == POS_COMMENT_DISPLAY:
            display.infoLabel['text'] = sc.getMostPositiveMedia(sc.__all_comments__)
        elif topic == TOTAL_REACTIONS_DISPLAY:
            display.infoLabel['text'] = formatReactions(sc.__all_reactions__)
    
    bar_canvas.create_rectangle(0, sc.MAX_SCORE/2 - pos_score/2, 100, sc.MAX_SCORE/2, fill="green")

def formatReactions(reactions):
    reaction_format = ""
    for key, value, in reactions.items():
        reaction_format += f"{key}: {value} \n" 
    return reaction_format

def makeFrame(window, width, height, row, col, rowspan=1):
    frame = tk.Frame(window, width=width, height=height, bg="light blue")
    frame.grid(row=row, column=col, rowspan=rowspan, sticky="nsew")

    return frame

def drawScoreBar(window): 

    myCanvas = tk.Canvas(window, bg="white", height=500, width=100)

    return myCanvas

def init(page):

    window = tk.Tk()
    window.title("FaceBook Positivity Reader")
    window.configure(bg="light blue")
    title_frame = makeFrame(window, 100, 100, 0, 0)
    
    img = Image.open(page.photo_path)
    desired_width = 100 
    desired_height = 75
    img = img.resize((desired_width, desired_height), Image.LANCZOS)

    img = ImageTk.PhotoImage(img)

    img_label = tk.Label(title_frame, image=img, padx=2, pady=2)
    img_label.grid(row=0, column=0, sticky="nsew")
    pageNameLabel = tk.Label(title_frame, text=page.name, font=("Arial", 10, "bold"), bg="light blue")
    pageNameLabel.grid(row=1, column=0, sticky="ew")

    infoFrame = makeFrame(window, 300, 300, 1, 0)

    InfoDisplay(infoFrame, POS_SCORE_DISPLAY, 0, 0)
    InfoDisplay(infoFrame, POS_POST_DISPLAY, 1, 0)
    InfoDisplay(infoFrame, POS_COMMENT_DISPLAY, 3, 0)
    InfoDisplay(infoFrame, TOTAL_REACTIONS_DISPLAY, 4, 0)

    bar_frame = makeFrame(window, 150, 500, 0, 1, 5)
    bar_canvas = drawScoreBar(bar_frame)
    bar_canvas.grid(row=0, column=1, rowspan=5, sticky="nsew")
    
    posButton = tk.Button(window, text="Get Positivity", command=lambda: updateDisplays(page, bar_canvas))
    posButton.grid(row=2, column=0, columnspan=2, sticky="w", padx=5, pady=5)

    window.mainloop()
