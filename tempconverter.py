import tkinter as tk
from tkinter import ttk, messagebox

def convert_temperature():
    try:
        temp = float(entry_temp.get())  # Validate input
        conversion_type = conversion_var.get()

        conversions = {
            "Celsius to Fahrenheit": ((temp * 9/5) + 32, "°C", "°F"),
            "Celsius to Kelvin": (temp + 273.15, "°C", "K"),
            "Fahrenheit to Celsius": ((temp - 32) * 5/9, "°F", "°C"),
            "Fahrenheit to Kelvin": ((temp - 32) * 5/9 + 273.15, "°F", "K"),
            "Kelvin to Celsius": (temp - 273.15, "K", "°C"),
            "Kelvin to Fahrenheit": ((temp - 273.15) * 9/5 + 32, "K", "°F")
        }

        if conversion_type in conversions:
            result, original_unit, converted_unit = conversions[conversion_type]
            label_result.config(
                text=f"Result: {temp:.2f} {original_unit} → {result:.2f} {converted_unit}",
                foreground="green",
                font=("Arial", 14, "bold")
            )
        else:
            messagebox.showerror("Error", "Invalid selection. Please choose a valid conversion type.")

    except ValueError:
        messagebox.showerror("Error", "Invalid temperature input! Please enter a valid number.")

# Create GUI window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x300")
root.configure(bg="#ddeeff")  # Set background color

# Styling
style = ttk.Style()
style.theme_use("clam")  # Ensure theme compatibility
style.configure("TButton", font=("Arial", 12), padding=6)
style.configure("TLabel", font=("Arial", 12), background="#ddeeff")

# Temperature input
ttk.Label(root, text="Enter Temperature:", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_temp = ttk.Entry(root, width=18, font=("Arial", 12))
entry_temp.grid(row=0, column=1, padx=10, pady=10)

# Dropdown for conversion selection
ttk.Label(root, text="Conversion Type:", font=("Arial", 12, "bold")).grid(row=1, column=0, padx=10, pady=10, sticky="w")
conversion_var = tk.StringVar()
conversion_var.set("Celsius to Fahrenheit")  # Default selection
options = ["Celsius to Fahrenheit", "Celsius to Kelvin",
           "Fahrenheit to Celsius", "Fahrenheit to Kelvin",
           "Kelvin to Celsius", "Kelvin to Fahrenheit"]
dropdown = ttk.Combobox(root, textvariable=conversion_var, values=options, state="readonly", font=("Arial", 12))
dropdown.grid(row=1, column=1, padx=10, pady=10)

# Convert button
convert_button = ttk.Button(root, text="Convert", command=convert_temperature, style="TButton")
convert_button.grid(row=2, column=0, columnspan=2, pady=15)

# Result display
label_result = ttk.Label(root, text="Result: ", font=("Arial", 16, "bold"), foreground="blue", background="#ddeeff")
label_result.grid(row=3, column=0, columnspan=2, pady=20)

# Run the GUI loop
root.mainloop()
