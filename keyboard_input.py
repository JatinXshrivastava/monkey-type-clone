import keyboard

print("Start typing... (press ESC to stop)")


def read_keyboard() :
    typed = ""  
    while True:
        event = keyboard.read_event()

        if event.event_type == keyboard.KEY_DOWN:
            key = event.name

            if key == "esc":
                break

            # space
            if key == "space":
                typed += " "
            # backspace 
            elif key == "backspace":
                typed = typed[:-1]
            # normal keys
            elif len(key) == 1:   # a-z, 0-9, punctuation
                typed += key

            print("\r" + " " * 200, end="")   # clears the line fully
            print("\r" + typed, end="")


