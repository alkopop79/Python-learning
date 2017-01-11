import Tkinter
from Tkinter import Tk, Label, Button

# Create the application window
window = Tk()
window.geometry("500x500")

# Create the user interface

def button_callback():
        print('click')

master=Tk()
my_label = Tkinter.Label(window, text="Hello World!")
my_label.grid(row=10, column=10)
my_button=Tkinter.Button(window,text="button", command=button_callback)

# Start the GUI event loop
window.mainloop()

