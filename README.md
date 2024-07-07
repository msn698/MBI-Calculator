# BMI Calculator

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
  - [Main Application](#main-application)
  - [Unit Tests](#unit-tests)
- [Contributing](#contributing)
- [Support](#support)
- [License](#license)

## Introduction
The BMI Calculator is a graphical application built using Python and Tkinter. It allows users to calculate their Body Mass Index (BMI) based on their height and weight, with options for different units of measurement. The application also includes functionality to save the calculated results along with the user's name.

## Features
- Input fields for height and weight.
- Dropdown menus for selecting height and weight units.
- Calculate BMI and categorize it as Underweight, Normal weight, Overweight, or Obese.
- Save the BMI results along with the user's name to a text file.
- A graphical interface with a light background color for better visibility.
- Unit tests to ensure the accuracy of BMI calculations and unit conversions.

## Installation
To run the BMI Calculator on your local machine, follow these steps:

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/yourusername/bmi-calculator.git
    cd bmi-calculator
    ```

2. **Set Up a Virtual Environment** (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install Required Packages**:
    ```sh
    pip install tkinter
    ```

4. **Run the Application**:
    ```sh
    python bmi_calculator.py
    ```

5. **Run Unit Tests**:
    ```sh
    python -m unittest test_bmi_calculator.py
    ```

## Usage
1. Open the application.
2. Enter your height and weight in the respective fields.
3. Select the appropriate units from the dropdown menus.
4. Click the "Calculate BMI" button to see your BMI and its category.
5. To save the results, click the "Save Results" button and enter your name when prompted.

## Code Explanation

### Main Application
The main application code is in `bmi_calculator.py`:

```python
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

```
## Unit Tests
The unit test code is in `test_bmi_calculator.py`:
```python
import unittest
from bmi_calculator import calculate_bmi_logic, convert_units

class TestBMICalculator(unittest.TestCase):

    def test_underweight(self):
        bmi, category, _ = calculate_bmi_logic(1.75, 50)
        self.assertAlmostEqual(bmi, 16.33, places=2)
        self.assertEqual(category, "Underweight")

    def test_normal_weight(self):
        bmi, category, _ = calculate_bmi_logic(1.75, 68)
        self.assertAlmostEqual(bmi, 22.2, places=1)
        self.assertEqual(category, "Normal weight")

    def test_overweight(self):
        bmi, category, _ = calculate_bmi_logic(1.75, 80)
        self.assertAlmostEqual(bmi, 26.12, places=2)
        self.assertEqual(category, "Overweight")

    def test_obese(self):
        bmi, category, _ = calculate_bmi_logic(1.75, 95)
        self.assertAlmostEqual(bmi, 31.02, places=2)
        self.assertEqual(category, "Obese")

    def test_invalid_height(self):
        with self.assertRaises(ValueError):
            calculate_bmi_logic(0, 50)

    def test_invalid_weight(self):
        with self.assertRaises(ValueError):
            calculate_bmi_logic(1.75, 0)

    def test_convert_units_cm(self):
        height, weight = convert_units(175, 150, "cm", "kg")
        self.assertAlmostEqual(height, 1.75)
        self.assertAlmostEqual(weight, 150)

    def test_convert_units_feet(self):
        height, weight = convert_units(5.74, 150, "feet", "kg")
        self.assertAlmostEqual(height, 1.75, places=2)
        self.assertAlmostEqual(weight, 150)

    def test_convert_units_pounds(self):
        height, weight = convert_units(1.75, 330.69, "m", "pounds")
        self.assertAlmostEqual(height, 1.75)
        self.assertAlmostEqual(weight, 150, places=2)

if __name__ == "__main__":
    unittest.main()
```
## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## Support

**Interested in supporting me? [Patreon](patreon.com/msaeed)**

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). Feel free to use, modify, and distribute the code as per the terms of the license.

