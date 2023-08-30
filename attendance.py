import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def submit():
    roll_number = roll_number_entry.get()
    name = name_entry.get()
    division = division_var.get()

    # You can add your logic here to process the entered data, e.g., store it in a database
    # For now, let's just display the entered data in a messagebox
    message = f"Roll Number: {roll_number}\nName: {name}\nDivision: {division}"
    messagebox.showinfo("Student Details", message)

def generate_report():
    roll_number = roll_number_entry.get()
    name = name_entry.get()
    division = division_var.get()

    # Generate a PDF report
    pdf_filename = f"report_{roll_number}.pdf"
    c = canvas.Canvas(pdf_filename, pagesize=letter)
    c.drawString(100, 750, "Student Details")
    c.drawString(100, 700, f"Roll Number: {roll_number}")
    c.drawString(100, 680, f"Name: {name}")
    c.drawString(100, 660, f"Division: {division}")
    c.save()

    messagebox.showinfo("Report Generated", f"Report generated as '{pdf_filename}'")

# Create the main application window
root = tk.Tk()
root.title("Student Information")

# Set the window size (width x height)
window_width = 600
window_height = 350
root.geometry(f"{window_width}x{window_height}")

# Create and place widgets
roll_number_label = tk.Label(root, text="Roll Number:")
roll_number_label.pack()

roll_number_entry = tk.Entry(root)
roll_number_entry.pack()

name_label = tk.Label(root, text="Name:")
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

division_label = tk.Label(root, text="Division:")
division_label.pack()

# Create a variable to store the selected division
division_var = tk.StringVar(root)
division_var.set("A")  # Set the default value

# Create the Combobox with division options
division_menu = ttk.Combobox(root, textvariable=division_var, values=["A", "B"], state="readonly")
division_menu.pack()

submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack(pady=10)  # Add some padding below the button

generate_report_button = tk.Button(root, text="Generate Report", command=generate_report)
generate_report_button.pack()  # Place the Generate Report button below the Submit button

root.mainloop()
