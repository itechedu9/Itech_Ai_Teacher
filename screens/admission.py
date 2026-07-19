import customtkinter as ctk

def open_admission():

    win = ctk.CTkToplevel()

    win.title("Student Admission")

    win.geometry("1100x700")

    title = ctk.CTkLabel(
        win,
        text="Student Admission Form",
        font=("Arial", 28, "bold")
    )

    title.pack(pady=20)

    frame = ctk.CTkFrame(win)
    frame.pack(fill="both", expand=True, padx=20, pady=20)

    ctk.CTkLabel(
        frame,
        text="Student Name"
    ).grid(row=0, column=0, padx=10, pady=10)

    ctk.CTkEntry(
        frame,
        width=250
    ).grid(row=0, column=1)
