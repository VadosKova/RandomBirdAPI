import requests
from tkinter import *
from PIL import Image, ImageTk


access_key = "zcM-4apdjE3GtYjE3g2MA3cyORU_Pntf5CD9OFCvNfI"



root = Tk()
root.title("Random Bird")
root.geometry("500x500")

label = Label(root)
label.pack(padx=20, pady=20)

btn = Button(root, text="Next")
btn.pack(pady=10)

root.mainloop()