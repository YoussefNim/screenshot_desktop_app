from PIL import ImageGrab
import os
from datetime import datetime
import tkinter as tk 
from tkinter import filedialog

# function to pick a directory
def set_default_path():
    new_path = filedialog.askdirectory()
    if new_path:
        default_save_path.set(new_path)

# main function to take the screenshot
def take_screenshot_and_restore():
    SS = ImageGrab.grab()
    ss_path = default_save_path.get()
    timestamp_id = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    file_path = os.path.join(ss_path,f"SS_{timestamp_id}.png")
    SS.save(fp=file_path)
    interface.wm_deiconify()

# quickly minimize & maximize app so that it doesn't appear on the screenshot
def screenshot_it():
    interface.withdraw()
    interface.after(10, lambda: take_screenshot_and_restore())

# set it up so that CTRL W closes the app
def close_app(event=None):
    interface.destroy()

# the main interface
interface = tk.Tk()
interface.iconbitmap('C:\\Users\\Dell\\Documents\\icons\\screenshot_app.ico')
interface.resizable(False, False)

# just a variable to store the path name
default_save_path = tk.StringVar()

# displays a clickable text to select a directory
select_dir_txt = tk.Label(master=interface,text = "click here to select directory")
select_dir_txt.pack()
select_dir_txt.bind("<Button-1>", lambda event : set_default_path())

# displays a button to take screenshots
SSbutton = tk.Button(master=interface,width=5, height=1,  text="SS", command=screenshot_it)
SSbutton.pack()

interface.bind("<Control-w>",close_app)

interface.mainloop()
