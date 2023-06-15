import tkinter as tk
import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS2
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

root = tk.Tk()
root.overrideredirect(True)
root.iconbitmap(resource_path("Hanuman.ico"))
root.config(bg="blue", bd=0, highlightthickness=0)
root.attributes("-topmost", True)
root.attributes("-transparentcolor", "gold")
root.geometry("+1222+22")

lastClickX = 0
lastClickY = 0

def SaveLastClickPos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y

def Dragging(event):
    x, y = event.x - lastClickX + root.winfo_x(), event.y - lastClickY + root.winfo_y()
    root.geometry("+%s+%s" % (x , y))
    
def destroy(event):
    root.destroy()

canvas = tk.Canvas(root, bg="gold", bd=0, highlightthickness=0)
canvas.pack()

img = tk.PhotoImage(file=resource_path("hanuman.png"))
tk_img = img.subsample(2, 2)
canvas.create_image(0, -10, image=tk_img, anchor="nw")

root.bind('<Button-1>', SaveLastClickPos)
root.bind('<B1-Motion>', Dragging)
root.bind('<Shift-Down>', destroy)

root.mainloop()