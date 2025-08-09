#!/usr/bin/env python3
"""
Enhanced settings handler that preserves comments and format

This module should be saved as 'settings_handler.py' in the same directory as LAP.pyw
"""

import os
from typing import Any

class CommentPreservingSettings:
    """Settings handler that preserves comments and formatting"""
    
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.lines = []
        self.settings = {}
        self.load()
    
    def load(self):
        """Load settings while preserving all formatting and comments"""
        self.lines = []
        self.settings = {}
        
        if not os.path.exists(self.file_path):
            # Create default settings file if it doesn't exist
            self.create_default_file()
            return
        
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                self.lines = f.readlines()
            
            current_section = None
            for line in self.lines:
                stripped = line.strip()
                
                # Skip empty lines and comments
                if not stripped or stripped.startswith('#'):
                    continue
                
                # Check for section headers
                if stripped.startswith('[') and stripped.endswith(']'):
                    current_section = stripped[1:-1].upper()
                    continue
                
                # Parse key-value pairs
                if '=' in stripped and current_section:
                    key, value = stripped.split('=', 1)
                    key = key.strip().upper()
                    value = value.strip()
                    
                    # Convert value to appropriate type
                    if current_section not in self.settings:
                        self.settings[current_section] = {}
                    
                    # Handle boolean values
                    if value.lower() in ('true', 'false'):
                        self.settings[current_section][key] = value.lower() == 'true'
                    # Handle numeric values
                    elif value.replace('.', '').replace('-', '').isdigit():
                        if '.' in value:
                            self.settings[current_section][key] = float(value)
                        else:
                            self.settings[current_section][key] = int(value)
                    else:
                        self.settings[current_section][key] = value
                        
        except Exception as e:
            print(f"Error loading settings: {e}")
            self.create_default_file()
    
    def create_default_file(self):
        """Create the default settings file with comments"""
        default_content = """[DETECTION]
# Percentage from the top of the screen to check for the Win Rate button
# Based on 1080p screen where row 801 is 74.17% from top (801/1080 * 100)
# This automatically scales to any screen resolution
CHECK_ROW_PERCENTAGE = 74.17

# X coordinate to start scanning from (0 = left edge, -1 = center of screen)
X_START_FROM_CENTER = -1

# X coordinate to end scanning at (-1 = right edge of screen)
X_END_AT_EDGE = -1

# Target color in RGB format (R,G,B) - button background color
TARGET_COLOR_R = 59
TARGET_COLOR_G = 1
TARGET_COLOR_B = 0

# Secondary color in RGB format (R,G,B) - text color
SECONDARY_COLOR_R = 246
SECONDARY_COLOR_G = 175
SECONDARY_COLOR_B = 100

# Color matching tolerance (higher = more lenient matching)
TOLERANCE = 10

# Size of the search area around the found target color in pixels
SEARCH_AREA_SIZE = 50

[TIMING]
# Seconds to wait between each scan
CHECK_INTERVAL = 1.0

[BEHAVIOR]
# Set to true to Alt+Tab after clicking (switch away from game)
ALT_TAB_AFTER_CLICK = false

# Set to true to reset cursor to original position after clicking
RESET_CURSOR_POSITION = true

# Set to true to force cursor to monitor before clicking
FORCE_CURSOR_TO_MONITOR = false

[DEBUG]
# Set to true to enable debug logging to log.txt file
DEBUG_LOGGING = false

[GUI]
# Selected monitor name for GUI
SELECTED_MONITOR = Monitor 1

# Resolution setting for GUI
RESOLUTION = 1920x1080
"""
        try:
            with open(self.file_path, 'w', encoding='utf-8') as f:
                f.write(default_content)
            self.load()  # Reload after creating
        except Exception as e:
            print(f"Error creating default settings file: {e}")
    
    def get(self, section: str, key: str, default=None):
        """Get a setting value"""
        section = section.upper()
        key = key.upper()
        return self.settings.get(section, {}).get(key, default)
    
    def set(self, section: str, key: str, value: Any):
        """Set a setting value and update the file lines"""
        section = section.upper()
        key = key.upper()
        
        # Ensure section exists in settings dict
        if section not in self.settings:
            self.settings[section] = {}
        
        self.settings[section][key] = value
        
        # Update the lines array
        self._update_line_value(section, key, value)
    
    def _update_line_value(self, section: str, key: str, value: Any):
        """Update a specific line in the lines array"""
        current_section = None
        
        for i, line in enumerate(self.lines):
            stripped = line.strip()
            
            # Track current section
            if stripped.startswith('[') and stripped.endswith(']'):
                current_section = stripped[1:-1].upper()
                continue
            
            # Look for the key in the current section
            if current_section == section and '=' in stripped:
                line_key = stripped.split('=')[0].strip().upper()
                if line_key == key:
                    # Update this line with the new value
                    indent = len(line) - len(line.lstrip())
                    if isinstance(value, bool):
                        str_value = str(value).lower()
                    else:
                        str_value = str(value)
                    
                    self.lines[i] = ' ' * indent + f"{key} = {str_value}\n"
                    return
        
        # If we get here, the key wasn't found, so add it to the section
        self._add_key_to_section(section, key, value)
    
    def _add_key_to_section(self, section: str, key: str, value: Any):
        """Add a new key to an existing section"""
        section_found = False
        insert_index = len(self.lines)
        
        for i, line in enumerate(self.lines):
            stripped = line.strip()
            
            if stripped == f"[{section}]":
                section_found = True
                # Find the end of this section
                for j in range(i + 1, len(self.lines)):
                    next_stripped = self.lines[j].strip()
                    if next_stripped.startswith('['):
                        insert_index = j
                        break
                else:
                    insert_index = len(self.lines)
                break
        
        if not section_found:
            # Add the section header and key
            self.lines.extend([f"\n[{section}]\n"])
            insert_index = len(self.lines)
        
        # Add the new key-value pair
        if isinstance(value, bool):
            str_value = str(value).lower()
        else:
            str_value = str(value)
        
        self.lines.insert(insert_index, f"{key} = {str_value}\n")
    
    def save(self):
        """Save the settings file while preserving comments and formatting"""
        try:
            with open(self.file_path, 'w', encoding='utf-8') as f:
                f.writelines(self.lines)
        except Exception as e:
            print(f"Error saving settings: {e}")
            raise


