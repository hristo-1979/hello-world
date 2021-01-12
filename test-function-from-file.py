import tkinter as tk
from onclick import onclick

def onclick_local():
    label1.configure(text=onclick(label1.cget("text")))

def btn2_click():
    label1.configure(text="result")

window = tk.Tk()
window.geometry("450x350")
window.title("Test App")

label1 = tk.Label(text="result", font="Helvetica 12 bold", bg="gray"
                  , fg="white", height=5, width=20)
label2 = tk.Label(text="Click the button", font="Helvetica 12 bold"
                  , bg="magenta", fg="white", height=1, width=20)
button1 = tk.Button(text="Click Me!", font="Helvetica 12 bold", bg="red"
                    , fg="white", height=5, width=20, command=onclick_local)
button2 = tk.Button(text="Reset", font="Helvetica 12 bold", bg="yellow"
                    , fg="white", height=5, width=20, command=btn2_click)

label2.pack()
button1.pack()
button2.pack()
label1.pack()

window.mainloop()
