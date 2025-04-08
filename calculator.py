import tkinter as tk
from tkinter import messagebox

# Main function for arithmetic operations
def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Cannot divide by zero.")

# Set up the window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x300")

# Entry fields
tk.Label(root, text="Enter First Number").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter Second Number").pack()
entry2 = tk.Entry(root)
entry2.pack()

# Buttons for operations
tk.Button(root, text="+", width=10, command=lambda: calculate('+')).pack(pady=5)
tk.Button(root, text="-", width=10, command=lambda: calculate('-')).pack(pady=5)
tk.Button(root, text="*", width=10, command=lambda: calculate('*')).pack(pady=5)
tk.Button(root, text="/", width=10, command=lambda: calculate('/')).pack(pady=5)

# Result label
result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=10)

# Run the GUI loop
root.mainloop() 
