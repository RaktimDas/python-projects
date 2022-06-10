"""Importing the libraries"""
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
"""Using the tk class """
window = Tk()
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def timer_reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    checked_label.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps in (1, 3, 5, 7):
        count_down(work_sec)
        timer_label.config(text="Work Time", fg=RED)
    elif reps == 8:
        count_down(long_break_sec)
        timer_label.config(text="Long Break", fg=GREEN)
    elif reps in (2, 4, 6):
        count_down(short_break_sec)
        timer_label.config(text="Short Break", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        word_session = math.floor(reps/2)
        for _ in range(word_session):
            marks += "✔"
        checked_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

"""Giving the window title"""

window.title("Tomato Timer")
window.config(padx=100, pady=50, bg=YELLOW)

"""The timer label color and positioning and font configuration, positioning it in the axis along the the grid"""

timer_label = Label(text="TIMER", fg=GREEN, bg=YELLOW,
                    highlightthickness=0, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=1, row=0)

"""The graphical image for the timer is used as canvas """

canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)

""" Using the Phototimage class in tkinter to load the image into the canvas and create_image to position it into the canvas """

tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

""" The timer text that will consist inside the canvas image and work as a clock and rest using font's and color and its own text color as white and using grid to position them also """

timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 24, "bold"))
canvas.grid(column=1, row=1)

"""The start button to start  the timer and using the command to use specified funtion described above """
start_button = Button(text="Start", font=(
    FONT_NAME, 12, "bold"), highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

"""The reset button to reset  the timer and using the command to use specified funtion described above """
reset_button = Button(text="Reset", font=(
    FONT_NAME, 12, "bold"), highlightthickness=0, command=timer_reset)
reset_button.grid(column=2, row=2)

"""This label will display a check tick at the end of the timer duration"""
checked_label = Label(fg=GREEN, bg=YELLOW, font=15)
checked_label.grid(column=1, row=3)

window.mainloop()
