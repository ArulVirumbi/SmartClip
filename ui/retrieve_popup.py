import tkinter as tk
from core import storage
import pyautogui

def show_retrieve_popup_and_get_key():
    result = {'key': None}

    def update_list(*args):
        typed = entry.get().strip().lower()
        listbox.delete(0, tk.END)
        matches = []
        for key in all_keys:
            if typed in key.lower():
                matches.append(key)
                listbox.insert(tk.END, key)
        if matches:
            listbox.selection_set(0)

    def on_select(event=None):
        try:
            selected = listbox.get(listbox.curselection())
            result['key'] = selected
        except:
            result['key'] = entry.get().strip()
        popup.quit()

    popup = tk.Tk()
    popup.title("Retrieve Snippet")
    popup.attributes('-topmost', True)
    popup.geometry("400x200")
    popup.resizable(False, False)

    tk.Label(popup, text="Search Key:", font=("Segoe UI", 10)).pack(pady=5)

    entry = tk.Entry(popup, font=("Segoe UI", 12))
    entry.pack(pady=5, padx=20, fill='x')

    listbox = tk.Listbox(popup, font=("Segoe UI", 11), height=6)
    listbox.pack(pady=5, padx=20, fill='both', expand=True)

    all_keys = storage.get_all_keys()

    entry.bind('<KeyRelease>', update_list)
    entry.bind('<Return>', on_select)
    listbox.bind('<Double-1>', on_select)

    def click_entry_box():
        popup.update_idletasks()
        x = popup.winfo_rootx() + 50
        y = popup.winfo_rooty() + 50
        pyautogui.click(x, y)
        update_list()

    popup.after(300, click_entry_box)
    popup.mainloop()
    try:
        popup.destroy()
    except tk.TclError:
        pass

    return result['key']