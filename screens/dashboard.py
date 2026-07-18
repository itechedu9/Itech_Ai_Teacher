import customtkinter as ctk

# ----------------------------
# App Settings
# ----------------------------
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()

app.title("ITECH AI Teacher Enterprise")

app.geometry("1400x800")

# ----------------------------
# Left Sidebar
# ----------------------------

sidebar = ctk.CTkFrame(app, width=250)

sidebar.pack(side="left", fill="y")

title = ctk.CTkLabel(
    sidebar,
    text="ITECH AI\nTeacher",
    font=("Arial",28,"bold")
)

title.pack(pady=30)

menus = [
    "🏠 Dashboard",
    "👨‍🎓 Students",
    "👨‍🏫 Teachers",
    "🤖 AI Teacher",
    "💼 Job Preparation",
    "📚 Courses",
    "📝 Exams",
    "📊 Reports",
    "⚙ Settings",
    "🚪 Logout"
]

for item in menus:

    btn = ctk.CTkButton(
        sidebar,
        text=item,
        width=200,
        height=40
    )

    btn.pack(pady=6)

# ----------------------------
# Main Area
# ----------------------------

main = ctk.CTkFrame(app)

main.pack(side="right", expand=True, fill="both", padx=10, pady=10)

heading = ctk.CTkLabel(
    main,
    text="Welcome to ITECH AI Teacher",
    font=("Arial",30,"bold")
)

heading.pack(pady=40)

info = ctk.CTkLabel(
    main,
    text="AI Powered Learning Platform",
    font=("Arial",18)
)

info.pack()

app.mainloop()
