#!/usr/bin/env python3

from gui import App
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image


def main():
    # Creates a window using tkinter
    window = App()
    winHeight = 1000
    winWidth = 1250

    top_frame = tk.Frame(window, width=winWidth, height=winHeight, bg="yellow")
    bot_frame = tk.Frame(window, width=winWidth, height=winHeight, bg="green")
    # Creates a label with text and uses pack() to put it on the window
    greeting = tk.Label(top_frame, text="Hello there")
    greeting.pack()

    log = tk.Button(
        master=top_frame,
        fg="black",
        bg="aqua",
        text="Mummy Joe is so cute and relatable but also totally not relatable LOL",
    )
    log.pack()

    top_frame.pack()
    bot_frame.pack()

    # ==== Attempt to incorporate images onto GUI =====
    oryx = Image.open("../res/Oryx1.png")

    # Create a photoimage object of the image in the path
    photoImage = ImageTk.PhotoImage(oryx)
    image_label = tk.Label(bot_frame, image=photoImage)
    image_label.image = photoImage

    # Position the image
    image_label.place(relx=0.5, rely=0.5)

    # .mainloop() is required to make the window appear
    window.mainloop()

    print("main.py was run successfully")


if __name__ == "__main__":
    main()
