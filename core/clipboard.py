import pyperclip

def get_clipboard_text():
    return pyperclip.paste()

def set_clipboard_text(text):
    pyperclip.copy(text)
