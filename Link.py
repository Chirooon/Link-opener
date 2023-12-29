import tkinter as tk
from tkinter import messagebox
import webbrowser

def open_link():
    link = entry.get()
    try:
        count = int(count_entry.get())
        for _ in range(count):
            webbrowser.open_new(link)
    except ValueError:
        messagebox.showerror("Fehler", "Bitte gib eine gültige Anzahl ein.")


root = tk.Tk()
root.title("Link Öffner")


label = tk.Label(root, text="Link:")
label.pack(pady=10)
entry = tk.Entry(root, width=50)
entry.pack(pady=10)


count_label = tk.Label(root, text="Anzahl:")
count_label.pack(pady=10)
count_entry = tk.Entry(root, width=10)
count_entry.pack(pady=10)


open_button = tk.Button(root, text="Link öffnen", command=open_link)
open_button.pack(pady=20)

# GUI starten
root.mainloop()
