import tkinter

# Create a window and its properties
window = tkinter.Tk()
window.title("Mile to Km Converter")
# window.minsize(width=500, height=300)
window.config(padx=100, pady=50)


# Calculate miles to kilometres
def calculation():
    miles_f = float(miles_entry.get())
    k = 1.609344 * miles_f
    km_result_label.config(text=f"{k}")


# Display a label
equal_to = tkinter.Label(text="is equal to")
equal_to.grid(column=0, row=1)

miles = tkinter.Label(text="Miles")
miles.grid(column=2, row=0)

km = tkinter.Label(text="Km")
km.grid(column=2, row=1)

km_result_label = tkinter.Label(text="0")
km_result_label.grid(column=1, row=1)

# Display entry
miles_entry = tkinter.Entry()
miles_entry.grid(column=1, row=0)

# Display button
calculate = tkinter.Button(text="Calculate", command=calculation)
calculate.grid(column=1, row=2)

window.mainloop()
