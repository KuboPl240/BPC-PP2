import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Function")

        self.supported_functions = {"sin", "cos", "tan", "xcos"}

        self.function_label = tk.Label(root, text="Function")
        self.function_label.grid(row=0, column=0)

        self.function_entry = tk.Entry(root, width=15)
        self.function_entry.grid(row=0, column=1)

        self.lower_limit_entry = tk.Entry(root, width=10)
        self.lower_limit_entry.grid(row=0, column=2)

        self.upper_limit_entry = tk.Entry(root, width=10)
        self.upper_limit_entry.grid(row=0, column=3)

        self.draw_button = tk.Button(root, text="Draw", command=self.plot_function)
        self.draw_button.grid(row=0, column=4)

        self.unit_var = tk.StringVar(value="radians")
        self.radians_button = tk.Radiobutton(root, text="Radians", variable=self.unit_var, value="radians")
        self.radians_button.grid(row=1, column=0)
        self.degrees_button = tk.Radiobutton(root, text="Degrees", variable=self.unit_var, value="degrees")
        self.degrees_button.grid(row=1, column=1)

        self.figure, self.ax = plt.subplots(figsize=(5, 4))
        self.canvas = FigureCanvasTkAgg(self.figure, master=root)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.grid(row=2, column=0, columnspan=5)

    def validate_float(self, value, field_name):
        try:
            return float(value)
        except ValueError:
            messagebox.showerror("Invalid Input", f"Please enter a valid float for {field_name}.")
            raise

    def xcos(self, x):
        with np.errstate(divide="ignore", invalid="ignore"):
            result = np.where(x == 0, 1.0, np.cos(x) / x)
        return result


    def plot_function(self):
        function_text = self.function_entry.get().strip()
        try:
            lower_limit = self.validate_float(self.lower_limit_entry.get(), "Lower Limit")
            upper_limit = self.validate_float(self.upper_limit_entry.get(), "Upper Limit")
        except ValueError:
            return

        if lower_limit >= upper_limit:
            messagebox.showerror("Invalid Input", "Lower limit must be less than the upper limit.")
            return

        try:
            if self.unit_var.get() == "degrees":
                lower_limit = np.radians(lower_limit)
                upper_limit = np.radians(upper_limit)

            x = np.linspace(lower_limit, upper_limit, 500)
            
            if function_text == "sin":
                y = np.sin(x)
            elif function_text == "cos":
                y = np.cos(x)
            elif function_text == "tan":
                y = np.tan(x)
            elif function_text == "xcos":
                y = np.sinc((x+np.pi/2)/np.pi)
            else:
                messagebox.showerror("Invalid Function", f"Unsupported function '{function_text}'.")
                return



            y = np.nan_to_num(y, nan=np.inf, posinf=np.inf, neginf=-np.inf)
        except Exception as e:
            messagebox.showerror("Error", f"Error evaluating the function: {e}")
            return

        self.ax.clear()
        self.ax.plot(x, y, label=function_text)
        self.ax.set_title("Function Plot")
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("y")
        self.ax.legend()
        self.canvas.draw()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

