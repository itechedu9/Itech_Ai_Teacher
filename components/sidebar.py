from screens.admission import open_admission
import customtkinter as ctk

def create_sidebar(parent):

    sidebar = ctk.CTkFrame(
        parent,
        width=250,
        corner_radius=0
    )
    sidebar.pack(side="left", fill="y")
    sidebar.pack_propagate(False)

    # Logo
    logo = ctk.CTkLabel(
        sidebar,
        text="🤖\nITECH AI\nTeacher",
        font=("Segoe UI", 24, "bold"),
        justify="center"
    )
    logo.pack(pady=(20, 30))

    # Menu List
    menus = [
        "🏠 Dashboard",
        "👨‍🎓 Students",
        "👨‍🏫 Teachers",
        "🤖 AI Teacher",
        "💼 Job Preparation",
        "📚 Courses",
        "📝 Exams",
        "📊 Reports",
        "⚙️ Settings"
    ]

    # Menu Buttons
    for menu in menus:

        btn = ctk.CTkButton(
            sidebar,
            text=menu,
            width=220,
            height=45,
            corner_radius=10,
            anchor="w",
            font=("Segoe UI", 16)
        )

        btn.pack(pady=6, padx=15)

    # Bottom Section
    ctk.CTkLabel(
        sidebar,
        text="────────────",
        font=("Segoe UI", 14)
    ).pack(side="bottom", pady=(0, 10))

    ctk.CTkButton(
        sidebar,
        text="📝 Student Admission",
        height=45,
        command=open_admission
    ).pack(fill="x", padx=15, pady=5)


    logout = ctk.CTkButton(
        sidebar,
        text="🚪 Logout",
        width=220,
        height=45,
        fg_color="#C0392B",
        hover_color="#A93226"
    )

    logout.pack(side="bottom", pady=20)

    version = ctk.CTkLabel(
        sidebar,
        text="Version 1.0 Enterprise",
        font=("Segoe UI", 12)
    )

    version.pack(side="bottom", pady=5)

    return sidebar
