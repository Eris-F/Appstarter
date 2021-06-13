import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt' , 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(",")
        apps = tempApps
        apps = [x for x in apps if x.split()]

def addApps():
    for name in frame.winfo_children():
        name.destroy()

    filename = filedialog.askopenfilename(initialdir="/" , title="Select File" , filetypes=(("executables","*.exe"),("All Files","*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        apptitle = tk.Label(frame , text=app)
        apptitle.pack()


def runApps():
    for app in apps:
        os.startfile(app)


canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth = 0.8 , relheight = 0.8 , relx = 0.1 , rely = 0.1)

openFile = tk.Button(root, text="Open File" , padx=10 , pady=5 , fg = "white" , bg = "#263D42" ,command=addApps)
openFile.pack()

runApps = tk.Button(root, text="Run Apps" , padx=10 , pady=5 , fg = "white" , bg = "#263D42" , command=runApps)
runApps.pack()

for app in apps:
    apptitle = tk.Label(frame, text=app)
    apptitle.pack()

root.mainloop()


with open("save.txt" , "w") as f:
    for app in apps:
        f.write(app + ',')