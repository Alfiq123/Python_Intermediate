import tkinter as tk
import ttkbootstrap as ttk

from os import path

app = ttk.Window(themename="cyborg")
app.title("Buttons")
app.resizable(width=False, height=False)


# Application.

# Button Function.
def button_func():
    print("Button Clicked")


# Button.
button_string = tk.StringVar(value="Button Variable")
button = ttk.Button(
    master=app,
    text="Click Me",
    command=button_func,
    textvariable=button_string
)
button.pack(padx=10, pady=10)

# Checkbutton.
checkbutton_var = tk.BooleanVar()
checkbutton = ttk.Checkbutton(
    master=app,
    text="Check 1",
    command=lambda: checkbutton_var.set(True),
    variable=checkbutton_var,
    onvalue=True,
    offvalue=False
)
checkbutton.pack(pady=10)

checkbutton2 = ttk.Checkbutton(
    master=app,
    text="Check 2",
    command=lambda: checkbutton_var.set(False)
)
checkbutton2.pack(pady=10)

# Radiobutton.
radiobutton_var = tk.StringVar()
radiobutton = ttk.Radiobutton(
    master=app,
    text="Radio 1",
    value="Radio 1",
    variable=radiobutton_var,
    command=lambda: print(radiobutton_var.get())
)
radiobutton.pack(pady=10)

radiobutton2 = ttk.Radiobutton(
    master=app,
    text="Radio 2",
    value="Radio 2",
    variable=radiobutton_var,
    command=lambda: print(radiobutton_var.get())
)
radiobutton2.pack(pady=10)


# Exercise.
def radiofunc():
    print(exercise_CheckBool.get())
    exercise_CheckBool.set(False)


exercise_StringRadio = tk.StringVar()

exercise_label = ttk.Label(
    master=app,
    text="Exercise:",
    font=("Times New Roman", 14, "bold")
)
exercise_label.pack(pady=10)

exercise_radio1 = ttk.Radiobutton(
    master=app,
    text="Radio AA",
    value="A",
    variable=exercise_StringRadio,
    command=radiofunc
)
exercise_radio1.pack(pady=10)

exercise_radio2 = ttk.Radiobutton(
    master=app,
    text="Radio BB",
    value="B",
    variable=exercise_StringRadio,
    command=radiofunc
)
exercise_radio2.pack(pady=10)

exercise_CheckBool = tk.BooleanVar()

exercise_check = ttk.Checkbutton(
    master=app,
    text="Check AB",
    variable=exercise_CheckBool,
    command=lambda: print(exercise_StringRadio.get())
)
exercise_check.pack(pady=10)

# Window Icon
app_icon_path = path.join(path.dirname(__file__),"Assets", "Icon_Python.png")
app_icon = tk.PhotoImage(file=app_icon_path)
app.iconphoto(True, app_icon)

# Run
app.mainloop()
