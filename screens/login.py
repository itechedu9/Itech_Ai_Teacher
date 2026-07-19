import customtkinter as ctk
from tkinter import messagebox


ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


def login():

    username = username_entry.get()
    password = password_entry.get()

    from utils.auth import login as db_login

    user = db_login(username, password)

    if user:
        messagebox.showinfo("Success", "Login Successful!")

        app.destroy()

        from screens.dashboard import run_dashboard
        run_dashboard()

    else:
        messagebox.showerror("Error", "Invalid Username or Password")

app = ctk.CTk()

app.title("ITECH AI Teacher")
app.geometry("500x650")
app.resizable(False, False)

# ---------------- Title ----------------

title = ctk.CTkLabel(
    app,
    text="🤖 ITECH AI Teacher",
    font=("Segoe UI", 28, "bold")
)

title.pack(pady=(40,10))

subtitle = ctk.CTkLabel(
    app,
    text="Welcome to Enterprise Edition",
    font=("Segoe UI",15)
)

subtitle.pack(pady=(0,30))

# ---------------- Username ----------------

username_entry = ctk.CTkEntry(
    app,
    width=320,
    height=45,
    placeholder_text="Username"
)

username_entry.pack(pady=10)

# ---------------- Password ----------------

password_entry = ctk.CTkEntry(
    app,
    width=320,
    height=45,
    placeholder_text="Password",
    show="*"
)

password_entry.pack(pady=10)

# ---------------- Remember ----------------

remember = ctk.CTkCheckBox(
    app,
    text="Remember Me"
)

remember.pack(anchor="w", padx=90, pady=10)

# ---------------- Login Button ----------------

login_btn = ctk.CTkButton(
    app,
    text="Login",
    width=320,
    height=45,
    command=login
)

login_btn.pack(pady=20)

# ---------------- Footer ----------------

footer = ctk.CTkLabel(
    app,
    text="© 2026 ITECH Computer Education",
    font=("Segoe UI",12)
)

footer.pack(side="bottom", pady=20)


def run_login():
    app.mainloop()
