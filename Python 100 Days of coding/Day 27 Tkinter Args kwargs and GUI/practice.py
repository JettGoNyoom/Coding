from tkinter import *

window = Tk()
window.title("My first GUI Program :P")
window.minsize(width=500, height=300)

# Create components inside the window
# Label
my_label = Label(text="This is a label!", font=("Times New Roman",24, "italic"))
my_label.pack() # NEEDS to pack the label onto the screen

# my_label['text'] = "New Text"

# Button
def button_clicked():
    # print("Button clicked.")
    new_text = input.get()
    my_label['text'] = new_text

button = Button(text="Click me!", command=button_clicked)
button.pack()

# Entry
input = Entry(width=10)
input.pack()

# Keeps the window up on screen
# ALWAYS HAS TO BE AT THE VERY END OF THE PROGRAM
window.mainloop()