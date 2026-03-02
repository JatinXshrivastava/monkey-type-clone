import tkinter as tk
from typing_canvas import TypingCanvas
from word_select import show_test

def start_test():
    target = show_test(10)
    canvas = TypingCanvas(target)
    canvas.run()

root = tk.Tk()
root.title("Monkeytype Clone")
root.geometry("400x200")

tk.Label(root, text="Monkeytype Clone", font=("Arial", 22)).pack(pady=20)

start_btn = tk.Button(root, text="Start Test", font=("Arial", 14), command=start_test)
start_btn.pack(pady=10)

root.mainloop()