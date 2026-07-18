import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()

app.title("ITECH AI Teacher")

app.geometry("1100x700")

title = ctk.CTkLabel(
    app,
    text="ITECH AI Teacher",
    font=("Arial",32,"bold")
)

title.pack(pady=40)

subtitle = ctk.CTkLabel(
    app,
    text="AI Powered Learning Platform",
    font=("Arial",18)
)

subtitle.pack()

language = ctk.CTkComboBox(
    app,
    values=[
        "বাংলা",
        "Hindi",
        "English"
    ]
)

language.pack(pady=25)

student = ctk.CTkButton(
    app,
    text="Student Login",
    width=300,
    height=45
)

student.pack(pady=10)

teacher = ctk.CTkButton(
    app,
    text="Teacher Login",
    width=300,
    height=45
)

teacher.pack(pady=10)

admin = ctk.CTkButton(
    app,
    text="Admin Login",
    width=300,
    height=45
)

admin.pack(pady=10)

app.mainloop()
