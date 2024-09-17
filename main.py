import tkinter as tk
from tkinter import messagebox
import hashlib
import uuid

salt = uuid.uuid4().hex
password = "123"
hashed_password = hashlib.md5(salt.encode() + password.encode()).hexdigest() + ':' + salt
print(hashed_password)


def check_password():
    entered_password = password_entry.get()
    entered_password_hash = hashlib.md5(salt.encode() + entered_password.encode()).hexdigest() + ':' + salt
    print(entered_password_hash)
    if entered_password_hash == hashed_password:
        messagebox.showinfo("Результат", "Пароль верен")
    else:
        messagebox.showwarning("Результат", "Пароль не верен")


root = tk.Tk()
root.title("Password Checker")

tk.Label(root, text="Enter Password:").pack(pady=10)
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

check_button = tk.Button(root, text="Check Password", command=check_password)
check_button.pack(pady=20)

root.mainloop()
