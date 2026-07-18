import customtkinter as ctk

def create_ai_panel(parent):

    frame = ctk.CTkFrame(parent,
                         corner_radius=15)

    frame.pack(side="right",
               fill="both",
               expand=True,
               padx=20,
               pady=10)

    title = ctk.CTkLabel(
        frame,
        text="🤖 AI Assistant",
        font=("Segoe UI",20,"bold")
    )

    title.pack(anchor="w",
               padx=15,
               pady=15)

    chat = ctk.CTkTextbox(frame)

    chat.insert(
        "1.0",
        "Welcome to ITECH AI Teacher\n\nHow can I help you today?"
    )

    chat.pack(fill="both",
              expand=True,
              padx=15,
              pady=15)

    return frame
