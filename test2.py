import tkinter as tk

window = tk.Tk()
window.geometry('600x480')
window.title('test2 program')

label1 = tk.Label(text='Hello World!')
button1 = tk.Button(text='Click Me!')

label1.pack()
button1.pack()

window.mainloop()
