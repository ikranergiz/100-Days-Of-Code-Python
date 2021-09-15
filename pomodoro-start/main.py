from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#FCFFA6"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# colorhunt.co
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer

    window.after_cancel(timer)
    timer_label.config(text="Timer")
    check_mark_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")

    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():

    global reps
    reps += 1

    work_sec = 5
    short_break_sec = 3
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)

    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)

    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    global timer

    count_min = math.floor(count / 60)  # 4.8 = 4
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")  # for chancing canvas object we use itemconfig func

    if count > 0:
        timer = window.after(1000, count_down, count - 1)

    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)

        for _ in range(work_sessions):
            marks += "✔"
        check_mark_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  # white line disappeared
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)  # required x and y. image expects a Photoimage object.
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Label
timer_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

# CheckMark-Label
check_mark_label = Label(font=(FONT_NAME, 14, "bold"), fg=GREEN, bg=YELLOW)
check_mark_label.grid(column=1, row=3)

# Start-Button
start_button = Button(text="Start", font=(FONT_NAME, 10, "bold"), command=start_timer)
start_button.grid(column=0, row=2)

# Reset-Button
reset_button = Button(text="Reset", font=(FONT_NAME, 10, "bold"), command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
