import tkinter as tk

window = tk.Tk()
window.geometry('640x480')
window.title('test2 program')

label1 = tk.Label(text='Hello World!', bg='red', fg='white')
button1 = tk.Button(text='Click Me!', bg='yellow', fg='blue')

label1.pack()
button1.pack()

window.mainloop()
