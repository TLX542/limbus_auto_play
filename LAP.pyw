#!/usr/bin/env python3
"""
Limbus Company Auto Player - Main Entry Point

Entry point for the Limbus Company automation GUI application.
"""
import tkinter as tk
from tkinter import ttk
from gui.main_window import LimbusAutoPlayerGUI

def main():
    """Main function to run the GUI"""
    root = tk.Tk()
    
    # Set up theme
    style = ttk.Style()
    
    # Try to use a modern theme
    available_themes = style.theme_names()
    if 'vista' in available_themes:
        style.theme_use('vista')
    elif 'clam' in available_themes:
        style.theme_use('clam')
    
    # Create and configure the application
    app = LimbusAutoPlayerGUI(root)
    
    # Handle window closing
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    
    # Only center window if settings loaded successfully
    if app.settings_loaded_successfully:
        # Center window on screen
        root.update_idletasks()
        x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
        y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
        root.geometry(f"+{x}+{y}")
    
    # Start the GUI
    root.mainloop()

if __name__ == "__main__":
    main()