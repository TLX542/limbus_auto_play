"""
Limbus Company Auto Player - Status Tab

Interface for viewing debug logs and application status.
"""
import os
import tkinter as tk
from tkinter import ttk, scrolledtext

class StatusTab:
    def __init__(self, parent, app):
        self.app = app
        self.frame = ttk.Frame(parent)
        self.create_widgets()
    
    def create_widgets(self):
        """Create the status/log tab widgets"""
        log_frame = ttk.LabelFrame(self.frame, text="Debug Log", padding=10)
        log_frame.pack(fill='both', expand=True)
        
        self.log_text = scrolledtext.ScrolledText(log_frame, height=20)
        self.log_text.pack(fill='both', expand=True)
        
        # Log controls
        log_control_frame = ttk.Frame(log_frame)
        log_control_frame.pack(fill='x', pady=(10, 0))
        
        ttk.Button(log_control_frame, text="Clear Log", 
                  command=self.clear_log).pack(side='left')
        
        ttk.Button(log_control_frame, text="Refresh Log", 
                  command=self.refresh_log).pack(side='left', padx=(10, 0))
    
    def clear_log(self):
        """Clear the debug log display"""
        self.log_text.delete(1.0, tk.END)
    
    def refresh_log(self):
        """Refresh the debug log from file"""
        if not self.app.debug_logging_var.get():
            self.log_text.delete(1.0, tk.END)
            self.log_text.insert(tk.END, "Debug logging is disabled. Enable it in Settings tab.\n")
            return
            
        log_file = os.path.join(self.app.settings['script_dir'], 'log.txt')
        
        try:
            if os.path.exists(log_file):
                with open(log_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    self.log_text.delete(1.0, tk.END)
                    self.log_text.insert(tk.END, content)
                    self.log_text.see(tk.END)
            else:
                self.log_text.delete(1.0, tk.END)
                self.log_text.insert(tk.END, "No log file found. Start detection to create logs.\n")
        except Exception as e:
            self.log_text.delete(1.0, tk.END)
            self.log_text.insert(tk.END, f"Error reading log file: {e}\n")