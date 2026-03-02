# 🐒 Monkeytype Clone (Python • Tkinter • Pygame)

A clean and lightweight **Monkeytype-inspired typing test** built using **Tkinter** (launcher) and **Pygame** (typing engine).  
This project recreates the core typing test experience of Monkeytype inside a modular Python environment.

> ⚠️ **Note:**  
> Only the **GUI version** is available and fully working.  
> The CLI version exists internally but is not maintained or recommended for use.

---

## 🎯 Features

### ✔ GUI Typing Test  
- Tkinter launcher window  
- Pygame typing test window  
- Automatic line wrapping  
- Per-character highlighting  
  - 🟩 Green = correct  
  - 🟥 Red = incorrect  
- WPM freezes the moment typing ends  
- Raw accuracy (mistakes are counted even if corrected)  
- Error count  
- Clean and modular codebase

### ✔ Inspired by Monkeytype  
This project is inspired by the amazing typing website  
**Monkeytype → https://monkeytype.com/**  
All mechanics are recreated purely for learning and personal development.

---

## 📦 Installation

## 1️⃣ Clone the repository

```sh
git clone https://github.com/YOUR-USERNAME/monkeytype-clone.git
cd monkeytype-clone
```

---

## 2️⃣ Install dependencies

Install everything from **requirements.txt**:

```sh
pip install -r requirements.txt
```

This installs the required libraries:

- `pygame`
- `keyboard`
- *(Tkinter comes bundled with Python on Windows/macOS)*

---

## 🚀 Running the GUI Version

Launch the main GUI:

```sh
python GUI/main_GUI.py
```

This will open:

- A Tkinter window with a **“Start Test”** button  
- A Pygame typing test window  

During the test:

- Target text is displayed  
- Typed characters appear with **green/red accuracy coloring**  
- When all words are typed, the test **auto-ends**  
- Final **WPM**, **accuracy**, and **errors** appear at the top  

---

## 🧠 Project Structure

```

main_GUI.py
typing_canvas.py
word_select.py
accuracy_meter.py
WPM_meter.py
words.txt
requirements.txt
README.md
```

Each file handles a separate part of the system, keeping the project clean and easy to maintain.

---

## 🙏 Credits

Special thanks to **Monkeytype → https://monkeytype.com/**  
This project is a Python-based recreation inspired by Monkeytype’s clean design and typing-test mechanics.  
Built purely for educational and personal use.

---

## ⭐ Support

If you like this project, consider starring ⭐ the repository!
