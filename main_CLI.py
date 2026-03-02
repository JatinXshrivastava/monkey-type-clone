from word_select import show_test 
import os
from keyboard_input import read_keyboard
from WPM_meter import WPMMeter 
from accuracy_meter import AccuracyMeter


target = show_test(10)   #generate 30 random words 
typed = ""    # initial state of typed words 
wpm_meter = WPMMeter()
accuracy_meter = AccuracyMeter(target) 

print(target)

def clear():
    os.system("cls" if os.name == "nt" else "clear")

clear()
print("TYPE THIS:\n")
print("="*100)
print(target)
print("="*100)
print("\nYour typing:    (press ESC when done) \n")

read_keyboard(target, wpm_meter, accuracy_meter)




