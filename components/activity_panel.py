import customtkinter as ctk

def create_activity(parent):

    frame = ctk.CTkFrame(parent, corner_radius=15)

    frame.pack(side="left", fill="both", expand=True,
               padx=20, pady=10)

    title = ctk.CTkLabel(
        frame,
        text="📝 Recent Activity",
        font=("Segoe UI",20,"bold")
    )

    title.pack(anchor="w", padx=15, pady=15)

    box = ctk.CTkTextbox(frame)

    box.insert("1.0",
"""
✔ Student Registration

✔ New Course Added

✔ AI Teacher Started

✔ Exam Scheduled

✔ Payment Received
""")

    box.configure(state="disabled")

    box.pack(fill="both", expand=True,
             padx=15, pady=15)

    return frame
