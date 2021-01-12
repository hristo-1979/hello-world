import tkinter as tk
from onclick import onclick

window = tk.Tk()
window.geometry("450x350")
window.title("Test App")

label1 = tk.Label(text="result")
label2 = tk.Label(text="Click the button")
button1 = tk.Button(text="Click Me!", command=onclick)

label2.pack()
button1.pack()
label1.pack()

window.mainloop()
