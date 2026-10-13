import secrets
import string
import tkinter as tk
from tkinter import messagebox

# Available password characters
symbols = string.ascii_letters + string.digits + "!@#$%&*()_"

# Generate password
def generate_password():
    length = length_entry.get()

    if not length.isdigit() or int(length) <= 0:
        messagebox.showerror(
            "Invalid input",
            "Please enter a positive whole number."
        )
        return

    length = int(length)
    password = ''.join(
        secrets.choice(symbols) for _ in range(length)
    )

    password_entry.config(state="normal")
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    password_entry.config(state="readonly")


# Copy password to clipboard
def copy_password():
    password = password_entry.get()

    if password:
        window.clipboard_clear()
        window.clipboard_append(password)
        messagebox.showinfo(
            "Copied",
            "Password copied to clipboard!"
        )


# Create the main window
window = tk.Tk()
window.title("Password Generator")
window.geometry("400x250")
window.resizable(False, False)

# Title
title_label = tk.Label(
    window,
    text="Password Generator",
    font=("Arial", 18, "bold")
)
title_label.pack(pady=15)

# Password length input
length_label = tk.Label(
    window,
    text="Enter password length:"
)
length_label.pack()

length_entry = tk.Entry(window, justify="center")
length_entry.pack(pady=5)
length_entry.insert(0, "16")

# Generate button
generate_button = tk.Button(
    window,
    text="Generate Password",
    command=generate_password
)
generate_button.pack(pady=8)

# Password output field
password_entry = tk.Entry(
    window,
    width=38,
    state="readonly",
    justify="center"
)
password_entry.pack(pady=5)

# Copy button
copy_button = tk.Button(
    window,
    text="Copy Password",
    command=copy_password
)
copy_button.pack(pady=5)

# Start the GUI event loop
window.mainloop()
