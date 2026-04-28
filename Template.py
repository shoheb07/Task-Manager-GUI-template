import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Task Manager")
root.geometry("400x500")

tasks = []

# Functions
def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
        tasks.pop(selected)
    except:
        messagebox.showwarning("Warning", "Please select a task")

def mark_completed():
    try:
        selected = listbox.curselection()[0]
        task = listbox.get(selected)
        listbox.delete(selected)
        listbox.insert(tk.END, f"✔ {task}")
    except:
        messagebox.showwarning("Warning", "Please select a task")

# UI Elements
frame = tk.Frame(root)
frame.pack(pady=10)

listbox = tk.Listbox(frame, width=40, height=15)
listbox.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Task", command=add_task)
add_btn.pack(pady=5)

delete_btn = tk.Button(root, text="Delete Task", command=delete_task)
delete_btn.pack(pady=5)

complete_btn = tk.Button(root, text="Mark Completed", command=mark_completed)
complete_btn.pack(pady=5)

# Run app
root.mainloop()
