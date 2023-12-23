from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    tick_mark.config(text="")
    timer_label.config(text='Timer')


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 0:
        if reps == 8:
            count_down(long_break_sec)
            timer_label.config(text='Break', fg=RED)
        else:
            timer_label.config(text='Break', fg=PINK)
            count_down(short_break)
    else:
        timer_label.config(text='Work!')
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(10, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔️"
        tick_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg='black')

timer_label = Label(text='Timer')
timer_label.config(font=(FONT_NAME, 28, "bold"), bg='black', fg='white')
timer_label.grid(column=1, row=0)

tomato_img = PhotoImage(file='tomato.png')
canvas = Canvas(width=200, height=224, bg='black', highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=2)

start_button = Button(text='Start', font=(FONT_NAME, 8, "bold"), highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=4)

reset_button = Button(text='Reset', font=(FONT_NAME, 8, "bold"), highlightthickness=0, command=reset_timer)
reset_button.grid(column=3, row=4)

tick_mark = Label()
tick_mark.config(font=(FONT_NAME, 6, "bold"), bg='black', fg='white')
tick_mark.grid(column=1, row=5)
window.mainloop()
