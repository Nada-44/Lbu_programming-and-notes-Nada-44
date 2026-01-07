from tkinter import *
import random


root = Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("Password Generator")
root.configure(bg="purple")

Label(root, text="Password Generator", font = "arial 15 bold").pack()
root.mainloop()
