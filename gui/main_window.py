"""
Limbus Auto Player - Main Window

Main GUI window class that manages the overall application interface.
"""
import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
import queue
import os

try:
    from lib.settings_handler import load_settings_with_comments
    USE_COMMENT_PRESERVING = True
except ImportError:
    from lib.config import load_settings
    USE_COMMENT_PRESERVING = False

from lib.monitor import get_monitor_info

from .settings_manager import SettingsManager
from .hotkey_manager import HotkeyManager
from .theme_manager import ThemeManager
from .tabs.control_tab import ControlTab
from .tabs.settings_tab import SettingsTab
from .tabs.display_tab import DisplayTab
from .tabs.status_tab import StatusTab
from .detection_worker import DetectionWorker

class LimbusAutoPlayerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Limbus Auto Player")
        self.root.geometry("700x600")
        self.root.resizable(True, True)
        
        # Initialize managers
        self.settings_manager = SettingsManager()
        self.theme_manager = ThemeManager(self)
        self.hotkey_manager = HotkeyManager(self)
        self.detection_worker = DetectionWorker(self)
        
        # Load settings
        self.settings = {}
        self.monitors = []
        self.selected_monitor = None
        self.screen_width = 1920
        self.screen_height = 1080
        self.settings_loaded_successfully = False
        
        # Control variables
        self.is_running = False
        self.is_paused = False
        self.detection_thread = None
        self.stop_event = threading.Event()
        self.pause_event = threading.Event()
        
        # GUI variables
        self.init_gui_variables()
        
        # Status queue for thread communication
        self.status_queue = queue.Queue()
        
        # Initialize
        self.load_initial_settings()
        
        # Create UI
        try:
            if self.settings_loaded_successfully:
                self.create_widgets()
                self.apply_initial_theme()
                self.update_status_display()
                self.root.after(100, self.debug_display_elements)
            else:
                self.create_error_display()
        except Exception as e:
            self.create_minimal_error_display(f"Critical error: {e}")
    
    def init_gui_variables(self):
        """Initialize all GUI variables"""
        self.alt_tab_var = tk.BooleanVar()
        self.reset_cursor_var = tk.BooleanVar()
        self.force_cursor_var = tk.BooleanVar()
        self.debug_logging_var = tk.BooleanVar()
        self.dark_mode_var = tk.BooleanVar()
        self.check_interval_var = tk.DoubleVar(value=1.0)
        self.tolerance_var = tk.IntVar(value=10)
        self.selected_monitor_var = tk.StringVar()
        self.resolution_var = tk.StringVar()
        
        # Color variables
        self.target_r_var = tk.IntVar(value=59)
        self.target_g_var = tk.IntVar(value=1)
        self.target_b_var = tk.IntVar(value=0)
        self.secondary_r_var = tk.IntVar(value=246)
        self.secondary_g_var = tk.IntVar(value=100)
        self.secondary_b_var = tk.IntVar(value=100)
    
    def load_initial_settings(self):
        """Load initial settings from config file"""
        self.settings_loaded_successfully = False
        self.settings_error = "Unknown error"
        
        try:
            if USE_COMMENT_PRESERVING:
                self.settings = load_settings_with_comments()
            else:
                self.settings = load_settings()
            
            # Use the repository root settings file
            script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            self.gui_settings_file = os.path.join(script_dir, 'settings.ini')
            
            self.monitors = get_monitor_info()
            
            # Set initial values
            self.alt_tab_var.set(self.settings.get('alt_tab_after_click', False))
            self.reset_cursor_var.set(self.settings.get('reset_cursor_position', True))
            self.force_cursor_var.set(self.settings.get('force_cursor_to_monitor', False))
            self.debug_logging_var.set(self.settings.get('debug_logging', False))
            self.dark_mode_var.set(self.settings.get('dark_mode', False))
            self.check_interval_var.set(self.settings.get('check_interval', 1.0))
            self.tolerance_var.set(self.settings.get('tolerance', 10))
            
            # Set color values
            target_color = self.settings.get('target_color', (59, 1, 0))
            self.target_r_var.set(target_color[0])
            self.target_g_var.set(target_color[1])
            self.target_b_var.set(target_color[2])
            
            secondary_color = self.settings.get('secondary_color', (246, 175, 100))
            self.secondary_r_var.set(secondary_color[0])
            self.secondary_g_var.set(secondary_color[1])
            self.secondary_b_var.set(secondary_color[2])
            
            # Load GUI-specific settings
            self.settings_manager.load_gui_settings(self)
            
            self.settings_loaded_successfully = True
            
        except Exception as e:
            print(f"Failed to load settings: {e}")
            self.settings_loaded_successfully = False
            self.settings_error = str(e)
            
            # Set fallback values
            script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            self.gui_settings_file = os.path.join(script_dir, 'settings.ini')
    
    def apply_initial_theme(self):
        """Apply the initial theme based on settings"""
        self.theme_manager.apply_theme(self.dark_mode_var.get())
    
    def toggle_dark_mode(self):
        """Toggle between dark and light mode"""
        is_dark = self.dark_mode_var.get()
        self.theme_manager.apply_theme(is_dark)
        
        # Update theme-specific colors in all tabs
        if hasattr(self, 'control_tab'):
            self.control_tab.update_hotkey_colors()
        
        if hasattr(self, 'display_tab'):
            self.display_tab.update_info_colors()
            self.display_tab.update_library_colors()
        
        # Save the theme preference
        self.save_all_settings(show_message=False)
        
        # Update config display
        self.update_config_display()
    
    def create_widgets(self):
        """Create all GUI widgets"""
        # Main container
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Title
        title_label = ttk.Label(main_frame, text="Limbus Auto Player", 
                               font=('Arial', 16, 'bold'))
        title_label.pack(pady=(0, 20))
        
        # Create notebook for tabbed interface
        notebook = ttk.Notebook(main_frame)
        notebook.pack(fill='both', expand=True)
        
        # Create tabs
        self.control_tab = ControlTab(notebook, self)
        self.settings_tab = SettingsTab(notebook, self)
        self.display_tab = DisplayTab(notebook, self)
        self.status_tab = StatusTab(notebook, self)
        
        # Add tabs to notebook
        notebook.add(self.control_tab.frame, text="Control")
        notebook.add(self.settings_tab.frame, text="Settings")
        notebook.add(self.display_tab.frame, text="Display")
        notebook.add(self.status_tab.frame, text="Log")
    
    def create_error_display(self):
        """Create error display when settings can't be loaded"""
        try:
            error_frame = ttk.Frame(self.root)
            error_frame.pack(fill='both', expand=True, padx=20, pady=20)
            
            title_frame = ttk.Frame(error_frame)
            title_frame.pack(pady=(0, 20))
            
            error_label = ttk.Label(title_frame, text="⚠️ Configuration Error", 
                                   font=('Arial', 16, 'bold'), foreground='red')
            error_label.pack()
            
            message_text = ("Could not read settings.ini file.\n\n"
                           "Please ensure the file is present and readable in the root folder.\n"
                           f"Expected location: {getattr(self, 'gui_settings_file', 'settings.ini')}\n\n"
                           f"Error details: {getattr(self, 'settings_error', 'Unknown error')}")
            
            message_label = ttk.Label(error_frame, text=message_text, 
                                     font=('Arial', 10), justify='left')
            message_label.pack(pady=10)
            
            instructions_text = ("To fix this issue:\n"
                               "1. Ensure settings.ini exists in the root folder\n"
                               "2. Check that the file is readable (not corrupted)\n"
                               "3. Restart the application")
            
            instructions_label = ttk.Label(error_frame, text=instructions_text, 
                                         font=('Arial', 9), foreground='gray', justify='left')
            instructions_label.pack(pady=10)
            
            close_button = ttk.Button(error_frame, text="Close Application", 
                                     command=self.root.destroy)
            close_button.pack(pady=20)
            
        except Exception as e:
            self.create_minimal_error_display(f"Error creating error display: {e}")
    
    def create_minimal_error_display(self, error_message):
        """Create a minimal error display that should always work"""
        try:
            label = tk.Label(self.root, 
                           text=f"CONFIGURATION ERROR\n\n{error_message}\n\nCould not load settings.ini\nEnsure the file exists and is readable.",
                           font=('Arial', 12),
                           fg='red',
                           justify='left',
                           wraplength=500)
            label.pack(expand=True, padx=20, pady=20)
            
            button = tk.Button(self.root, 
                             text="Close Application", 
                             command=self.root.destroy,
                             font=('Arial', 10))
            button.pack(pady=10)
            
        except Exception as final_error:
            self.root.title(f"ERROR: Could not load settings.ini - {final_error}")
            try:
                text_widget = tk.Text(self.root, wrap='word')
                text_widget.pack(fill='both', expand=True, padx=10, pady=10)
                text_widget.insert('1.0', f"CRITICAL ERROR\n\nCould not load settings.ini file.\nError: {error_message}\nFinal error: {final_error}")
                text_widget.config(state='disabled')
            except:
                pass
    
    def get_current_colors(self):
        """Get current color values as tuples"""
        target_color = (self.target_r_var.get(), self.target_g_var.get(), self.target_b_var.get())
        secondary_color = (self.secondary_r_var.get(), self.secondary_g_var.get(), self.secondary_b_var.get())
        return target_color, secondary_color
    
    def update_config_display(self):
        """Update the configuration display"""
        if hasattr(self, 'control_tab'):
            self.control_tab.update_config_display()
    
    def toggle_pause(self):
        """Toggle pause/resume state when 'P' key is pressed"""
        if not self.is_running:
            return
        
        if self.is_paused:
            self.resume_detection()
        else:
            self.pause_detection()
    
    def pause_detection(self):
        """Pause the detection"""
        if not self.is_running or self.is_paused:
            return
        
        self.is_paused = True
        self.pause_event.set()
        self.add_status("⏸️ Detection PAUSED (Press 'P' to resume)")
        
        if hasattr(self, 'control_tab'):
            self.root.after(0, lambda: self.control_tab.update_pause_button())
    
    def resume_detection(self):
        """Resume the detection"""
        if not self.is_running or not self.is_paused:
            return
        
        self.is_paused = False
        self.pause_event.clear()
        self.add_status("▶️ Detection RESUMED")
        
        if hasattr(self, 'control_tab'):
            self.root.after(0, lambda: self.control_tab.update_pause_button())
    
    def toggle_detection(self):
        """Toggle detection on/off"""
        if not self.is_running:
            self.start_detection()
        else:
            self.stop_detection()
    
    def start_detection(self):
        """Start the detection thread"""
        if self.is_running:
            return
            
        if not self.selected_monitor:
            messagebox.showerror("Error", "Please select a monitor")
            return
            
        self.is_running = True
        self.is_paused = False
        self.stop_event.clear()
        self.pause_event.clear()
        
        # Update UI
        if hasattr(self, 'control_tab'):
            self.control_tab.update_control_buttons()
        
        # Start detection thread
        self.detection_thread = threading.Thread(target=self.detection_worker.run, daemon=True)
        self.detection_thread.start()
        
        self.add_status("🚀 Detection started! Press 'P' to pause/resume")
    
    def stop_detection(self):
        """Stop the detection"""
        if not self.is_running:
            return
            
        self.is_running = False
        self.is_paused = False
        self.stop_event.set()
        self.pause_event.clear()
        
        # Update UI
        if hasattr(self, 'control_tab'):
            self.control_tab.update_control_buttons()
        
        self.add_status("🛑 Detection stopped!")
        self.update_config_display()
    
    def add_status(self, message):
        """Add a status message to the display"""
        timestamp = time.strftime("%H:%M:%S")
        full_message = f"[{timestamp}] {message}\n"
        self.status_queue.put(full_message)
    
    def update_status_display(self):
        """Update status display from queue"""
        try:
            while True:
                message = self.status_queue.get_nowait()
                if hasattr(self, 'control_tab'):
                    self.control_tab.add_status_message(message)
        except queue.Empty:
            pass
            
        self.root.after(100, self.update_status_display)
    
    def save_all_settings(self, show_message=True):
        """Save all settings to file"""
        self.settings_manager.save_all_settings(self, USE_COMMENT_PRESERVING, show_message)
    
    def debug_display_elements(self):
        """Debug function to check if display elements are working"""
        print(f"Debug: Selected monitor: {self.selected_monitor}")
        print(f"Debug: Resolution var: {self.resolution_var.get()}")
        print(f"Debug: Monitor var: {self.selected_monitor_var.get()}")
        print(f"Debug: Number of monitors: {len(self.monitors)}")
        self.update_config_display()
    
    def on_closing(self):
        """Handle window closing"""
        self.save_all_settings(show_message=False)
        
        if self.is_running:
            self.stop_detection()
            if self.detection_thread and self.detection_thread.is_alive():
                self.detection_thread.join(timeout=1)
        
        self.root.destroy()