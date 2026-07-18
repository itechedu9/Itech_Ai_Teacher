import customtkinter as ctk

def show(parent):

    for widget in parent.winfo_children():
        widget.destroy()

    ctk.CTkLabel(
        parent,
        text="📚 Course Management",
        font=("Segoe UI",28,"bold")
    ).pack(pady=40)
