
from tkinter import *
from random import randint


root = Tk()
root.title('Password Generator')
root.geometry('500x350')

# Function to generate a random password
def new_rand():
    length = int(entry.get())  
    password = ''.join(chr(randint(33, 126)) for _ in range(length)) 
    pw_entry.delete(0, END)  
    pw_entry.insert(0, password)  


def clipper():
    root.clipboard_clear()  
    root.clipboard_append(pw_entry.get()) 
    root.update()  


lf = LabelFrame(root,bg="orange", text="Length of characters?")
lf.pack(pady=20)
entry = Entry(lf, font=("Helvetica", 24))
entry.pack(pady=20, padx=20)


pw_entry = Entry(root, text='', font=("Helvetica", 24))
pw_entry.pack(pady=20)


myframe = Frame(root)
myframe.pack(pady=20)


button = Button(myframe,bg="light green", text="Generate Password", command=new_rand)
button.grid(row=0, column=0, padx=10)

clip_button = Button(myframe,bg="yellow", text="Copy to Clipboard", command=clipper)
clip_button.grid(row=0, column=1, padx=20)


root.mainloop()
