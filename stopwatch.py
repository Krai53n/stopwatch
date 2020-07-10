import tkinter as tk
from time import sleep
from playsound import playsound as pl


#### DRAW WINDOW
root = tk.Tk()
root.resizable(0, 0)
root.title('Stopwatch')


### SETTINGS
FONT = 'SourceCodePro-Bold'
SIZE = 50
SIZE_TEXT = 22
BACKGROUND = '#28313D'
FOREGORUND = '#f5b849'
FOREGROUND_ACTIVE = 'white'
FOREGROUND_RESET = '#DC6952'


### GLOBAL VARIABLES
counter_reset = 0


### FUNCTIONS
def cmd_start_stop():
    information = bttn_start_stop['text']
    information = information.lower()
    if information == 'start':
        bttn_start_stop['text'] = 'STOP'
        bttn_start_stop['fg'] = FOREGROUND_RESET
        __start()
    elif information == 'continue':
        bttn_start_stop['text'] = 'STOP'
        bttn_start_stop['fg'] = FOREGROUND_RESET
        __start()
    elif information == 'stop':
        bttn_start_stop['text'] = 'CONTINUE'
        bttn_start_stop['fg'] = FOREGORUND

def cmd_reset():
    global counter_reset
    counter_reset = 1

    lbl_hours['text'] = '00'
    lbl_minutes['text'] = '00'
    lbl_seconds['text'] = '00'

    bttn_start_stop['text'] = 'START'
    bttn_start_stop['fg'] = FOREGORUND

def __start():
    global counter_reset
    seconds = lbl_seconds['text']
    seconds = int(seconds)
    minutes = lbl_minutes['text']
    minutes = int(minutes)
    hours = lbl_hours['text']
    hours = int(hours)

    while 1:
        if seconds < 59:
            if (bttn_start_stop['text'] == 'CONTINUE' or
                    counter_reset == 1):
                counter_reset = 0
                break
            seconds = __time_go(seconds)
            lbl_seconds['text'] = seconds
            seconds = int(seconds)
            root.update()
            sleep(0.1)
            continue
        
        seconds = 0
        lbl_seconds['text'] = '00'

        if minutes < 59:
            if (bttn_start_stop['text'] == 'CONTINUE' or
                    counter_reset == 1):
                counter_reset = 0
                break
            minutes = __time_go(minutes)
            lbl_minutes['text'] = minutes
            minutes = int(minutes)
            continue

        minutes = 0
        lbl_minutes['text'] = '00'

        if hours < 59:
            if (bttn_start_stop['text'] == 'CONTINUE' or
                    counter_reset == 1):
                counter_reset = 0
                break
            hours = __time_go(hours)
            lbl_hours['text'] = hours
            hours = int(hours)


def __time_go(value):
    if value < 9:
        value += 1
        value = '0' + str(value)
    else:
        value += 1
        value = str(value)
    return value


### WIDGETS
lbl_hours = tk.Label(text = '00',
                      font = (FONT, SIZE),
                      fg = FOREGORUND)
lbl_hours.grid()

tk.Label(text = ':',
         font = (FONT, SIZE),
         fg = FOREGORUND).grid(row = 0, column = 1)

lbl_minutes = tk.Label(text = '00',
                        font = (FONT, SIZE),
                        fg = FOREGORUND)
lbl_minutes.grid(row = 0, column = 2)

tk.Label(text = ':',
         font = (FONT, SIZE),
         fg = FOREGORUND).grid(row = 0, column = 3)

lbl_seconds = tk.Label(text = '00',
                        font = (FONT, SIZE),
                        fg = FOREGORUND)
lbl_seconds.grid(row = 0, column = 4)

bttn_start_stop = tk.Button(text = 'START',
                            font = (FONT, SIZE_TEXT),
                            fg = FOREGORUND,
                            activeforeground = FOREGROUND_ACTIVE,
                            bd = 0,
                            command = cmd_start_stop)
bttn_start_stop.grid(row = 1, column = 2, columnspan = 3)

bttn_reset = tk.Button(text = 'RESET',
                       font = (FONT, SIZE_TEXT),
                       fg = FOREGROUND_RESET,
                       activeforeground = FOREGROUND_ACTIVE,
                       bd = 0,
                       command = cmd_reset)
bttn_reset.grid(row = 1, columnspan = 2)


root.mainloop()
