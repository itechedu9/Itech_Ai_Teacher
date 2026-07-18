import customtkinter as ctk


def create(parent):

    frame = ctk.CTkFrame(parent)

    title = ctk.CTkLabel(
        frame,
        text="Student Management",
        font=("Segoe UI", 28, "bold")
    )

    title.pack(pady=20)

    return frame
