import tkinter as tk
from tkinter import messagebox

lessons = [
    {"word": "Hello", "translation": "Hola"},
    {"word": "Thank you", "translation": "Gracias"},
    {"word": "Goodbye", "translation": "Adiós"},
]

index = 0

def show_lesson():
    word_label.config(text=f"Word: {lessons[index]['word']}")
    translation_label.config(text="Translation: ???")

def show_translation():
    translation_label.config(text=f"Translation: {lessons[index]['translation']}")

def next_lesson():
    global index
    index = (index + 1) % len(lessons)
    show_lesson()

root = tk.Tk()
root.title("Language Learning App")

word_label = tk.Label(root, text="", font=("Arial", 18))
word_label.pack(pady=10)

translation_label = tk.Label(root, text="", font=("Arial", 14))
translation_label.pack(pady=5)

tk.Button(root, text="Show Translation", command=show_translation).pack(pady=5)
tk.Button(root, text="Next Word", command=next_lesson).pack(pady=5)

show_lesson()
root.mainloop()
