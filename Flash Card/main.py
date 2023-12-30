from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
LANG_FONT = ('Arial', 40, 'italic')
WORD_FONT = ('Arial', 60, 'bold')

data_dictionary = {}
current_card = {}
try:
    data = pandas.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('./data/french_words.csv')
    data_dictionary = original_data.to_dict(orient='records')
else:
    data_dictionary = data.to_dict(orient='records')


# TODO: Create flash card. Show the answer in 3 seconds, if got it right delete it from the flash cards else repeat it.
def create_flashcard():
    global current_card, timer
    window.after_cancel(timer)
    canvas.itemconfig(canvas_bg_img, image=canvas_front_img)
    current_card = choice(data_dictionary)
    canvas.itemconfig(canvas_title, text='French', fill='Black')
    canvas.itemconfig(canvas_word, text=current_card['French'], fill='Black')
    timer = window.after(3000, show_flashcard)


def show_flashcard():
    canvas.itemconfig(canvas_bg_img, image=canvas_back_img)
    canvas.itemconfig(canvas_title, text='English', fill='white')
    canvas.itemconfig(canvas_word, text=current_card['English'], fill='white')


def add_word():
    data_dictionary.remove(current_card)
    words_to_learn = pandas.DataFrame(data_dictionary)
    words_to_learn.to_csv('data/words_to_learn.csv', index=False)
    create_flashcard()


# Window Settings
window = Tk()
window.title('Flash Card')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = window.after(3000, show_flashcard)
# Flash Card Settings
canvas_front_img = PhotoImage(file='./images/card_front.png')
canvas_back_img = PhotoImage(file='./images/card_back.png')

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_bg_img = canvas.create_image(400, 263, image=canvas_front_img)
canvas_title = canvas.create_text(400, 150, font=LANG_FONT)
canvas_word = canvas.create_text(400, 263, font=WORD_FONT)
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
cross_img = PhotoImage(file='./images/wrong.png')
cross_button = Button(image=cross_img, highlightthickness=0, command=create_flashcard)
cross_button.grid(column=0, row=1)

check_img = PhotoImage(file='./images/right.png')
check_button = Button(image=check_img, highlightthickness=0, command=add_word)
check_button.grid(column=1, row=1)
create_flashcard()

window.mainloop()
