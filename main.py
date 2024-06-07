import tkinter as tk
from tkinter import ttk, messagebox
from connect_db import create_connection
from create_table import create_family_details_table
from insert_data import insert_family_data
from styles import configure_styles, create_treeview

class FamilyApp:
    def __init__(self, master):
        self.master = master
        master.title("Family Details App")

        # Configure styles
        configure_styles()

        # Welcome message
        self.welcome_label = ttk.Label(master, text="Welcome to the Family Details App!", style="TLabel")
        self.welcome_label.pack(pady=20)

        self.connection = create_connection()
        create_family_details_table(self.connection)

        # Create and style buttons
        self.add_data_button = ttk.Button(master, text="Add Data", command=self.ask_for_data, style="Accent.TButton")
        self.add_data_button.pack(pady=10)

        self.delete_data_button = ttk.Button(master, text="Delete Data", command=self.ask_for_delete, style="Accent.TButton")
        self.delete_data_button.pack(pady=10)

        self.quit_button = ttk.Button(master, text="Quit", command=master.quit, style="Danger.TButton")
        self.quit_button.pack(pady=10)

        # Create a themed treeview for displaying data
        self.tree = create_treeview(master)
        self.tree.pack(padx=10, pady=10)

        # Display existing data
        self.display_data()

    def display_data(self):
        # Delete existing data in treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        cursor = self.connection.cursor()
        select_query = "SELECT * FROM family_details"
        cursor.execute(select_query)
        result = cursor.fetchall()

        if result:
            for row in result:
                self.tree.insert("", "end", values=row)

    def ask_for_data(self):
        # Create a new window for data input
        data_window = tk.Toplevel(self.master)
        data_window.title("Add New Data")
        data_window.geometry("400x600")

        # Entry widgets for user input
        fields = ["Name", "Last Name", "Age", "Occupation", "Location", "Relation"]
        entry_widgets = {}

        for idx, field in enumerate(fields):
            label = ttk.Label(data_window, text=f"{field}:", style="TLabel")
            label.grid(row=idx, column=0, padx=10, pady=5, sticky="e")
            entry_widgets[field] = ttk.Entry(data_window, font=("Helvetica", 12))
            entry_widgets[field].grid(row=idx, column=1, padx=10, pady=5)

        # Button to submit data
        submit_button = ttk.Button(data_window, text="Submit", command=lambda: self.submit_data(
            {field.lower().replace(" ", "_"): entry_widgets[field].get() for field in fields}, data_window),
                                   style="Accent.TButton")
        submit_button.grid(row=len(fields), column=0, columnspan=2, pady=10)

        # Add a little animation
        for i in range(1, 100, 2):
            data_window.update()
            data_window.geometry(f"400x{600 - i}")
            data_window.update_idletasks()

    def submit_data(self, data, data_window):
        # Insert new data into the table
        insert_family_data(self.connection, **data)

        messagebox.showinfo("Success", "Data added successfully!")

        # Update the displayed data
        self.display_data()

        # Close the data input window
        data_window.destroy()

    def ask_for_delete(self):
        # Create a new window for data deletion
        delete_window = tk.Toplevel(self.master)
        delete_window.title("Delete Data")
        delete_window.geometry("400x200")

        # Entry widget for user input
        delete_id_label = ttk.Label(delete_window, text="Enter ID to delete:", style="TLabel")
        delete_id_label.pack()
        delete_id_entry = ttk.Entry(delete_window)
        delete_id_entry.pack()

        # Button to delete data
        delete_button = ttk.Button(delete_window, text="Delete", command=lambda: self.delete_data(delete_id_entry.get(), delete_window),
                                   style="Accent.TButton")
        delete_button.pack()

    def delete_data(self, delete_id, delete_window):
        # Delete data from the table
        try:
            delete_id = int(delete_id)
            cursor = self.connection.cursor()
            delete_query = f"DELETE FROM family_details WHERE id = {delete_id}"
            cursor.execute(delete_query)
            self.connection.commit()

            messagebox.showinfo("Success", f"Data with ID {delete_id} deleted successfully!")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid ID for deletion.")

        # Update the displayed data
        self.display_data()

        # Close the delete data window
        delete_window.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = FamilyApp(root)
    root.mainloop()
