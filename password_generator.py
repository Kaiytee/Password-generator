import tkinter as tk
from tkinter import messagebox
import random
import string
from PIL import Image, ImageTk

def generate_password():
    length = int(length_var.get())
    
    if length < 6:
        messagebox.showerror("Error", "Password length should be at least 6 characters")
        return
    
    while True:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        if (any(c.islower() for c in password) and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in string.punctuation for c in password)):
            break
    
    password_var.set(password)
    copy_button.place(relx=0.9, rely=0.80, anchor="e")  # Show copy button

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    root.update()

# GUI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("450x250")
root.resizable(False, False)  # Fix the window size

# Load background image
bg_image = Image.open("background.jpg")
bg_image = bg_image.resize((450, 250))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Ensure it fills the UI

# Input for password length
length_label = tk.Label(root, text="Enter Password Length", bg="lightgray")
length_label.place(relx=0.9, rely=0.2, anchor="e")

length_var = tk.StringVar(value="8")
length_entry = tk.Entry(root, textvariable=length_var, width=20)
length_entry.place(relx=0.9, rely=0.30, anchor="e")

# Button to generate password
generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg="green", fg="white", width=16)
generate_button.place(relx=0.9, rely=0.50, anchor="e")

# Display generated password
password_var = tk.StringVar()
password_entry = tk.Entry(root, textvariable=password_var, state="readonly", width=20)
password_entry.place(relx=0.9, rely=0.60, anchor="e")

# Copy button (initially hidden)
copy_button = tk.Button(root, text="Copy Password", command=copy_to_clipboard, bg="lightgray", fg="black")
copy_button.place_forget()


# Run the GUI
root.mainloop()