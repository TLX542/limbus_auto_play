"""
Limbus Auto Player - Settings Manager

Handles loading and saving of GUI and application settings.
"""
import os
import configparser
from tkinter import messagebox
from lib.monitor import get_monitor_info

class SettingsManager:
    def __init__(self):
        pass
    
    def load_gui_settings(self, app):
        """Load GUI-specific settings from the main settings.ini file"""
        config = configparser.ConfigParser(interpolation=None)
        
        # Default values
        default_monitor = None
        default_resolution = "1920x1080"
        default_dark_mode = False  # Default to light mode
        
        # Try to get monitor info, with fallback if it fails
        try:
            if not hasattr(app, 'monitors') or not app.monitors:
                app.monitors = get_monitor_info()
        except:
            app.monitors = [{
                'name': 'Primary Monitor',
                'width': 1920,
                'height': 1080,
                'x': 0,
                'y': 0,
                'is_primary': True
            }]
        
        # Try to load saved GUI settings from main settings file
        if os.path.exists(app.gui_settings_file):
            try:
                config.read(app.gui_settings_file)
                
                if config.has_section('GUI'):
                    saved_monitor_name = config.get('GUI', 'SELECTED_MONITOR', fallback='')
                    saved_resolution = config.get('GUI', 'RESOLUTION', fallback=default_resolution)
                    saved_dark_mode = config.getboolean('GUI', 'DARK_MODE', fallback=default_dark_mode)
                    
                    # Set dark mode preference
                    app.dark_mode_var.set(saved_dark_mode)
                    
                    # Try to find the saved monitor
                    for monitor in app.monitors:
                        if monitor['name'] == saved_monitor_name:
                            default_monitor = monitor
                            break
                    
                    if default_monitor:
                        default_resolution = saved_resolution
                else:
                    # GUI section doesn't exist, use defaults and create it
                    app.dark_mode_var.set(default_dark_mode)
                    self._create_gui_section_if_missing(app.gui_settings_file)
                
            except Exception as e:
                print(f"Warning: Could not load GUI settings: {e}")
                # Set to default values
                app.dark_mode_var.set(default_dark_mode)
                self._create_gui_section_if_missing(app.gui_settings_file)
        else:
            # Settings file doesn't exist, set defaults
            app.dark_mode_var.set(default_dark_mode)
        
        # If no saved monitor or monitor not found, use primary
        if not default_monitor:
            default_monitor = next((m for m in app.monitors if m.get('is_primary', False)), app.monitors[0])
            default_resolution = f"{default_monitor['width']}x{default_monitor['height']}"
        
        # Set the selected monitor
        app.selected_monitor = default_monitor
        app.selected_monitor_var.set(f"{default_monitor['name']} ({default_monitor['width']}x{default_monitor['height']})")
        
        # Set resolution
        app.resolution_var.set(default_resolution)
        
        # Parse resolution for screen dimensions
        try:
            res_part = default_resolution.split('(')[0].strip()
            if 'x' in res_part:
                width_str, height_str = res_part.split('x')
                app.screen_width = int(width_str.strip())
                app.screen_height = int(height_str.strip())
            else:
                app.screen_width = default_monitor['width']
                app.screen_height = default_monitor['height']
        except:
            app.screen_width = default_monitor['width']
            app.screen_height = default_monitor['height']
    
    def _create_gui_section_if_missing(self, settings_file):
        """Create GUI section with default values if it doesn't exist"""
        try:
            config = configparser.ConfigParser(interpolation=None)
            
            # Read existing file if it exists
            if os.path.exists(settings_file):
                config.read(settings_file)
            
            # Add GUI section if it doesn't exist
            if not config.has_section('GUI'):
                config.add_section('GUI')
                config.set('GUI', 'SELECTED_MONITOR', 'Monitor 1')
                config.set('GUI', 'RESOLUTION', '1920x1080')
                config.set('GUI', 'DARK_MODE', 'false')
                
                # Save the updated file
                with open(settings_file, 'w') as f:
                    config.write(f)
                    
                print("Created GUI section in settings.ini with default values")
                
        except Exception as e:
            print(f"Warning: Could not create GUI section: {e}")
    
    def save_gui_settings(self, app):
        """Save GUI-specific settings to the main settings.ini file"""
        config = configparser.ConfigParser(interpolation=None)
        
        # Read existing settings first to preserve them
        if os.path.exists(app.gui_settings_file):
            try:
                config.read(app.gui_settings_file)
            except Exception as e:
                print(f"Warning: Could not read existing settings: {e}")
        
        # Add GUI section if it doesn't exist
        if not config.has_section('GUI'):
            config.add_section('GUI')
        
        # Save GUI-specific settings
        if app.selected_monitor:
            config.set('GUI', 'SELECTED_MONITOR', app.selected_monitor['name'])
        
        config.set('GUI', 'RESOLUTION', app.resolution_var.get())
        config.set('GUI', 'DARK_MODE', str(app.dark_mode_var.get()).lower())
        
        try:
            with open(app.gui_settings_file, 'w') as f:
                config.write(f)
        except Exception as e:
            print(f"Warning: Could not save GUI settings: {e}")
    
    def save_all_settings(self, app, use_comment_preserving, show_message=True):
        """Save all settings (both GUI and detection) to the main settings.ini file"""
        if use_comment_preserving and '_handler' in app.settings:
            # Use the comment-preserving handler
            try:
                from lib.settings_handler import save_all_settings_with_comments
                save_all_settings_with_comments(app, show_message)
            except ImportError:
                self._fallback_save_all_settings(app, show_message)
        else:
            self._fallback_save_all_settings(app, show_message)
    
    def _fallback_save_all_settings(self, app, show_message):
        """Fallback method to save all settings"""
        config = configparser.ConfigParser(interpolation=None)
        
        # Read existing settings first to preserve any comments or formatting
        if os.path.exists(app.gui_settings_file):
            try:
                config.read(app.gui_settings_file)
            except Exception as e:
                print(f"Warning: Could not read existing settings: {e}")
        
        # Ensure all required sections exist
        sections_to_ensure = ['DETECTION', 'TIMING', 'BEHAVIOR', 'DEBUG', 'GUI']
        for section in sections_to_ensure:
            if not config.has_section(section):
                config.add_section(section)
        
        # Update DETECTION settings
        target_color, secondary_color = app.get_current_colors()
        
        config.set('DETECTION', 'TARGET_COLOR_R', str(target_color[0]))
        config.set('DETECTION', 'TARGET_COLOR_G', str(target_color[1]))
        config.set('DETECTION', 'TARGET_COLOR_B', str(target_color[2]))
        config.set('DETECTION', 'SECONDARY_COLOR_R', str(secondary_color[0]))
        config.set('DETECTION', 'SECONDARY_COLOR_G', str(secondary_color[1]))
        config.set('DETECTION', 'SECONDARY_COLOR_B', str(secondary_color[2]))
        config.set('DETECTION', 'TOLERANCE', str(app.tolerance_var.get()))
        
        # Update TIMING settings
        config.set('TIMING', 'CHECK_INTERVAL', str(float(app.check_interval_var.get())))
        
        # Update BEHAVIOR settings
        config.set('BEHAVIOR', 'ALT_TAB_AFTER_CLICK', str(app.alt_tab_var.get()).lower())
        config.set('BEHAVIOR', 'RESET_CURSOR_POSITION', str(app.reset_cursor_var.get()).lower())
        config.set('BEHAVIOR', 'FORCE_CURSOR_TO_MONITOR', str(app.force_cursor_var.get()).lower())
        
        # Update DEBUG settings
        config.set('DEBUG', 'DEBUG_LOGGING', str(app.debug_logging_var.get()).lower())
        
        # Update GUI settings
        if app.selected_monitor:
            config.set('GUI', 'SELECTED_MONITOR', app.selected_monitor['name'])
        config.set('GUI', 'RESOLUTION', app.resolution_var.get())
        config.set('GUI', 'DARK_MODE', str(app.dark_mode_var.get()).lower())
        
        try:
            with open(app.gui_settings_file, 'w') as f:
                config.write(f)
            print("All settings saved successfully!")
            if show_message:
                messagebox.showinfo("Success", "All settings saved successfully!")
        except Exception as e:
            print(f"Warning: Could not save settings: {e}")
            if show_message:
                messagebox.showerror("Error", f"Could not save settings: {e}")