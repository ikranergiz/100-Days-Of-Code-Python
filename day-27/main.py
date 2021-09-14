from tkinter import *

window = Tk()

window.title("My First GUI Program")
window.minsize(width=400, height=300)

# around all of edges has more space
window.config(padx=20, pady=20)


# but for specific
# my_label.config(padx=20, pady=20)


def button_clicked():
    my_label["text"] = "I got clicked"
    new_text = input.get()
    my_label.config(text=new_text)


# Label
my_label = Label(text="I am a label", font=("Arial", 8, "italic"))  # italic, normal, bold

# pack func takes **kw (dictionary) so text key can be chance like :
my_label["text"] = "new text"
my_label.config(text="New text")
# my_label.place(x=100, y=-12)
my_label.grid(column=0, row=0)

# Button
# command triggered this button_clicked method
button = Button(text="Click me !", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New button")
new_button.grid(column=2, row=0)

# Entry
input = Entry(width=10)
input.grid(column=3, row=2)
print(input.get())

# my_label.pack()  # left, bottom, expand=True expand??
# button.pack()
# input.pack()
window.mainloop()

# you have to choose one of place,pack and grid. You cannot use all of them at the same time

# pack always shows top of the page
# pack is a layout manager but place and grid is also layout manager
