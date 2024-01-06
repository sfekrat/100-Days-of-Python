import requests
from tkinter import *


def get_quote():
    response = requests.get(url='https://api.kanye.rest')
    response.raise_for_status()
    data = response.json()
    canvas.itemconfig(canvas_text, text=data['quote'])


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

background_image = PhotoImage(file='../kanye quotes/background.png')
canvas = Canvas(width=300, height=414)
canvas.create_image(150, 207, image=background_image)
canvas_text = canvas.create_text(150, 207, text='Kanye Quote Goes HERE', width=250, font=("Arial", 20, "bold"),
                                 fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file='../kanye quotes/kanye.png')
button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
button.grid(row=1, column=0)

window.mainloop()
