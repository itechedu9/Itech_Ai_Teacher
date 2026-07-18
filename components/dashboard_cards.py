import customtkinter as ctk
from components.stat_card import StatCard


def create_cards(parent):

    container = ctk.CTkFrame(
        parent,
        fg_color="transparent"
    )

    container.pack(fill="x", padx=20, pady=20)

    data = [

        ("👨‍🎓", "Students", "2564", "#00C853"),

        ("👨‍🏫", "Teachers", "48", "#00C853"),

        ("📚", "Courses", "125", "#29B6F6"),

        ("💼", "Jobs", "32", "#FFA726"),

        ("🤖", "AI Sessions", "12450", "#AB47BC"),

        ("💰", "Revenue", "₹845000", "#26C6DA")

    ]

    for i, (icon, title, value, color) in enumerate(data):

        card = StatCard(
            container,
            icon,
            title,
            value,
            color
        )

        row = i // 3
        col = i % 3

        card.grid(
            row=row,
            column=col,
            padx=15,
            pady=15,
            sticky="nsew"
        )

    for i in range(3):
        container.grid_columnconfigure(i, weight=1)
