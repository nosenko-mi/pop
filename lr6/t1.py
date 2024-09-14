import tkinter as tk
from tkinter import messagebox, scrolledtext
import math


def f(x):
    e = math.exp(2 * x)
    return (e - 8) / (x + 3)


def calculate():
    try:
        min_x = float(entry_min_x.get())
        max_x = float(entry_max_x.get())
        delta_x = float(entry_delta_x.get())

        if delta_x <= 0:
            messagebox.showerror("Error", "delta_x must be a positive number.")
            return
        

        i = min_x
        results = []
        output_area.delete(1.0, tk.END)
        while i <= max_x:
            tmp = f(i)
            results.append(tmp)
            output_area.insert(tk.END, f"x={i:.2f}; y={tmp:.2f}\n")
            i += delta_x

        return results

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")


root = tk.Tk()
root.title("nmi_l6_t1")
tk.Label(root, text="Calculate y=(e^(2*x) - 8) / (x + 3)").grid(row=0, column=0, padx=10, pady=10)

tk.Label(root, text="min_x:").grid(row=1, column=0, padx=10, pady=5)
entry_min_x = tk.Entry(root)
entry_min_x.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="max_x:").grid(row=2, column=0, padx=10, pady=5)
entry_max_x = tk.Entry(root)
entry_max_x.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="delta_x:").grid(row=3, column=0, padx=10, pady=5)
entry_delta_x = tk.Entry(root)
entry_delta_x.grid(row=3, column=1, padx=10, pady=5)

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

output_area = scrolledtext.ScrolledText(root, width=50, height=10)
output_area.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
