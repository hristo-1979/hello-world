import tkinter as tk

window = tk.Tk()
window.title("test app")
window.geometry("450x350")

label1 = tk.Label(text="Hello there!")
button1 = tk.Button(text="Click Me!")

label1.pack()
button1.pack()

window.mainloop()
