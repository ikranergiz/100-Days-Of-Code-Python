from tkinter import *

window = Tk()

window.title("Mile to Kilometers Converts Project")
window.minsize(width=500, height=500)
window.config(padx=100, pady=100)

mile_label = Label(text="Mile:", font=("Arial", 15, "bold"))
mile_label.grid(column=4, row=4)

kilometer_label = Label(text="Kilometer: ", font=("Arial", 15, "bold"))
kilometer_label.grid(column=0, row=0)


def button_clicked():
    mile = int(user_value.get())

    kilometer_label["text"] = f"Kilometer: {mile + 12}"


button = Button(text="Convert", command=button_clicked)
button.grid(column=5, row=7)

# Entry
user_value = Entry(width=10)
user_value.grid(column=5, row=4)

window.mainloop()
