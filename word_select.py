import random
import os 




def show_test(num):
    words = open("words.txt").read().split() 
    os.system("cls" if os.name == "nt" else "clear")
    return (" ".join(random.choices(words, k= num)))



show_test(20)