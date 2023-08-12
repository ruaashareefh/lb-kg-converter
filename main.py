from tkinter import *

window = Tk()
window.title("Lb to Kg Converter")
window.minsize(width=350,height=200)
window.config(padx=70, pady=70)

def conversion():
    lbs = int(input.get())
    kg = round(lbs * 0.45359237, 2)
    conversion_label.config(text=kg)

button = Button(text="Calculate", command=conversion)
button.grid(column=1, row=2)

equal_to_label = Label(text="is equal to", font=("Arial", 18))
equal_to_label.grid(column=0, row=1)

lb_label = Label(text="Lb", font=("Arial", 18))
lb_label.grid(column=2, row=0)

input = Entry(width=10)
input.grid(column=1, row=0)

conversion_label = Label(text="0", font=("Arial", 18))
conversion_label.grid(column=1, row=1)

kg_label = Label(text="Kg", font=("Arial", 18))
kg_label.grid(column=2, row=1)






window.mainloop()
