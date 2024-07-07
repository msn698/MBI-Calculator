import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog

def calculate_bmi_logic(height, weight):
    if height <= 0 or weight <= 0:
        raise ValueError("Height and weight must be greater than zero.")
    
    bmi = weight / (height ** 2)
    
    if bmi < 18.5:
        category = "Underweight"
        color = "lightblue"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
        color = "lightgreen"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
        color = "orange"
    else:
        category = "Obese"
        color = "red"
    
    return bmi, category, color

def convert_units(height, weight, height_unit, weight_unit):
    if height_unit == "cm":
        height = height / 100
    elif height_unit == "feet":
        height = height * 0.3048
    
    if weight_unit == "pounds":
        weight = weight * 0.453592
    
    return height, weight

def calculate_bmi():
    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())
        height_unit = height_unit_var.get()
        weight_unit = weight_unit_var.get()

        height, weight = convert_units(height, weight, height_unit, weight_unit)

        bmi, category, color = calculate_bmi_logic(height, weight)
        bmi_result_label.config(text=f"BMI: {bmi:.2f}")
        bmi_category_label.config(text=f"Category: {category}")
        bmi_category_label.config(bg=color)
    except ValueError as ve:
        messagebox.showerror("Invalid input", str(ve))
    except Exception:
        messagebox.showerror("Invalid input", "Please enter valid numbers for height and weight.")

def show_about():
    messagebox.showinfo("About", "BMI Calculator\nVersion 1.0\nCalculate your Body Mass Index (BMI) easily with different units of measurement.")

def save_results():
    bmi_result = bmi_result_label.cget("text")
    bmi_category = bmi_category_label.cget("text")
    if bmi_result == "BMI: " or bmi_category == "Category: ":
        messagebox.showerror("No Results", "Please calculate the BMI before saving.")
        return

    name = simpledialog.askstring("Input", "Enter your name:")
    if name is None:
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(f"Name: {name}\n{bmi_result}\n{bmi_category}")
        messagebox.showinfo("Saved", "Results saved successfully.")

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

# Set a minimum size for the window
root.minsize(400, 400)
root.configure(bg="lightgray")

# Create the menu
menu = tk.Menu(root)
root.config(menu=menu)
about_menu = tk.Menu(menu)
menu.add_cascade(label="Help", menu=about_menu)
about_menu.add_command(label="About", command=show_about)

# Create and place the instructions label
instructions_label = tk.Label(root, text="Enter your height and weight to calculate your BMI.", bg="lightgray")
instructions_label.pack(pady=10)

# Create and place the height label and entry
height_label = tk.Label(root, text="Height:", bg="lightgray")
height_label.pack(pady=5)
height_entry = tk.Entry(root)
height_entry.pack(pady=5)

# Create and place the height unit dropdown
height_unit_var = tk.StringVar(value="m")
height_unit_frame = tk.Frame(root, bd=2, relief=tk.SOLID, padx=5, pady=5, bg="lightgray")
height_unit_menu = tk.OptionMenu(height_unit_frame, height_unit_var, "m", "cm", "feet")
height_unit_menu.pack()
height_unit_frame.pack(pady=5)

# Create and place the weight label and entry
weight_label = tk.Label(root, text="Weight:", bg="lightgray")
weight_label.pack(pady=5)
weight_entry = tk.Entry(root)
weight_entry.pack(pady=5)

# Create and place the weight unit dropdown
weight_unit_var = tk.StringVar(value="kg")
weight_unit_frame = tk.Frame(root, bd=2, relief=tk.SOLID, padx=5, pady=5, bg="lightgray")
weight_unit_menu = tk.OptionMenu(weight_unit_frame, weight_unit_var, "kg", "pounds")
weight_unit_menu.pack()
weight_unit_frame.pack(pady=5)

# Create and place the calculate button
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack(pady=10)

# Create and place the result labels
bmi_result_label = tk.Label(root, text="BMI: ", bg="lightgray")
bmi_result_label.pack(pady=5)
bmi_category_label = tk.Label(root, text="Category: ", width=20, bg="lightgray")
bmi_category_label.pack(pady=5)

# Create and place the save button
save_button = tk.Button(root, text="Save Results", command=save_results)
save_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
