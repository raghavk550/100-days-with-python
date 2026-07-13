import tkinter, math
from tkinter import PhotoImage

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✔"
reps = 0
window = tkinter.Tk()
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_pressed():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0
    timer_label.config(text="TIMER", fg=GREEN)
    check_mark_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_pressed():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
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
    count_min = math.floor(count / 60)
    count_sec = math.floor(count % 60)
    # if count_sec < 10:
    #     count_sec = "0" + str(count_sec)

    canvas.itemconfig(timer_text, text=f"{count_min:02}:{count_sec:02}")
    if count > 1:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        global reps
        mark = ""
        for _ in range(math.floor(reps / 2)):
            mark += CHECKMARK
        check_mark_label.config(text=mark)
        start_pressed()

# ---------------------------- UI SETUP ------------------------------- #
window.title("Pomodoro")
window.config(background=YELLOW, padx=100, pady=50)

timer_label = tkinter.Label(text="TIMER", font=(FONT_NAME,50), foreground=GREEN, background=YELLOW)
timer_label.grid(row=0, column=1)

canvas = tkinter.Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
image = PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

start_button = tkinter.Button(text="Start", command=start_pressed, bg=YELLOW, highlightthickness=0)
start_button.grid(row=2, column=0)

reset_button = tkinter.Button(text="Reset", command=reset_pressed, bg=YELLOW, highlightthickness=0)
reset_button.grid(row=2, column=2)

check_mark_label = tkinter.Label(foreground=GREEN, background=YELLOW)
check_mark_label.grid(row=3, column=1)

window.mainloop()