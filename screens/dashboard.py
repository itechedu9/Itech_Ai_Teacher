import customtkinter as ctk

from components.sidebar import create_sidebar
from components.topbar import create_topbar
from components.dashboard_cards import create_cards
from components.graph_panel import create_graph_panel
from components.activity_panel import create_activity
from components.ai_panel import create_ai_panel


def run_dashboard():

    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()

    app.title("ITECH AI Teacher Enterprise")
    app.geometry("1400x850")

    # Sidebar
    create_sidebar(app)

    # Main Area
    main = ctk.CTkFrame(app)
    main.pack(side="right", fill="both", expand=True)

    # Topbar
    create_topbar(main)

    # Dashboard Cards
    create_cards(main)

    # Graph
    create_graph_panel(main)

    # Bottom
    bottom = ctk.CTkFrame(main, fg_color="transparent")
    bottom.pack(fill="both", expand=True, padx=20, pady=10)

    create_activity(bottom)
    create_ai_panel(bottom)

    app.mainloop()
