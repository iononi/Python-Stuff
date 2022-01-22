# Copy Master is a program to copy files and directories 
# from src dir to dst dir. This is the windows version.

import subprocess
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askdirectory


def load(label):
	"""Sets the value of label with the selected file"""
	filename = askdirectory() # show an "Open" dialog box and return the path to the selected directory
	return label.set(filename)

def copyFull(src, dst):
	"""Copy all files and subdirectories from src to dst"""
	updated_src = src.replace("/", "\\")
	updated_dst = dst.replace("/", "\\")
	status = subprocess.run(["xcopy", updated_src, updated_dst, "/s", "/e"], capture_output=True)
	if status.returncode == 0:
		msg = (status.stdout).decode(encoding="UTF-8", errors="ignore")
		files = msg.replace("\r", "").split("\n")
		return messagebox.showinfo(title="Files copied successfully", message=files[-2])
	return messagebox.showinfo(title="Oops!", message="Something went wrong in the process :/")


def main():
	"""Main program function"""
	root = tk.Tk()
	root.geometry("600x400")
	root.title("Copy Master")
	root.resizable(False, False)

	src = tk.StringVar()
	dst = tk.StringVar()

	srcLbl = tk.Label(root, text="Source:")
	srcLbl.place(x=50, y=150)

	dstLbl = tk.Label(root, text="Destiny:")
	dstLbl.place(x=50, y=200)

	tk.Entry(root, width=70, state=tk.DISABLED, textvariable=src).place(x=100, y=150)
	tk.Entry(root, width=70, state=tk.DISABLED, textvariable=dst).place(x=100, y=200)

	tk.Button(root, text="Copy files", cursor="hand2", command=lambda : copyFull(src.get(), dst.get())).place(x=250, y=250)
	tk.Button(root, text="Load", cursor="hand2", command=lambda : load(src)).place(x=540, y=145)
	tk.Button(root, text="Load", cursor="hand2", command=lambda : load(dst)).place(x=540, y=195)
	
	root.mainloop()

if __name__ == "__main__":
	main()