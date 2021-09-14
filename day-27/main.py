import tkinter

window = tkinter.Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=500)

# Label

my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "italic"))  # italic, normal, bold
my_label.pack()  # left, bottom, expand=True **kw?

import turtle

tim = turtle.Turtle()
tim.write()

window.mainloop()
