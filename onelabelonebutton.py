import tkinter as tk

def onclick():
    listbox1.configure(text="You Clicked Me!", bg="brown")


window = tk.Tk()
window.title("One Button One Label App")
window.geometry("450x350")

label1 = tk.Label(text="I am a label!", font="Helvetica 12 bold", bg="yellow", fg="white")
button1 = tk.Button(text="Click Me!", font="Helvetica 12 bold", bg="red", fg="white", command=onclick)
listbox1 = tk.Label(text="result here", font="Helvetica 12 bold", bg="magenta", fg="white")

listbox1.pack()
button1.pack()
label1.pack()

window.mainloop()
