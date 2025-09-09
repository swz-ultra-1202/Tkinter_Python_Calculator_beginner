import tkinter as tk

# -------------------- Colors --------------------
BG_COLOR = "#1e1e1e"
BTN_COLOR = "#2c2c2c"
OP_COLOR = "#ffffff"
CE_COLOR = "#f39c12"
TEXT_COLOR = "#ffffff"

# -------------------- Functions --------------------
def add_to_expression(value):
    current = entry.get()
    if current == "0":
        entry.delete(0, tk.END)
    entry.insert(tk.END, value)

def clear_entry():
    entry.delete(0, tk.END)
    entry.insert(0, "0")

def calculate():
    try:
        result = str(eval(entry.get().replace("x", "*").replace("÷", "/")))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# -------------------- GUI Setup --------------------
root = tk.Tk()
root.title("Python Calculator")
root.configure(bg=BG_COLOR)
root.resizable(False, False)

# -------------------- Entry --------------------
entry = tk.Entry(root, width=15, font=("Arial", 24), borderwidth=0, bg=BG_COLOR, fg=TEXT_COLOR, justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=15)
entry.insert(0, "0")

# -------------------- Buttons --------------------
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("x", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("ce", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, bg="#ffffff", fg=BG_COLOR, font=("Arial", 18),
                        command=calculate, width=5, height=2, borderwidth=0)
    elif text == "ce":
        btn = tk.Button(root, text=text, bg=CE_COLOR, fg=BG_COLOR, font=("Arial", 18),
                        command=clear_entry, width=5, height=2, borderwidth=0)
    elif text in {"+", "-", "x", "/"}:
        btn = tk.Button(root, text=text, bg=OP_COLOR, fg=BG_COLOR, font=("Arial", 18),
                        command=lambda val=text: add_to_expression(val), width=5, height=2, borderwidth=0)
    else:
        btn = tk.Button(root, text=text, bg=BTN_COLOR, fg=TEXT_COLOR, font=("Arial", 18),
                        command=lambda val=text: add_to_expression(val), width=5, height=2, borderwidth=0)

    btn.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
