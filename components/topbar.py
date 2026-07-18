import customtkinter as ctk
from datetime import datetime

def create_topbar(parent):

    topbar = ctk.CTkFrame(parent, height=70, corner_radius=10)
    topbar.pack(fill="x", padx=15, pady=15)

    # Dashboard Title
    title = ctk.CTkLabel(
        topbar,
        text="🏠 Dashboard",
        font=("Segoe UI", 24, "bold")
    )
    title.pack(side="left", padx=20)

    # Search Box
    search = ctk.CTkEntry(
        topbar,
        width=260,
        placeholder_text="🔍 Search..."
    )
    search.pack(side="left", padx=20)

    # Notification
    notification = ctk.CTkButton(
        topbar,
        text="🔔",
        width=45
    )
    notification.pack(side="right", padx=10)

    # User Profile
    profile = ctk.CTkButton(
        topbar,
        text="👤 Admin",
        width=120
    )
    profile.pack(side="right", padx=10)

    # Live Clock
    clock = ctk.CTkLabel(
        topbar,
        text="",
        font=("Segoe UI",16,"bold")
    )
    clock.pack(side="right", padx=20)

    def update_clock():
        now = datetime.now().strftime("%d-%m-%Y  %I:%M:%S %p")
        clock.configure(text=now)
        clock.after(1000, update_clock)

    update_clock()

    return topbar
