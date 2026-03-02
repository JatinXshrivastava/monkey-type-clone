from word_select import show_test 
import os
from keyboard_input import read_keyboard


target = show_test(10)   #generate 30 random words 
typed = ""    # initial state of typed words 

def calculate_accuracy(target, typed):
    correct = 0
    for i in range(len(typed)):
        if i < len(target) and typed[i] == target[i]:
            correct += 1
    if len(typed) == 0:
        return 0
    return (correct / len(typed)) * 100

print(target)
def clear():
    os.system("cls" if os.name == "nt" else "clear")

clear()
print("TYPE THIS:\n")
print("="*100)
print(target)
print("="*100)
print("\nYour typing:    (press ESC to exit) \n")

accuracy = calculate_accuracy(target, typed)
print(f"\nAccuracy: {accuracy:.2f}%")

read_keyboard()

