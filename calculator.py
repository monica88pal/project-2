import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("300x450")
root.resizable(False, False)

expression = ""

def add_to_expression(value):
    global expression
    expression += str(value)
    label_text.set(expression)

def clear_expression():
    global expression
    expression = ""
    label_text.set("")

def calculate():
    global expression
    try:
        result = str(eval(expression))
        label_text.set(result)
        expression = result
    except:
        label_text.set("Error")
        expression = ""

label_text = tk.StringVar()

label = tk.Label(root, textvariable=label_text,
                 font=("Arial", 24), bg="white",
                 anchor="e")
label.pack(fill="both", ipadx=5, ipady=20)

frame = tk.Frame(root)
frame.pack()

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
]

for (text, row, col) in buttons:
    if text == "C":
        command = clear_expression
    else:
        command = lambda t=text: add_to_expression(t)

    tk.Button(frame, text=text, width=6, height=3, command=command)\
        .grid(row=row, column=col, padx=5, pady=5)

# = BUTTON (Full Row)
tk.Button(frame, text="=", width=26, height=3, bg="lightgreen",
          command=calculate)\
    .grid(row=5, column=0, columnspan=4, pady=10)

root.mainloop()