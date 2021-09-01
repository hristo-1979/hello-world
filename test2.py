import tkinter as tk

window1 = tk.Tk()
window1.geometry('640x480')
window1.title('test2 program')

window2 = tk.Tk()
window2.geometry('200x100')
window2.title('window2')

label1 = tk.Label(text='Hello World!', bg='red', fg='white')
button1 = tk.Button(text='Click Me!', bg='yellow', fg='blue')

label1.pack()
button1.pack()

window1.mainloop()
window2.mainloop()
