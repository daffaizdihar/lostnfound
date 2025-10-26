import tkinter as tk
from tkinter import messagebox

def add_item():
    name = entry_name.get()
    desc = entry_desc.get()
    if name == "" or desc == "":
        messagebox.showwarning("Warning", "Please fill in all fields!")
        return
    listbox.insert(tk.END, f"{name} — {desc}")
    entry_name.delete(0, tk.END)
    entry_desc.delete(0, tk.END)

def delete_item():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
    except IndexError:
        messagebox.showinfo("Info", "Please select an item to delete!")

# Window setup
root = tk.Tk()
root.title("Lost & Found App")
root.geometry("400x400")

# Widgets
tk.Label(root, text="Item Name:").pack(pady=5)
entry_name = tk.Entry(root, width=40)
entry_name.pack()

tk.Label(root, text="Description:").pack(pady=5)
entry_desc = tk.Entry(root, width=40)
entry_desc.pack()

tk.Button(root, text="Add Item", command=add_item).pack(pady=5)
tk.Button(root, text="Delete Selected", command=delete_item).pack(pady=5)

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

root.mainloop()
