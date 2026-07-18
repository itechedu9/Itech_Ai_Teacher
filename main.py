import tkinter as tk

window = tk.Tk()
window.title("ITECH AI Teacher")
window.geometry("900x600")

title = tk.Label(
    window,
    text="ITECH AI Teacher",
    font=("Arial", 24, "bold")
)
title.pack(pady=30)

subtitle = tk.Label(
    window,
    text="Welcome to the Future of Learning",
    font=("Arial", 14)
)
subtitle.pack(pady=10)

start_btn = tk.Button(
    window,
    text="Start Learning",
    font=("Arial", 14),
    width=20
)
start_btn.pack(pady=20)

window.mainloop()
