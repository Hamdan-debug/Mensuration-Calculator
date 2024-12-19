import tkinter as tk
from tkinter import messagebox

def calculate_area():
    shape = shape_var.get()
    try:
        if shape == 'square':
            side = float(entry1.get())
            area = side ** 2
            messagebox.showinfo("Result", f'The area of the square is {area:.2f}')

        elif shape == 'triangle':
            height = float(entry1.get())
            base = float(entry2.get())
            area = 0.5 * height * base
            messagebox.showinfo("Result", f'The area of the triangle is {area:.2f}')

        elif shape == 'rectangle':
            length = float(entry1.get())
            breadth = float(entry2.get())
            area = length * breadth
            messagebox.showinfo("Result", f'The area of the rectangle is {area:.2f}')

        elif shape == 'circle':
            radius = float(entry1.get())
            area = 3.14159 * radius ** 2
            messagebox.showinfo("Result", f'The area of the circle is {area:.2f}')

        elif shape == 'parallelogram':
            height = float(entry1.get())
            base = float(entry2.get())
            area = height * base
            messagebox.showinfo("Result", f'The area of the parallelogram is {area:.2f}')

        elif shape == 'trapezoid':
            side1 = float(entry1.get())
            side2 = float(entry2.get())
            height = float(entry3.get())
            area = 0.5 * (side1 + side2) * height
            messagebox.showinfo("Result", f'The area of the trapezoid is {area:.2f}')

        elif shape == 'ellipse':
            semi_major = float(entry1.get())
            semi_minor = float(entry2.get())
            area = 3.14159 * semi_major * semi_minor
            messagebox.showinfo("Result", f'The area of the ellipse is {area:.2f}')
            
        else:
            messagebox.showerror("Error", "Shape not recognized.")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

def update_fields(*args):
    shape = shape_var.get()
    
    # Hide all labels and entry fields by default
    entry1_label.grid_remove()
    entry1.grid_remove()
    entry2_label.grid_remove()
    entry2.grid_remove()
    entry3_label.grid_remove()
    entry3.grid_remove()
    
    # Update and show relevant input fields based on the shape
    entry1_label.grid(row=1, column=0, sticky="e")
    entry1.grid(row=1, column=1)
    
    if shape == 'square':
        entry1_label.config(text="Enter side length:")
    
    elif shape == 'triangle':
        entry1_label.config(text="Enter height:")
        entry2_label.config(text="Enter base length:")
        entry2_label.grid(row=2, column=0, sticky="e")
        entry2.grid(row=2, column=1)
    
    elif shape == 'rectangle':
        entry1_label.config(text="Enter length:")
        entry2_label.config(text="Enter breadth:")
        entry2_label.grid(row=2, column=0, sticky="e")
        entry2.grid(row=2, column=1)
    
    elif shape == 'circle':
        entry1_label.config(text="Enter radius:")
    
    elif shape == 'parallelogram':
        entry1_label.config(text="Enter height of parallelogram:")
        entry2_label.config(text="Enter length of base:")
        entry2_label.grid(row=2, column=0, sticky="e")
        entry2.grid(row=2, column=1)
    
    elif shape == 'trapezoid':
        entry1_label.config(text="Enter length of first base:")
        entry2_label.config(text="Enter length of second base:")
        entry3_label.config(text="Enter height:")
        entry2_label.grid(row=2, column=0, sticky="e")
        entry2.grid(row=2, column=1)
        entry3_label.grid(row=3, column=0, sticky="e")
        entry3.grid(row=3, column=1)
    
    elif shape == 'ellipse':
        entry1_label.config(text="Enter semi-major axis:")
        entry2_label.config(text="Enter semi-minor axis:")
        entry2_label.grid(row=2, column=0, sticky="e")
        entry2.grid(row=2, column=1)


root = tk.Tk()
root.title("2D Shapes Area Calculator")


root.columnconfigure(1, weight=1)


choose_shape_label = tk.Label(root, text="Choose a Shape:")
choose_shape_label.grid(row=0, column=0, sticky="w")


shape_var = tk.StringVar(value='square')
shapes = ['square', 'triangle', 'rectangle', 'circle', 'parallelogram', 'trapezoid', 'ellipse']
shape_dropdown = tk.OptionMenu(root, shape_var, *shapes)
shape_dropdown.grid(row=0, column=1, sticky="ew")


entry1_label = tk.Label(root, text="Enter value:")
entry1 = tk.Entry(root)

entry2_label = tk.Label(root, text="Enter second value:")
entry2 = tk.Entry(root)

entry3_label = tk.Label(root, text="Enter height:")
entry3 = tk.Entry(root)


calculate_button = tk.Button(root, text="Calculate Area", command=calculate_area)
calculate_button.grid(row=4, column=0, columnspan=2, pady=10)


shape_var.trace("w", update_fields)


update_fields()  
root.mainloop()
