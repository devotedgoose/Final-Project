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
from tkinter import messagebox
from tkinter import PhotoImage


# Storage for tickets
tickets = []  # Initially empty

# ====== Module: Main Window (Home) ======
# This function sets up and displays the main window, including company branding and navigation to the form.
def show_main_window():
    home = tk.Tk()
    home.title("G-TECH Repair Ticket Service")
    home.geometry("500x300")
    home.resizable(False, False)

    # Load images
    try:
        logo_img = tk.PhotoImage(file="logo.png")  # Company logo
        icon_img = tk.PhotoImage(file="repair_icon.png")  # Repair icon
    except Exception as e:
        messagebox.showerror("Image Load Error", f"Could not load image: {e}")
        logo_img = icon_img = None

    # Display logo image with alt text
    if logo_img:
        logo_label = tk.Label(home, image=logo_img, text="G-TECH Logo", compound="top")
        logo_label.image = logo_img  # Keep a reference
        logo_label.pack(pady=10)

    # Heading label
    heading = tk.Label(home, text="Welcome to G-TECH!", font=("Helvetica", 16, "bold"))
    heading.pack(pady=5)

    # Description label
    desc = tk.Label(home, text="Click below to submit or search a repair ticket.", font=("Helvetica", 12))
    desc.pack(pady=5)

    # Button to go to form window
    next_btn = tk.Button(home, text="Submit Repair Ticket", command=lambda: [home.destroy(), show_form_window()])
    next_btn.pack(pady=10)

    # Button to search for tickets
    search_btn = tk.Button(home, text="Search Ticket", command=lambda: [home.destroy(), show_search_window()])
    search_btn.pack(pady=10)

    # Exit Button
    exit_btn = tk.Button(home, text="Exit", command=home.destroy)
    exit_btn.pack(pady=5)

    home.mainloop()

# ====== Module: Search Window ======
# This function sets up the search window where users can search for existing tickets.
def show_search_window():
    search_window = tk.Tk()
    search_window.title("Search Ticket")
    search_window.geometry("400x200")

    label = tk.Label(search_window, text="Enter Ticket ID or Name:")
    label.pack(pady=5)

    search_entry = tk.Entry(search_window)
    search_entry.pack(pady=5)

    def perform_search():
        term = search_entry.get().strip().lower()
        results = [t for t in tickets if term == str(t.get('ID', '')).lower() or term in t.get('Name', '').lower()]
        if results:
            ticket = results[0]
            msg = f"Ticket #{ticket['ID']} | Name: {ticket['Name']} | Device: {ticket['Device']} | Status: {ticket['Status']} | Description: {ticket['Description']}"
            messagebox.showinfo("Ticket Found", msg)
        else:
            messagebox.showwarning("Not Found", "No matching ticket found.")

    search_btn = tk.Button(search_window, text="Search", command=perform_search)
    search_btn.pack(pady=10)

    exit_btn = tk.Button(search_window, text="Back", command=lambda: [search_window.destroy(), show_main_window()])
    exit_btn.pack()

# ====== Module: Form Window ======
# This function sets up the form window where users can input repair ticket info.
def show_form_window():
    form = tk.Tk()
    form.title("Repair Ticket Form")
    form.geometry("500x350")
    form.resizable(False, False)

    # Labels
    tk.Label(form, text="Customer Name:", font=("Helvetica", 12)).grid(row=0, column=0, pady=10, padx=10, sticky="e")
    tk.Label(form, text="Device Type:", font=("Helvetica", 12)).grid(row=1, column=0, pady=10, padx=10, sticky="e")
    tk.Label(form, text="Phone Number:", font=("Helvetica", 12)).grid(row=2, column=0, pady=10, padx=10, sticky="e")
    tk.Label(form, text="Issue Description:", font=("Helvetica", 12)).grid(row=3, column=0, pady=10, padx=10, sticky="ne")
    

    # Input Fields
    name_var = tk.StringVar()
    device_var = tk.StringVar()
    phone_var = tk.StringVar()
    issue_text = tk.Text(form, height=5, width=30)

    name_entry = tk.Entry(form, textvariable=name_var)
    device_entry = tk.Entry(form, textvariable=device_var)
    phone_entry = tk.Entry(form, textvariable=phone_var)

    name_entry.grid(row=0, column=1, pady=10)
    device_entry.grid(row=1, column=1, pady=10)
    phone_entry.grid(row=2, column=1, pady=10)
    issue_text.grid(row=3, column=1, pady=10)

    # Submit Callback Function
    def submit_form():
        name = name_var.get().strip()
        device = device_var.get().strip()
        phone = phone_var.get().strip()
        issue = issue_text.get("1.0", "end").strip()

        # Input validation
        if not name or not device or not issue:
            messagebox.showwarning("Input Error", "All fields are required.")
            return

        if not name.replace(" ", "").isalpha():
            messagebox.showerror("Validation Error", "Name should only contain letters.")
            return

        # Simulate ticket submission
        ticket_id = len(tickets) + 1
        tickets.append({
            "ID": ticket_id,
            "Name": name,
            "Device": device,
            "Description": issue,
            "Status": "Open"
        })

        messagebox.showinfo("Success", f"Ticket #{ticket_id} submitted for {name}'s {device}.")
        form.destroy()
        show_main_window()

    # Submit Button
    submit_btn = tk.Button(form, text="Submit", command=submit_form)
    submit_btn.grid(row=4, column=1, pady=20)

    # Exit Button
    exit_btn = tk.Button(form, text="Exit", command=form.destroy)
    exit_btn.grid(row=5, column=1)

    form.mainloop()

# ====== Program Start ======
# Launch the main window when script runs
if __name__ == "__main__":
    show_main_window()
