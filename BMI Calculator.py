import tkinter as tk
from tkinter import messagebox, filedialog

def calculate_bmi():
    try:
        # Get user input
        height = float(height_entry.get())
        weight = float(weight_entry.get())

        # Calculate BMI
        bmi = weight / (height ** 2)

        # Determine BMI category
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        # Display result
        result = f"BMI: {bmi:.2f}\nCategory: {category}"
        messagebox.showinfo("BMI Result", result)

        # Save result to file
        save_result(result)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values for height and weight.")

def save_result(result):
    # Ask user to choose a file location to save the result
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])

    # Save result to the chosen file
    if file_path:  # Check if a file path is selected
        with open(file_path, 'w') as file:
            file.write(result)

        messagebox.showinfo("Save Result", "Result saved successfully!")

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y}")

# Create main window
window = tk.Tk()
window.title("BMI Calculator")

# Window size
window_width = 300
window_height = 300
window.geometry(f"{window_width}x{window_height}")

# Center the window on the screen
center_window(window, window_width, window_height)

# Create labels and entry widgets for user input
name_label = tk.Label(window, text="First Name:")
name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1, padx=10, pady=5)

surname_label = tk.Label(window, text="Last Name:")
surname_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
surname_entry = tk.Entry(window)
surname_entry.grid(row=1, column=1, padx=10, pady=5)

age_label = tk.Label(window, text="Age:")
age_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
age_entry = tk.Entry(window)
age_entry.grid(row=2, column=1, padx=10, pady=5)

height_label = tk.Label(window, text="Height (m):")
height_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
height_entry = tk.Entry(window)
height_entry.grid(row=3, column=1, padx=10, pady=5)

weight_label = tk.Label(window, text="Weight (kg):")
weight_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
weight_entry = tk.Entry(window)
weight_entry.grid(row=4, column=1, padx=10, pady=5)

# BMI calculation button
calculate_button = tk.Button(window, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=5, column=0, columnspan=2, pady=10)

# Start the main loop
window.mainloop()
