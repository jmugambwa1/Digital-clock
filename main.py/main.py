import tkinter as tk
from time import strftime


root = tk.Tk()
root.title("Digital Clock")
root.resizable(False, False)
root.geometry("550x340")




def time():
    tyme = strftime("%I:%M:%S %p")
    lbl.config(text=tyme)
    lbl.after(1000, time)

lbl = tk.Label(root, font=('franklin go', 50), bg="black", fg="green")
lbl.pack(expand=True)

time()

root.mainloop()


