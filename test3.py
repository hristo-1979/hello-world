import tkinter as tk

window = tk.Tk()
window.geometry('600x480')
window.title('test3 program')
window.configure(background='yellow')

label1 = tk.Label(bg='red', text='Hello There!')
button1 = tk.Button(bg='blue', fg='magenta', text='Click Me!')

label1.pack()
button1.pack()

window.mainloop()
