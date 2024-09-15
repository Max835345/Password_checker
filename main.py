import tkinter as tk
from tkinter import messagebox
import hashlib

hashed_password = hashlib.md5()
hashed_password.update(b"super_secret_password")
password = hashed_password.hexdigest()


def check_password():
    entered_password = password_entry.get()
    entered_password_hash = hashlib.md5(entered_password.encode()).hexdigest()
    if entered_password_hash == password:
        messagebox.showinfo("Result", "Password is correct!")
    else:
        messagebox.showwarning("Result", "Password is incorrect!")


root = tk.Tk()
root.title("Password Checker")

tk.Label(root, text="Enter Password:").pack(pady=10)
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

check_button = tk.Button(root, text="Check Password", command=check_password)
check_button.pack(pady=20)

root.mainloop()
