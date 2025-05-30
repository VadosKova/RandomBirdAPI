import requests
from tkinter import *
from PIL import Image, ImageTk


access_key = "zcM-4apdjE3GtYjE3g2MA3cyORU_Pntf5CD9OFCvNfI"

def update_image():
    url = f"https://api.unsplash.com/photos/random?query=bird&client_id={access_key}&count=1"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(data)

        if data:
            bird_image_url = data[0]["urls"]["regular"]

            image = requests.get(bird_image_url)

            img = Image.open(requests.get(bird_image_url, stream=True).raw)
            file_type = img.format.lower()

            with open(f"bird.{file_type}", "wb") as f:
                f.write(image.content)

            img = Image.open(f"bird.{file_type}")
            img = img.resize((400, 400))
            tk_img = ImageTk.PhotoImage(img)

            label.config(image=tk_img)
            label.image = tk_img
            print(f"Птица: {bird_image_url}")
        else:
            print("Not Found")
    else:
        print(f"Error: {response.status_code}")

root = Tk()
root.title("Random Bird")
root.geometry("500x500")

label = Label(root)
label.pack(padx=20, pady=20)

update_image()

btn = Button(root, text="Next", command=update_image)
btn.pack(pady=10)

root.mainloop()