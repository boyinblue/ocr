#!/usr/bin/env python3

import pytesseract

from tkinter import *
from tkinter import ttk, messagebox
import tkinter.filedialog

try:
    import Image
except ImportError:
    from PIL import Image

# Make Main Window
root = Tk()
root.title("Make Preview From URL")
root.geometry("1000x768")
root.resizable(False, False)

# Make Text Box
path_label = Label(root, text="경로")
path_label.grid(column=0, row=0)
path_str = StringVar()
path_str.set("경로를 설정해주세요.")
path_textbox = ttk.Entry(root, width=100, textvariable=path_str)
path_textbox.grid(column=1, row=0)
path_textbox.focus()

# Make Select File Button
def select_path():
    root = Tk().withdraw()
    title = '분석할 이미지 파일'
    ftypes = [('JPEG file', '.jpeg'), ('JPG file', '.jpg'), ('PNG file', '.png'), ('All files', '*')]
    filename = tkinter.filedialog.askopenfilename(filetypes=ftypes, title=title)
    path_str.set(filename)

load_btn = ttk.Button(root, text="찾아보기", width=10, command=select_path)
load_btn.grid(column=0, row=1)

# Make OCR Button
def read_img():
    output_text = pytesseract.image_to_string(Image.open(path_str.get()))
    output_textbox.delete(1.0, END)
    output_textbox.insert(END, output_text)

run_btn = ttk.Button(root, text="분석하기", width=10, command=read_img)
run_btn.grid(column=1, row=1)

# Make Output Text Box
output_label = Label(root, text = "판독 결과")
output_label.grid(column=0, row=2)
output_textbox = Text(root, width=100, height=30)
output_textbox.grid(column=1, row=2)

# infinite loop
root.mainloop()