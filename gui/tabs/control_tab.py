"""
Limbus Auto Player - Control Tab

Main control interface for starting/stopping detection and viewing status.
"""
import tkinter as tk
from tkinter import ttk, scrolledtext

class ControlTab:
    def __init__(self, parent, app):
        self.app = app
        self.frame = ttk.Frame(parent)
        self.create_widgets()
    
    def create_widgets(self):
        """Create the control tab widgets"""
        # Control buttons frame
        button_frame = ttk.LabelFrame(self.frame, text="Control", padding=10)
        button_frame.pack(fill='x', pady=(0, 10))
        
        # Main control buttons
        control_buttons_frame = ttk.Frame(button_frame)
        control_buttons_frame.pack(fill='x')
        
        self.toggle_button = ttk.Button(control_buttons_frame, text="Start Detection", 
                                        command=self.app.toggle_detection, 
                                        width=20)
        self.toggle_button.pack(side='left', padx=(0, 10))
        
        # Pause/resume button
        self.pause_button = ttk.Button(control_buttons_frame, text="Pause (P)", 
                                      command=self.app.toggle_pause, 
                                      width=15, state='disabled')
        self.pause_button.pack(side='left', padx=(0, 10))
        
        # Save settings button
        save_button = ttk.Button(control_buttons_frame, text="Save Settings", 
                                command=lambda: self.app.save_all_settings(show_message=True), 
                                width=15)
        save_button.pack(side='left')
        
        # Hotkey info
        hotkey_frame = ttk.Frame(button_frame)
        hotkey_frame.pack(fill='x', pady=(10, 0))
        
        self.hotkey_label = ttk.Label(hotkey_frame, text="💡 Press 'P' anywhere to pause/resume detection", 
                                     font=('Arial', 9))
        self.hotkey_label.pack(anchor='w')
        
        # Apply initial theme colors
        self.update_hotkey_colors()
        
        # Current settings display
        current_frame = ttk.LabelFrame(self.frame, text="Current Configuration", padding=10)
        current_frame.pack(fill='x', pady=(0, 10))
        
        self.config_label = ttk.Label(current_frame, text="", justify='left')
        self.config_label.pack(anchor='w')
        
        # Status display
        status_frame = ttk.LabelFrame(self.frame, text="Status", padding=10)
        status_frame.pack(fill='both', expand=True)
        
        self.status_text = scrolledtext.ScrolledText(status_frame, height=8, width=60)
        self.status_text.pack(fill='both', expand=True)
        
        self.update_config_display()
    
    def update_config_display(self):
        """Update the configuration display"""
        target_color, secondary_color = self.app.get_current_colors()
        
        status_text = "PAUSED" if self.app.is_paused else ("RUNNING" if self.app.is_running else "STOPPED")
        
        config_text = f"""Status: {status_text}
Monitor: {self.app.selected_monitor['name'] if self.app.selected_monitor else 'None'}
Resolution: {self.app.screen_width}x{self.app.screen_height}
Theme: {'Dark' if self.app.dark_mode_var.get() else 'Light'} Mode
Check Interval: {self.app.check_interval_var.get()}s
Tolerance: {self.app.tolerance_var.get()}
Target Color: RGB{target_color}
Secondary Color: RGB{secondary_color}
Alt+Tab: {'Yes' if self.app.alt_tab_var.get() else 'No'}
Reset Cursor: {'Yes' if self.app.reset_cursor_var.get() else 'No'}
Force Cursor: {'Yes' if self.app.force_cursor_var.get() else 'No'}
Debug Logging: {'Yes' if self.app.debug_logging_var.get() else 'No'}"""
        
        self.config_label.config(text=config_text)
    
    def update_control_buttons(self):
        """Update control button states"""
        if self.app.is_running:
            self.toggle_button.config(text="Stop Detection")
            self.pause_button.config(state='normal')
        else:
            self.toggle_button.config(text="Start Detection")
            self.pause_button.config(state='disabled')
    
    def update_pause_button(self):
        """Update pause button text based on current state"""
        if self.app.is_paused:
            self.toggle_button.config(text="Resume Detection")
        else:
            self.toggle_button.config(text="Stop Detection")
    
    def update_hotkey_colors(self):
        """Update hotkey info color based on current theme"""
        if hasattr(self.app, 'theme_manager'):
            is_dark = self.app.dark_mode_var.get()
            info_color = self.app.theme_manager.get_text_color_for_type('info', is_dark)
            self.hotkey_label.configure(foreground=info_color)
    
    def add_status_message(self, message):
        """Add a status message to the status display"""
        self.status_text.insert(tk.END, message)
        self.status_text.see(tk.END)