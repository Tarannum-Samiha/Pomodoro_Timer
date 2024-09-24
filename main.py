from tkinter import *
import math

PINK = "#ffb3ba"
ORANGE = "#ffc299"
BLUE = "#bae1ff"
GREEN = "#90ee90"
YELLOW = "#ffffba"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK = 5
LONG_BREAK = 20
SECONDS = 60
lap = 0
set_timer = None

# Reset mechanism


def reset_timer():
    global set_timer, lap
    window.after_cancel(set_timer)

    pomodoro_label.config(text="Pomodoro Timer")
    canvas.itemconfig(timer_count, text="00:00")
    check_mark.config(text="")
    lap = 0


# Timer mechanism


def timer():
    global lap
    lap += 1

    if lap % 8 == 0:
        count_down(LONG_BREAK * SECONDS)
        pomodoro_label.config(text="LONG BREAK ☕")

    elif lap % 2 == 0:
        count_down(SHORT_BREAK * SECONDS)
        pomodoro_label.config(text="SHORT BREAK ☕")

    else:
        count_down(WORK_MIN * SECONDS)
        pomodoro_label.config(text="WORK 📝")

# Counting mechanism


def count_down(count):

    count_minute = math.floor(count / 60)
    count_second = count % 60

    if count_second < 10:
        count_second = "0" + f"{count_second}"

    canvas.itemconfig(timer_count, text=f"{count_minute}:{count_second}")
    if count > 0:
        global set_timer
        set_timer = window.after(1000, count_down, count-1)
    else:
        timer()
        mark = ""
        sessions = math.floor(lap/2)
        for i in range(sessions):
            mark += "✔"
        check_mark.config(text=mark)



# Creating a screen

window = Tk()
window.minsize(width=500, height=300)
window.title("Pomodoro")
window.config(bg=YELLOW, padx=100, pady=100)


canvas = Canvas(width=280, height=200, bg=YELLOW, highlightthickness=0)
cat_image = PhotoImage(file="cat.png")
canvas.create_image(140, 90, image=cat_image)
timer_count = canvas.create_text(140, 180, text="00:00", fill=ORANGE, font=(FONT_NAME, 30, "bold"))
canvas.grid(row=0, column=1)

pomodoro_label = Label(text="Pomodoro Timer", font=(FONT_NAME, 18, "bold"), bg=YELLOW, fg=PINK)
pomodoro_label.grid(row=1, column=1)

start = Button(text="Start", font=(FONT_NAME, 10, "normal"), highlightthickness=0, bg=BLUE, activebackground=PINK, command=timer)
start.grid(row=2, column=0)

reset = Button(text="Reset", font=(FONT_NAME, 10, "normal"), highlightthickness=0, bg=BLUE, activebackground=PINK, command=reset_timer)
reset.grid(row=2, column=2)

check_mark = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"))
check_mark.grid(row=3, column=1)
check_mark.config(padx=10, pady=10)


window.mainloop()

