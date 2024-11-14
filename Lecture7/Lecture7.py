import tkinter as tk
from tkinter import StringVar, IntVar

def count_text():
    input_text = input_field.get()
    count_mode = mode.get()
    if count_mode == 1:
        result = input_text.count('.')
    elif count_mode == 2:
        result = len(input_text.split())
    elif count_mode == 3:
        result = sum(char.isalpha() for char in input_text)
    result_label.config(text=str(result))

def revert_text():
    input_text = input_field.get()
    reversed_text = ' '.join(word[::-1] for word in input_text.split())
    input_field.delete(0, tk.END)
    input_field.insert(0, reversed_text)

root = tk.Tk()
root.title("String Count")

tk.Label(root, text="Input String").grid(row=0, column=0, columnspan=3)
input_field = tk.Entry(root, width=30)
input_field.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

mode = IntVar(value=3)
tk.Radiobutton(root, text="sentences", variable=mode, value=1).grid(row=2, column=0)
tk.Radiobutton(root, text="words", variable=mode, value=2).grid(row=2, column=1)
tk.Radiobutton(root, text="letters", variable=mode, value=3).grid(row=2, column=2)

result_label = tk.Label(root, text="0")
result_label.grid(row=3, column=1)

count_button = tk.Button(root, text="Count", command=count_text)
count_button.grid(row=3, column=2, pady=5)

revert_button = tk.Button(root, text="Revert", command=revert_text)
revert_button.grid(row=4, column=2, pady=5)

root.mainloop()
