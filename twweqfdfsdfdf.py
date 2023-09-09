import tkinter as tk


window = tk.Tk()
window.title("tkinter.test")
window.geometry("800x600")

def change_label_text(text):
    label["text"] = text


def show_message():
    label["text"] = entry.get()

label = tk.Label(window, text="Здесь появится", background="#DAA520", font=("Impact", 19),)

entry = tk.Entry(font=("Impact", 18))

button = tk.Button(text="Напиши в окошке то что ты хочешь", font=("Impact", 17), command=show_message) 
"""lambda: change_label_text("КИРИЕШКИ")"""

label.pack(anchor="nw", padx=6, pady=6)
entry.pack(anchor="nw", padx=6, pady=6)
button.pack(anchor="nw", padx=6, pady=6)


window.mainloop()
