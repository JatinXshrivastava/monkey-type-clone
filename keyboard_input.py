import keyboard
from WPM_meter import WPMMeter 

wpm_meter= WPMMeter() 

print("Start typing... (press ESC to stop)")


def read_keyboard(target , wpm_meter) :
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

            # print("\r" + " " * 200, end="") 
            print("\r" + typed + f"         | WPM: {wpm:.2f}" , end="") 
    


