"""
Limbus Company Auto Player - Settings Tab

Interface for configuring detection and behavior settings.
"""
import tkinter as tk
from tkinter import ttk

class SettingsTab:
    def __init__(self, parent, app):
        self.app = app
        self.frame = ttk.Frame(parent)
        self.create_widgets()
    
    def create_widgets(self):
        """Create the settings tab widgets"""
        # Appearance settings
        appearance_frame = ttk.LabelFrame(self.frame, text="Appearance", padding=10)
        appearance_frame.pack(fill='x', pady=(0, 10))
        
        ttk.Checkbutton(appearance_frame, text="Dark mode", 
                       variable=self.app.dark_mode_var, 
                       command=self.app.toggle_dark_mode).pack(anchor='w')
        
        # Behavior settings
        behavior_frame = ttk.LabelFrame(self.frame, text="Behavior Settings", padding=10)
        behavior_frame.pack(fill='x', pady=(0, 10))
        
        ttk.Checkbutton(behavior_frame, text="Alt+Tab after click (switch away from game)", 
                       variable=self.app.alt_tab_var, 
                       command=self.app.update_config_display).pack(anchor='w')
        
        ttk.Checkbutton(behavior_frame, text="Reset cursor position after click", 
                       variable=self.app.reset_cursor_var, 
                       command=self.app.update_config_display).pack(anchor='w')
        
        ttk.Checkbutton(behavior_frame, text="Force cursor to monitor before click", 
                       variable=self.app.force_cursor_var, 
                       command=self.app.update_config_display).pack(anchor='w')
        
        ttk.Checkbutton(behavior_frame, text="Enable debug logging (log.txt)", 
                       variable=self.app.debug_logging_var, 
                       command=self.app.update_config_display).pack(anchor='w')
        
        # Detection settings
        detection_frame = ttk.LabelFrame(self.frame, text="Detection Settings", padding=10)
        detection_frame.pack(fill='x', pady=(0, 10))
        
        # Check interval
        interval_frame = ttk.Frame(detection_frame)
        interval_frame.pack(fill='x', pady=2)
        ttk.Label(interval_frame, text="Check interval (seconds):").pack(side='left')
        interval_spinbox = ttk.Spinbox(interval_frame, from_=0.1, to=10.0, increment=0.1, 
                                      textvariable=self.app.check_interval_var, width=10,
                                      command=self.app.update_config_display)
        interval_spinbox.pack(side='right')
        interval_spinbox.bind('<KeyRelease>', lambda e: self.app.update_config_display())
        
        # Tolerance
        tolerance_frame = ttk.Frame(detection_frame)
        tolerance_frame.pack(fill='x', pady=2)
        ttk.Label(tolerance_frame, text="Color tolerance:").pack(side='left')
        tolerance_spinbox = ttk.Spinbox(tolerance_frame, from_=1, to=50, increment=1,
                                       textvariable=self.app.tolerance_var, width=10,
                                       command=self.app.update_config_display)
        tolerance_spinbox.pack(side='right')
        tolerance_spinbox.bind('<KeyRelease>', lambda e: self.app.update_config_display())
        
        # Color settings
        self.create_color_settings()
    
    def create_color_settings(self):
        """Create color configuration widgets"""
        color_frame = ttk.LabelFrame(self.frame, text="Detection Colors", padding=10)
        color_frame.pack(fill='x', pady=(0, 10))
        
        # Target color (button background)
        target_frame = ttk.LabelFrame(color_frame, text="Target Color (Button Background)", padding=5)
        target_frame.pack(fill='x', pady=(0, 5))
        
        target_rgb_frame = ttk.Frame(target_frame)
        target_rgb_frame.pack(fill='x')
        
        ttk.Label(target_rgb_frame, text="R:", width=2).grid(row=0, column=0, padx=2)
        ttk.Spinbox(target_rgb_frame, from_=0, to=255, width=5, textvariable=self.app.target_r_var,
                   command=self.update_color_previews).grid(row=0, column=1, padx=2)
        
        ttk.Label(target_rgb_frame, text="G:", width=2).grid(row=0, column=2, padx=2)
        ttk.Spinbox(target_rgb_frame, from_=0, to=255, width=5, textvariable=self.app.target_g_var,
                   command=self.update_color_previews).grid(row=0, column=3, padx=2)
        
        ttk.Label(target_rgb_frame, text="B:", width=2).grid(row=0, column=4, padx=2)
        ttk.Spinbox(target_rgb_frame, from_=0, to=255, width=5, textvariable=self.app.target_b_var,
                   command=self.update_color_previews).grid(row=0, column=5, padx=2)
        
        self.target_preview = tk.Label(target_rgb_frame, text="   ", width=3)
        self.target_preview.grid(row=0, column=6, padx=10)
        
        # Secondary color (text)
        secondary_frame = ttk.LabelFrame(color_frame, text="Secondary Color (Text)", padding=5)
        secondary_frame.pack(fill='x', pady=(5, 0))
        
        secondary_rgb_frame = ttk.Frame(secondary_frame)
        secondary_rgb_frame.pack(fill='x')
        
        ttk.Label(secondary_rgb_frame, text="R:", width=2).grid(row=0, column=0, padx=2)
        ttk.Spinbox(secondary_rgb_frame, from_=0, to=255, width=5, textvariable=self.app.secondary_r_var,
                   command=self.update_color_previews).grid(row=0, column=1, padx=2)
        
        ttk.Label(secondary_rgb_frame, text="G:", width=2).grid(row=0, column=2, padx=2)
        ttk.Spinbox(secondary_rgb_frame, from_=0, to=255, width=5, textvariable=self.app.secondary_g_var,
                   command=self.update_color_previews).grid(row=0, column=3, padx=2)
        
        ttk.Label(secondary_rgb_frame, text="B:", width=2).grid(row=0, column=4, padx=2)
        ttk.Spinbox(secondary_rgb_frame, from_=0, to=255, width=5, textvariable=self.app.secondary_b_var,
                   command=self.update_color_previews).grid(row=0, column=5, padx=2)
        
        self.secondary_preview = tk.Label(secondary_rgb_frame, text="   ", width=3)
        self.secondary_preview.grid(row=0, column=6, padx=10)
        
        # Bind events for color preview updates
        for var in [self.app.target_r_var, self.app.target_g_var, self.app.target_b_var,
                   self.app.secondary_r_var, self.app.secondary_g_var, self.app.secondary_b_var]:
            var.trace('w', self.update_color_previews)
        
        self.update_color_previews()
    
    def update_color_previews(self, *args):
        """Update color preview labels"""
        try:
            # Target color preview
            target_r = self.app.target_r_var.get()
            target_g = self.app.target_g_var.get()
            target_b = self.app.target_b_var.get()
            target_hex = f"#{target_r:02x}{target_g:02x}{target_b:02x}"
            self.target_preview.config(bg=target_hex)
            
            # Secondary color preview
            secondary_r = self.app.secondary_r_var.get()
            secondary_g = self.app.secondary_g_var.get()
            secondary_b = self.app.secondary_b_var.get()
            secondary_hex = f"#{secondary_r:02x}{secondary_g:02x}{secondary_b:02x}"
            self.secondary_preview.config(bg=secondary_hex)
            
        except (tk.TclError, ValueError):
            # Handle invalid color values
            pass
        
        # Update configuration display
        self.app.update_config_display()