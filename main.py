import keyboard
import threading
import time
import pyperclip
from ui.save_popup import show_save_popup
from ui.retrieve_popup import show_retrieve_popup_and_get_key
from core import storage

import win32event
import win32api
import winerror

from pystray import Icon, MenuItem, Menu
from PIL import Image, ImageDraw
import threading
import sys

def create_image():
    # Small sky blue circle icon
    image = Image.new('RGB', (64, 64), color=(0, 0, 0, 0))
    d = ImageDraw.Draw(image)
    sky_blue = (135, 206, 235)
    d.ellipse((16, 16, 48, 48), fill=sky_blue)
    return image

def on_exit(icon, item):
    icon.stop()
    sys.exit(0)

def setup_tray():
    icon = Icon("SmartClip", create_image(), menu=Menu(
        MenuItem("Exit", on_exit)
    ))
    threading.Thread(target=icon.run, daemon=True).start()


mutex = win32event.CreateMutex(None, False, "SmartClipSingleton")
last_error = win32api.GetLastError()
if last_error == winerror.ERROR_ALREADY_EXISTS:
    # Another instance is running
    print("SmartClip is already running.")
    exit(0)


def handle_save_shortcut():
    keyboard.press_and_release("ctrl+c")
    # pyautogui.hotkey("ctrl", "c")
    time.sleep(0.1)  # Small delay to allow clipboard to update
    selected_text = pyperclip.paste().strip()
    if not selected_text:
        return
    threading.Thread(target=show_save_popup, args=(selected_text,), daemon=True).start()

def handle_retrieve_shortcut():
    def retrieve():
        key = show_retrieve_popup_and_get_key()
        if not key:
            return
        result = storage.get_entry(key)
        if result:
            keyboard.write(result)  # Automatically types the result where the cursor is

    threading.Thread(target=retrieve, daemon=True).start()

def main():
    setup_tray()
    # keyboard.add_hotkey('ctrl+alt+c', handle_save_shortcut)
    # keyboard.add_hotkey('ctrl+alt+v', handle_retrieve_shortcut)
    keyboard.add_hotkey("ctrl+alt+c", lambda: threading.Thread(target=handle_save_shortcut, daemon=True).start())
    keyboard.add_hotkey("ctrl+alt+v", lambda: threading.Thread(target=handle_retrieve_shortcut, daemon=True).start())

    print("SmartClip running in background. Press Ctrl+Alt+C to save, Ctrl+Alt+V to retrieve.")
    keyboard.wait()  # Keeps the listener alive

if __name__ == '__main__':
    main()
