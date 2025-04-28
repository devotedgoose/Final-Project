# Author: Emmanuel Asiedu
# Date: 04/12/2025
# Assignment: Module 08 Programming Assignment
# Description : This program implements a GUI application for managing repair tickets in a small computer repair shop.
"""
G-TECH Repair Ticket System
-----------------------------
Main Purpose:
A GUI application for managing repair tickets in a small computer repair shop.
Developed using Python's Tkinter library with a modular and secure approach.
"""

import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

# Store tickets in a list of dictionaries
tickets = []

# Function: Exit the application
def exit_app():
    root.quit()

# Function: Validate and create a new ticket
def submit_ticket():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    device = device_entry.get().strip()
    problem = problem_entry.get("1.0", tk.END).strip()
    serial = serial_entry.get().strip()
    date_created = datetime.now().strftime("%m/%d/%Y")

    # Input validation
    if not name or not phone.isdigit() or len(phone) != 10 or not device or not problem or not serial:
        messagebox.showerror("Input Error", "Please ensure all fields are valid.")
        return

    ticket_id = len(tickets) + 1
    ticket = {
        "ID": ticket_id,
        "Name": name,
        "Phone": phone,
        "Device": device,
        "Serial": serial,
        "Problem": problem,
        "Date": date_created,
        "Status": "Open"
    }
    tickets.append(ticket)
    messagebox.showinfo("Success", f"Ticket #{ticket_id} created successfully.")
    clear_fields()
    update_ticket_list()

# Function: Clear input fields
def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    device_entry.delete(0, tk.END)
    serial_entry.delete(0, tk.END)
    problem_entry.delete("1.0", tk.END)

# Function: Update ticket TreeView
def update_ticket_list():
    for row in ticket_tree.get_children():
        ticket_tree.delete(row)
    for t in tickets:
        ticket_tree.insert('', 'end', values=(t['ID'], t['Name'], t['Device'], t['Status']))

# Function: Open the Search Window
def open_search_window():
    search_win = tk.Toplevel(root)
    search_win.title("Search Ticket")
    search_win.geometry("400x250")

    tk.Label(search_win, text="Enter Ticket ID or Name:").pack(pady=5)
    search_entry = tk.Entry(search_win)
    search_entry.pack(pady=5)

    def perform_search():
        term = search_entry.get().strip().lower()
        results = [t for t in tickets if term == str(t['ID']).lower() or term in t['Name'].lower()]
        if results:
            ticket = results[0]
            msg = f"Ticket #{ticket['ID']} | Name: {ticket['Name']} | Device: {ticket['Device']} | Status: {ticket['Status']} | Description: {ticket['Problem']}"
            messagebox.showinfo("Ticket Found", msg)
        else:
            messagebox.showinfo("Not Found", "No matching ticket found.")

    tk.Button(search_win, text="Search", command=perform_search).pack(pady=10)

# ------------------ GUI Layout -------------------
root = tk.Tk()
root.title("G-TECH Repair Ticket System")
root.geometry("1020x500")

# Labels
tk.Label(root, text="Customer Name:").grid(row=0, column=0, sticky='e')
tk.Label(root, text="Phone Number:").grid(row=1, column=0, sticky='e')
tk.Label(root, text="Device Type:").grid(row=2, column=0, sticky='e')
tk.Label(root, text="Serial Number:").grid(row=3, column=0, sticky='e')
tk.Label(root, text="Problem Description:").grid(row=4, column=0, sticky='ne')

# Entry fields
name_entry = tk.Entry(root)
phone_entry = tk.Entry(root)
device_entry = tk.Entry(root)
serial_entry = tk.Entry(root)
problem_entry = tk.Text(root, height=4, width=30)

name_entry.grid(row=0, column=1)
phone_entry.grid(row=1, column=1)
device_entry.grid(row=2, column=1)
serial_entry.grid(row=3, column=1)
problem_entry.grid(row=4, column=1)

# Buttons
tk.Button(root, text="Create Ticket", command=submit_ticket).grid(row=5, column=0, pady=10)
tk.Button(root, text="Search Ticket", command=open_search_window).grid(row=5, column=1, pady=10)
tk.Button(root, text="Exit", command=exit_app).grid(row=6, column=0, columnspan=2)

# Ticket list
ticket_tree = ttk.Treeview(root, columns=("ID", "Name", "Device", "Status", "Description"), show='headings')
ticket_tree.heading("ID", text="ID")
ticket_tree.heading("Name", text="Name")
ticket_tree.heading("Device", text="Device")
ticket_tree.heading("Status", text="Status")
ticket_tree.heading("Description", text="Description")
ticket_tree.grid(row=7, column=0, columnspan=2, pady=20)





root.mainloop()
