import customtkinter as ctk

def create_graph_panel(parent):

    frame = ctk.CTkFrame(parent, corner_radius=15)

    frame.pack(fill="x", padx=20, pady=10)

    title = ctk.CTkLabel(
        frame,
        text="📈 Analytics Dashboard",
        font=("Segoe UI",22,"bold")
    )

    title.pack(anchor="w", padx=20, pady=15)

    chart = ctk.CTkTextbox(frame, height=180)

    chart.insert("1.0",
"""
Admissions Graph

███████████

Attendance Graph

██████████████

Revenue Graph

██████████

AI Usage

████████████████
""")

    chart.configure(state="disabled")

    chart.pack(fill="both", padx=20, pady=10)

    return frame
