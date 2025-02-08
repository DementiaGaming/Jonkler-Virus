import os
import shutil
import time
import pygame
import pyautogui
import ctypes
import customtkinter
from PIL import Image, ImageTk
import random
import sys

# Gets users desktop path (for later)
desktop_path = os.environ.get('USERPROFILE') + "\\Onedrive\\Desktop"

soundPath = "sounds\jonkler.mp3"

pygame.mixer.init()
pygame.mixer.music.load(soundPath)

windows_list = []


SPI_SETDESKWALLPAPER = 20  # Set desktop wallpaper
SPIF_UPDATEINIFILE = 0x01  # Update the user profile
SPIF_SENDCHANGE = 0x02  # Broadcast to all windows

def change_wallpaper(image_path):
    # Make sure the path is absolute
    abs_path = os.path.abspath(image_path)
    
    # Call the SystemParametersInfo function to change the wallpaper
    ctypes.windll.user32.SystemParametersInfoW(
        SPI_SETDESKWALLPAPER,
        0,
        abs_path,
        SPIF_UPDATEINIFILE | SPIF_SENDCHANGE
    )

def playSound():
    pygame.mixer.music.play(loops=-1)

def writeToDesktop(count):
    for i in range(count):
        source_file = "images\\jonkler.jpg"
        file_path = os.path.join(desktop_path, f"jonkler{i}.jpg")
        shutil.copy(source_file, file_path)
        time.sleep(0.1)

def openNotepadAndWrite():
    pyautogui.press("winleft")
    time.sleep(0.1)
    pyautogui.write("notepad", interval=0.1)
    time.sleep(0.1)
    pyautogui.press("enter")
    time.sleep(1.5)
    pyautogui.write("Why so serious?", interval=0.1)
    time.sleep(2)
    os.system("taskkill /f /im notepad.exe")
    pyautogui.hotkey("winleft","d")

def fakeBSOD():
    root = customtkinter.CTk()
    root.geometry("1920x1080")
    root.attributes("-fullscreen", True)

    image_path = "images/bsod.png"
    image = Image.open(image_path)

    width, height = root.winfo_screenwidth(), root.winfo_screenheight()  
    image = image.resize((width, height), Image.Resampling.LANCZOS)  

    img_tk = ImageTk.PhotoImage(image)

    bg_label = customtkinter.CTkLabel(root, image=img_tk, text="")
    bg_label.image = img_tk 
    bg_label.place(relx=0, rely=0, relwidth=1, relheight=1) 

    pygame.mixer.music.load("sounds\\error.mp3")
    pygame.mixer.music.play()

    root.mainloop()

playSound()
openNotepadAndWrite()
writeToDesktop(100)
change_wallpaper("images\\jonkler.jpg")
time.sleep(2)
fakeBSOD()
#test