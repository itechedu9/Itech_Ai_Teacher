import customtkinter as ctk


class StatCard(ctk.CTkFrame):

    def __init__(self, parent, icon, title, value, color):

        super().__init__(
            parent,
            corner_radius=15,
            fg_color="#313335",
            width=260,
            height=150
        )

        self.pack_propagate(False)

        icon_label = ctk.CTkLabel(
            self,
            text=icon,
            font=("Segoe UI Emoji", 34)
        )

        icon_label.pack(anchor="w", padx=20, pady=(15, 0))

        title_label = ctk.CTkLabel(
            self,
            text=title,
            font=("Segoe UI", 18, "bold")
        )

        title_label.pack(anchor="w", padx=20)

        value_label = ctk.CTkLabel(
            self,
            text=value,
            text_color=color,
            font=("Segoe UI", 30, "bold")
        )

        value_label.pack(anchor="w", padx=20)

        growth = ctk.CTkLabel(
            self,
            text="▲ +12% This Month",
            text_color="#00C853",
            font=("Segoe UI", 13)
        )

        growth.pack(anchor="w", padx=20)

        details = ctk.CTkButton(
            self,
            text="View Details →",
            width=140,
            height=30
        )

        details.pack(anchor="w", padx=20, pady=10)