# Modified functions for the main GUI code
def load_settings_with_comments():
    """Load settings using the comment-preserving handler"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Get the parent directory
    parent_dir = os.path.dirname(script_dir)
    settings_file = os.path.join(parent_dir, 'settings.ini')
    
    # Create the comment-preserving settings handler
    settings_handler = CommentPreservingSettings(settings_file)
    
    # Convert to the format expected by the existing code
    settings = {
        'script_dir': script_dir,
        'check_row_percentage': settings_handler.get('DETECTION', 'CHECK_ROW_PERCENTAGE', 74.17),
        'x_start_from_center': settings_handler.get('DETECTION', 'X_START_FROM_CENTER', -1),
        'x_end_at_edge': settings_handler.get('DETECTION', 'X_END_AT_EDGE', -1),
        'target_color': (
            settings_handler.get('DETECTION', 'TARGET_COLOR_R', 59),
            settings_handler.get('DETECTION', 'TARGET_COLOR_G', 1),
            settings_handler.get('DETECTION', 'TARGET_COLOR_B', 0)
        ),
        'secondary_color': (
            settings_handler.get('DETECTION', 'SECONDARY_COLOR_R', 246),
            settings_handler.get('DETECTION', 'SECONDARY_COLOR_G', 175),
            settings_handler.get('DETECTION', 'SECONDARY_COLOR_B', 100)
        ),
        'tolerance': settings_handler.get('DETECTION', 'TOLERANCE', 10),
        'search_area_size': settings_handler.get('DETECTION', 'SEARCH_AREA_SIZE', 50),
        'check_interval': settings_handler.get('TIMING', 'CHECK_INTERVAL', 1.0),
        'alt_tab_after_click': settings_handler.get('BEHAVIOR', 'ALT_TAB_AFTER_CLICK', False),
        'reset_cursor_position': settings_handler.get('BEHAVIOR', 'RESET_CURSOR_POSITION', True),
        'force_cursor_to_monitor': settings_handler.get('BEHAVIOR', 'FORCE_CURSOR_TO_MONITOR', False),
        'debug_logging': settings_handler.get('DEBUG', 'DEBUG_LOGGING', False),
        'selected_monitor': settings_handler.get('GUI', 'SELECTED_MONITOR', 'Monitor 1'),
        'resolution': settings_handler.get('GUI', 'RESOLUTION', '1920x1080'),
        '_handler': settings_handler  # Keep reference to the handler
    }
    
    return settings


def save_all_settings_with_comments(gui_instance, show_message=True):
    """Save all settings while preserving comments"""
    try:
        # Get the settings handler from the loaded settings
        if '_handler' not in gui_instance.settings:
            # Fallback to old method if handler not available
            return gui_instance.save_all_settings(show_message)
        
        handler = gui_instance.settings['_handler']
        
        # Update all settings through the handler
        target_color, secondary_color = gui_instance.get_current_colors()
        
        # DETECTION settings
        handler.set('DETECTION', 'TARGET_COLOR_R', target_color[0])
        handler.set('DETECTION', 'TARGET_COLOR_G', target_color[1])
        handler.set('DETECTION', 'TARGET_COLOR_B', target_color[2])
        handler.set('DETECTION', 'SECONDARY_COLOR_R', secondary_color[0])
        handler.set('DETECTION', 'SECONDARY_COLOR_G', secondary_color[1])
        handler.set('DETECTION', 'SECONDARY_COLOR_B', secondary_color[2])
        handler.set('DETECTION', 'TOLERANCE', gui_instance.tolerance_var.get())
        
        # TIMING settings
        handler.set('TIMING', 'CHECK_INTERVAL', gui_instance.check_interval_var.get())
        
        # BEHAVIOR settings
        handler.set('BEHAVIOR', 'ALT_TAB_AFTER_CLICK', gui_instance.alt_tab_var.get())
        handler.set('BEHAVIOR', 'RESET_CURSOR_POSITION', gui_instance.reset_cursor_var.get())
        handler.set('BEHAVIOR', 'FORCE_CURSOR_TO_MONITOR', gui_instance.force_cursor_var.get())
        
        # DEBUG settings
        handler.set('DEBUG', 'DEBUG_LOGGING', gui_instance.debug_logging_var.get())
        
        # GUI settings
        if gui_instance.selected_monitor:
            handler.set('GUI', 'SELECTED_MONITOR', gui_instance.selected_monitor['name'])
        handler.set('GUI', 'RESOLUTION', gui_instance.resolution_var.get())
        
        # Save to file
        handler.save()
        
        print("All settings saved successfully with comments preserved!")
        if show_message:
            import tkinter.messagebox as messagebox
            messagebox.showinfo("Success", "All settings saved successfully!")
            
    except Exception as e:
        print(f"Error saving settings: {e}")
        if show_message:
            import tkinter.messagebox as messagebox
            messagebox.showerror("Error", f"Could not save settings: {e}")