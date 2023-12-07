import tkinter as tk
from tkinter import messagebox
from . import tinder_view
import os


def start_ai_experience(root):
    print("bla")
    data_dir = "resources/myntradataset"
    tinder_view.show_image_rating_window(root, data_dir)
    # print wd files


def home_screen(root):
    # Create the main window

    root.title("Home Screen")

    # Set the window to full screen
    root.attributes('-fullscreen', True)

    # Welcome label
    welcome_label = tk.Label(root, text="Welcome!", font=("Helvetica", 18))
    welcome_label.grid(row=0, column=0, pady=(root.winfo_screenheight() // 2 - 50))

    # Start AI experience button
    start_button = tk.Button(root, text="Start AI Experience", command=lambda: start_ai_experience(root))
    start_button.grid(row=1, column=0, pady=10)

    # Center the button horizontally
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # Run the Tkinter event loop
    root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    home_screen(root)
