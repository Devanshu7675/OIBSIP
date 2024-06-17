import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Function to calculate BMI
def calculate_bmi():
    try:
        height = float(entry_height.get())
        weight = float(entry_weight.get())
        name = entry_name.get()

        if height <= 0 or weight <= 0:
            messagebox.showerror("Input Error", "Height and weight must be positive numbers.")
            return

        bmi = ((weight/height)/height)*10000

        if bmi < 18.5:
            result = "Underweight"
        elif 18.5 <= bmi < 24.9:
            result = "Normal weight"
        elif 25 <= bmi < 29.9:
            result = "Overweight"
        else:
            result = "Obesity"

        label_result['text'] = f"BMI: {bmi:.2f}\nResult: {result}"
        save_to_database(name, height, weight,format(bmi,".2f"))
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# Function to save data to the MySQL database
def save_to_database(username, height, weight, result):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Up20au7675@',
            database='bmi'
        )
        cursor = connection.cursor()
        sql = "INSERT INTO calculator (username, height, weight, result) VALUES (%s, %s, %s, %s)"
        values = (username, height, weight, result)
        cursor.execute(sql, values)
        connection.commit()
        cursor.close()
        connection.close()
        messagebox.showinfo("Success", "Data saved successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

# Create the GUI application
app = tk.Tk()
app.title("BMI Calculator")

# Name input
tk.Label(app, text="Name:").grid(row=0, column=0)
entry_name = tk.Entry(app)
entry_name.grid(row=0, column=1)

# Height input
tk.Label(app, text="Height (cm):").grid(row=1, column=0)
entry_height = tk.Entry(app)
entry_height.grid(row=1, column=1)

# Weight input
tk.Label(app, text="Weight (kg):").grid(row=2, column=0)
entry_weight = tk.Entry(app)
entry_weight.grid(row=2, column=1)

# Calculate button
btn_calculate = tk.Button(app, text="Calculate BMI", command=calculate_bmi)
btn_calculate.grid(row=3, columnspan=2)

# Result label
label_result = tk.Label(app, text="")
label_result.grid(row=4, columnspan=2)

# Run the application
app.mainloop()