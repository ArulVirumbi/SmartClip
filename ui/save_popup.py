import tkinter as tk
from core import storage
import pyautogui

def show_save_popup(selected_text):
    def on_ok():
        key = entry.get().strip()
        if key:
            storage.save_entry(key, selected_text)
        popup.destroy()

    popup = tk.Tk()
    popup.title("Save Snippet")
    popup.attributes('-topmost', True)
    popup.geometry("400x120")
    popup.resizable(False, False)

    tk.Label(popup, text=f"Save selected text as key:", font=("Segoe UI", 10)).pack(pady=10)

    entry = tk.Entry(popup, font=("Segoe UI", 12))
    entry.pack(pady=5, padx=20, fill='x')
    entry.focus()

    entry.bind("<Return>", lambda e: on_ok())

    def click_entry_box():
        popup.update_idletasks()
        x = popup.winfo_rootx() + 50
        y = popup.winfo_rooty() + 50
        pyautogui.click(x, y)

    popup.after(300, click_entry_box)

    popup.mainloop()
