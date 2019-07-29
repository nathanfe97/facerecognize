from __future__ import print_function
from PIL import Image
from PIL import ImageTk
import Tkinter as tki
import threading
import datetime
import imutils
import cv2
import os



class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        self.label = tk.Label(self, text="This is our first GUI!")
        self.label.pack()

        self.log = tk.Button(self, text="LOG IN/OUT", fg="red",command=self.master.destroy)
        self.add = tk.Button(self, text="NEW MEMBER", fg="red",command=self.master.destroy)
        
        self.log.pack(side="bottom")
        self.add.pack(side="bottom")


root = tk.Tk()
app = Application(master=root)
app.mainloop()