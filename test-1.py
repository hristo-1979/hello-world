import tkinter as tk

window = tk.Tk()
window.title("test app")
window.geometry("450x350")

label1 = tk.Label(text="Hello there!")
button1 = tk.Button(text="Click Me!")
label2 = tk.Label(text="I am number 2")

label1.pack()
button1.pack()
label2.pack()

window.mainloop()
