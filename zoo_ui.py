import tkinter as tk
from tkinter import ttk, messagebox
import requests
import yaml
import os

# --- Backend communication ---

BACKEND_URL = "http://localhost:8080"

def fetch_pets():
    try:
        res = requests.get(f"{BACKEND_URL}/status")
        res.raise_for_status()
        return res.json()
    except requests.exceptions.RequestException:
        return None

def apply_zoo():
    if not os.path.exists("pets/my_zoo.yaml"):
        messagebox.showerror("Error", "Zoo config not found at 'pets/my_zoo.yaml'")
        return

    try:
        with open("pets/my_zoo.yaml") as f:
            data = yaml.safe_load(f)
        res = requests.post(f"{BACKEND_URL}/apply", json=data)
        res.raise_for_status()
        messagebox.showinfo("Zoo Created", "The zoo has been successfully created!")
        update_ui()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to apply zoo:\n{e}")

def destroy_zoo():
    try:
        res = requests.post(f"{BACKEND_URL}/destroy")
        res.raise_for_status()
        messagebox.showinfo("Zoo Destroyed", "The zoo has been destroyed.")
        update_ui()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to destroy zoo:\n{e}")

def feed_pets():
    try:
        res = requests.post(f"{BACKEND_URL}/feed")
        res.raise_for_status()
        messagebox.showinfo("Fed the Zoo", "🍖 All pets have been fed!")
        update_ui()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to feed pets:\n{e}")


# --- UI Update Logic ---

def update_ui():
    for widget in frame.winfo_children():
        widget.destroy()
    
    pets = fetch_pets()
    if pets is None:
        label = tk.Label(frame, text="❌ No pets in the zoo.", font=("Helvetica", 12), fg="black")
        label.pack(pady=10)
        return

    if not pets:
        label = tk.Label(frame, text="No pets found in the zoo. 🐾", font=("Helvetica", 12))
        label.pack(pady=10)
        return

    for pet in pets:
        pet_info = f"{pet['name']} the {pet['type']} 🐾 | Hunger: {pet['hunger']} | Lifespan: {pet['lifespan']}"
        label = tk.Label(frame, text=pet_info, font=("Helvetica", 12), anchor="w", justify="left")
        label.pack(fill='x', padx=10, pady=2)

# --- UI Setup ---

root = tk.Tk()
root.title("🐾 Zoo Control Panel")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(fill='both', expand=True)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

apply_btn = ttk.Button(button_frame, text="🪄 Create Zoo", command=apply_zoo)
apply_btn.grid(row=0, column=0, padx=5)

feed_btn = ttk.Button(button_frame, text="🍗 Feed All Pets", command=feed_pets)
feed_btn.grid(row=0, column=3, padx=5)

destroy_btn = ttk.Button(button_frame, text="💀 Destroy Zoo", command=destroy_zoo)
destroy_btn.grid(row=0, column=1, padx=5)

refresh_btn = ttk.Button(button_frame, text="🔄 Refresh", command=update_ui)
refresh_btn.grid(row=0, column=2, padx=5)

update_ui()
root.mainloop()
