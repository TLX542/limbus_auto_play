"""
Limbus Company Auto Player - Display Tab

Interface for monitor and resolution configuration.
"""
import tkinter as tk
from tkinter import ttk, messagebox
from lib.library_checker import get_missing_libraries

class DisplayTab:
    def __init__(self, parent, app):
        self.app = app
        self.frame = ttk.Frame(parent)
        self.create_widgets()
    
    def create_widgets(self):
        """Create the display tab widgets"""
        # Monitor selection (only show if multiple monitors)
        if len(self.app.monitors) > 1:
            self.create_monitor_selection()
        
        # Resolution settings
        self.create_resolution_settings()
        
        # Library status
        self.create_library_status()
    
    def create_monitor_selection(self):
        """Create monitor selection widgets"""
        monitor_frame = ttk.LabelFrame(self.frame, text="Monitor Selection", padding=10)
        monitor_frame.pack(fill='x', pady=(0, 10))
        
        ttk.Label(monitor_frame, text="Select monitor:").pack(anchor='w')
        
        self.monitor_combo = ttk.Combobox(monitor_frame, textvariable=self.app.selected_monitor_var,
                                         state='readonly', width=50)
        monitor_values = []
        for monitor in self.app.monitors:
            status = " (Primary)" if monitor.get('is_primary', False) else ""
            monitor_values.append(f"{monitor['name']} ({monitor['width']}x{monitor['height']}){status}")
        self.monitor_combo['values'] = monitor_values
        self.monitor_combo.pack(fill='x', pady=5)
        self.monitor_combo.bind('<<ComboboxSelected>>', self.on_monitor_changed)
    
    def create_resolution_settings(self):
        """Create resolution configuration widgets"""
        # Remove existing resolution frame if it exists
        if hasattr(self, 'resolution_frame'):
            self.resolution_frame.destroy()
        
        self.resolution_frame = ttk.LabelFrame(self.frame, text="Resolution Settings", padding=10)
        self.resolution_frame.pack(fill='x', pady=(0, 10))
        
        ttk.Label(self.resolution_frame, text="Current resolution:").pack(anchor='w')
        
        self.resolution_combo = ttk.Combobox(self.resolution_frame, textvariable=self.app.resolution_var,
                                            width=30)
        
        # Common resolutions
        common_resolutions = [
            "1920x1080",
            "2560x1440", 
            "3840x2160",
            "1600x900",
            "1366x768",
            "Custom..."
        ]
        
        self.resolution_combo['values'] = common_resolutions
        self.resolution_combo.pack(fill='x', pady=5)
        self.resolution_combo.bind('<<ComboboxSelected>>', self.on_resolution_changed)
        self.resolution_combo.bind('<KeyRelease>', self.on_resolution_changed)
        
        # DPI scaling info
        scaling_info_frame = ttk.Frame(self.resolution_frame)
        scaling_info_frame.pack(fill='x', pady=(10, 0))
        
        self.info_label = ttk.Label(scaling_info_frame, text="ℹ️ Windows DPI scaling can affect detection accuracy")
        self.info_label.pack(anchor='w')
        
        self.normal_label = ttk.Label(scaling_info_frame, text="Ensure the resolution matches your monitor's native resolution")
        self.normal_label.pack(anchor='w')
        
        self.gray_label = ttk.Label(scaling_info_frame, text="If detection fails, ensure the resolution matches your monitor")
        self.gray_label.pack(anchor='w')
        
        # Apply initial theme colors
        self.update_info_colors()
    
    def update_info_colors(self):
        """Update info text colors based on current theme"""
        if hasattr(self.app, 'theme_manager'):
            is_dark = self.app.dark_mode_var.get()
            
            # Update info text color
            info_color = self.app.theme_manager.get_text_color_for_type('info', is_dark)
            self.info_label.configure(foreground=info_color)
            
            # Update normal text color
            normal_color = self.app.theme_manager.get_text_color_for_type('normal', is_dark)
            self.normal_label.configure(foreground=normal_color)
            
            # Update gray text color
            disabled_color = self.app.theme_manager.get_text_color_for_type('disabled', is_dark)
            self.gray_label.configure(foreground=disabled_color)
    
    def create_library_status(self):
        """Create library status display"""
        # Remove existing library frame if it exists
        if hasattr(self, 'lib_frame'):
            self.lib_frame.destroy()
        
        self.lib_frame = ttk.LabelFrame(self.frame, text="Library Status", padding=10)
        self.lib_frame.pack(fill='x')
        
        missing_libs = get_missing_libraries()
        if not missing_libs:
            self.lib_status_label = ttk.Label(self.lib_frame, text="✅ All optional libraries are available")
            self.lib_status_label.pack(anchor='w')
        else:
            self.lib_status_label = ttk.Label(self.lib_frame, text="⚠️ Some optional libraries are missing:")
            self.lib_status_label.pack(anchor='w')
            
            self.lib_detail_labels = []
            for name, install_cmd, impact in missing_libs:
                label = ttk.Label(self.lib_frame, text=f"  • {name}: {install_cmd}", 
                                 font=('Courier', 8))
                label.pack(anchor='w')
                self.lib_detail_labels.append(label)
        
        # Apply theme colors
        self.update_library_colors()
    
    def update_library_colors(self):
        """Update library status colors based on current theme"""
        if hasattr(self.app, 'theme_manager'):
            is_dark = self.app.dark_mode_var.get()
            
            missing_libs = get_missing_libraries()
            if not missing_libs:
                # Success color for all libraries available
                success_color = self.app.theme_manager.get_text_color_for_type('success', is_dark)
                self.lib_status_label.configure(foreground=success_color)
            else:
                # Warning color for missing libraries
                warning_color = self.app.theme_manager.get_text_color_for_type('warning', is_dark)
                self.lib_status_label.configure(foreground=warning_color)
                
                # Gray color for detail text
                disabled_color = self.app.theme_manager.get_text_color_for_type('disabled', is_dark)
                if hasattr(self, 'lib_detail_labels'):
                    for label in self.lib_detail_labels:
                        label.configure(foreground=disabled_color)
    
    def on_monitor_changed(self, event=None):
        """Handle monitor selection change"""
        selection = self.app.selected_monitor_var.get()
        if selection:
            # Find the selected monitor
            for monitor in self.app.monitors:
                status = " (Primary)" if monitor.get('is_primary', False) else ""
                expected = f"{monitor['name']} ({monitor['width']}x{monitor['height']}){status}"
                if expected == selection:
                    self.app.selected_monitor = monitor
                    self.app.screen_width = monitor['width']
                    self.app.screen_height = monitor['height']
                    self.app.resolution_var.set(f"{self.app.screen_width}x{self.app.screen_height}")
                    self.app.update_config_display()
                    self.app.settings_manager.save_gui_settings(self.app)
                    break
    
    def on_resolution_changed(self, event=None):
        """Handle resolution change"""
        resolution = self.app.resolution_var.get()
        
        if resolution == "Custom...":
            self.open_custom_resolution_dialog()
        elif 'x' in resolution:
            try:
                # Extract width and height
                res_part = resolution.split('(')[0].strip()
                width_str, height_str = res_part.split('x')
                self.app.screen_width = int(width_str.strip())
                self.app.screen_height = int(height_str.strip())
                self.app.update_config_display()
                self.app.settings_manager.save_gui_settings(self.app)
                
            except ValueError:
                pass  # Invalid format, ignore
    
    def open_custom_resolution_dialog(self):
        """Open dialog for custom resolution input"""
        dialog = tk.Toplevel(self.app.root)
        dialog.title("Custom Resolution")
        dialog.geometry("300x150")
        dialog.resizable(False, False)
        dialog.grab_set()
        
        # Apply theme to dialog
        if hasattr(self.app, 'theme_manager'):
            is_dark = self.app.dark_mode_var.get()
            theme = self.app.theme_manager.dark_theme if is_dark else self.app.theme_manager.light_theme
            dialog.configure(bg=theme['bg'])
        
        ttk.Label(dialog, text="Enter custom resolution:").pack(pady=10)
        
        entry_frame = ttk.Frame(dialog)
        entry_frame.pack(pady=10)
        
        width_entry = ttk.Entry(entry_frame, width=8)
        width_entry.pack(side='left')
        width_entry.insert(0, str(self.app.screen_width))
        
        ttk.Label(entry_frame, text=" x ").pack(side='left')
        
        height_entry = ttk.Entry(entry_frame, width=8)
        height_entry.pack(side='left')
        height_entry.insert(0, str(self.app.screen_height))
        
        def apply_custom():
            try:
                width = int(width_entry.get())
                height = int(height_entry.get())
                if width > 0 and height > 0:
                    self.app.screen_width = width
                    self.app.screen_height = height
                    self.app.resolution_var.set(f"{width}x{height}")
                    self.app.update_config_display()
                    self.app.settings_manager.save_gui_settings(self.app)
                    dialog.destroy()
                else:
                    messagebox.showerror("Error", "Width and height must be positive numbers")
            except ValueError:
                messagebox.showerror("Error", "Please enter valid numbers")
        
        button_frame = ttk.Frame(dialog)
        button_frame.pack(pady=20)
        
        ttk.Button(button_frame, text="Apply", command=apply_custom).pack(side='left', padx=5)
        ttk.Button(button_frame, text="Cancel", command=dialog.destroy).pack(side='left', padx=5)