import keyboard
from WPM_meter import WPMMeter 

wpm_meter= WPMMeter() 

print("Start typing... (press ESC to stop)")


def read_keyboard(target , wpm_meter, accuracy_meter) :
    typed = ""  
    started = False
    while True:
        event = keyboard.read_event()

        if event.event_type == keyboard.KEY_DOWN:
            key = event.name

            if not started:
                wpm_meter.start()
                started = True

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

            wpm = wpm_meter.get_wpm(len(typed))
            accuracy = accuracy_meter.get_raw_accuracy()
            errors = accuracy_meter.get_error_count() 

            
            # Clear previous output (200 spaces overwrites old text)

            # Print updated typed text
            # print("\r" , end="")
            print("\r" + typed, end="")

    print("")
    print(f"WPM: {wpm:.2f} | Accuracy: {accuracy:.2f}% | Errors: {errors}")
