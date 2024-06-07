from tkinter import ttk
from ttkthemes import ThemedStyle

def configure_styles():
    style = ThemedStyle()
    style.set_theme("plastik")

    style.configure("TLabel", font=("Helvetica", 12), padding=10)
    style.configure("TButton", font=("Helvetica", 12), padding=10)
    style.configure("Treeview", font=("Helvetica", 10))
    style.configure("TCombobox", font=("Helvetica", 12))

def create_treeview(master):
    tree = ttk.Treeview(master, columns=("ID", "Name", "Last Name", "Age", "Occupation", "Location", "Relation"),
                        show="headings", style="Treeview")
    tree.heading("ID", text="ID")
    tree.heading("Name", text="Name")
    tree.heading("Last Name", text="Last Name")
    tree.heading("Age", text="Age")
    tree.heading("Occupation", text="Occupation")
    tree.heading("Location", text="Location")
    tree.heading("Relation", text="Relation")
    return tree
