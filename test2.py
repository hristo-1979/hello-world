import tkinter as tk

def opnwindow2():
    window2 = tk.Tk()
    window2.geometry('200x100')
    window2.title('window2')

window1 = tk.Tk()
window1.geometry('640x480')
window1.title('test2 program')

label1 = tk.Label(text='Hello World!', bg='red', fg='white')
button1 = tk.Button(text='Click Me!', bg='yellow', fg='blue', command=opnwindow2)

label1.pack()
button1.pack()

window1.mainloop()
