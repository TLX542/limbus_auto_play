"""
Limbus Company Auto Player - Theme Manager

Handles dark/light mode theming for the application.
"""
import tkinter as tk
from tkinter import ttk

class ThemeManager:
    def __init__(self, app):
        self.app = app
        self.setup_themes()
    
    def setup_themes(self):
        """Set up light and dark themes"""
        style = ttk.Style()
        
        # Define color schemes
        self.light_theme = {
            'bg': '#ffffff',
            'fg': '#000000',
            'select_bg': '#0078d4',
            'select_fg': '#ffffff',
            'field_bg': '#ffffff',
            'field_fg': '#000000',
            'button_bg': '#f0f0f0',
            'button_fg': '#000000',
            'frame_bg': '#f0f0f0',
            'entry_bg': '#ffffff',
            'entry_fg': '#000000',
            'text_bg': '#ffffff',
            'text_fg': '#000000',
            'label_fg': '#000000',
            'disabled_fg': '#666666'
        }
        
        self.dark_theme = {
            'bg': '#1a1a1a',  # Darker main background
            'fg': '#ffffff',
            'select_bg': '#0d7377',
            'select_fg': '#ffffff',
            'field_bg': '#2d2d2d',  # Darker field background
            'field_fg': '#ffffff',
            'button_bg': '#2d2d2d',  # Darker button background
            'button_fg': '#ffffff',
            'frame_bg': '#1a1a1a',  # Darker frame background
            'entry_bg': '#2d2d2d',  # Darker entry background
            'entry_fg': '#ffffff',
            'text_bg': '#121212',  # Much darker text background
            'text_fg': '#ffffff',
            'label_fg': '#ffffff',
            'disabled_fg': '#888888',
            'info_text_fg': '#87ceeb',  # Light blue for info text
            'link_fg': '#66b3ff',  # Lighter blue for links
            'success_fg': '#90ee90',  # Light green for success messages
            'warning_fg': '#ffd700',  # Gold for warnings
            'error_fg': '#ff6b6b'  # Light red for errors
        }
        
        # Configure light theme
        style.theme_create("light_theme", parent="clam", settings={
            "TLabel": {
                "configure": {"background": self.light_theme['bg'], "foreground": self.light_theme['label_fg']}
            },
            "TButton": {
                "configure": {"background": self.light_theme['button_bg'], "foreground": self.light_theme['button_fg']},
                "map": {
                    "background": [("active", "#e1e1e1"), ("pressed", "#d0d0d0")],
                    "foreground": [("active", self.light_theme['button_fg'])]
                }
            },
            "TFrame": {
                "configure": {"background": self.light_theme['frame_bg']}
            },
            "TLabelFrame": {
                "configure": {"background": self.light_theme['frame_bg'], "foreground": self.light_theme['label_fg']}
            },
            "TLabelFrame.Label": {
                "configure": {"background": self.light_theme['frame_bg'], "foreground": self.light_theme['label_fg']}
            },
            "TEntry": {
                "configure": {"fieldbackground": self.light_theme['entry_bg'], "foreground": self.light_theme['entry_fg'],
                             "bordercolor": "#cccccc", "lightcolor": "#ffffff", "darkcolor": "#cccccc"}
            },
            "TCombobox": {
                "configure": {"fieldbackground": self.light_theme['entry_bg'], "foreground": self.light_theme['entry_fg'],
                             "bordercolor": "#cccccc", "arrowcolor": self.light_theme['entry_fg']}
            },
            "TSpinbox": {
                "configure": {"fieldbackground": self.light_theme['entry_bg'], "foreground": self.light_theme['entry_fg'],
                             "bordercolor": "#cccccc", "arrowcolor": self.light_theme['entry_fg']}
            },
            "TCheckbutton": {
                "configure": {"background": self.light_theme['bg'], "foreground": self.light_theme['fg']}
            },
            "TNotebook": {
                "configure": {"background": self.light_theme['bg'], "bordercolor": "#cccccc"}
            },
            "TNotebook.Tab": {
                "configure": {"background": "#e1e1e1", "foreground": self.light_theme['fg']},
                "map": {
                    "background": [("selected", self.light_theme['bg']), ("active", "#f0f0f0")],
                    "foreground": [("selected", self.light_theme['fg'])]
                }
            }
        })
        
        # Configure dark theme
        style.theme_create("dark_theme", parent="clam", settings={
            "TLabel": {
                "configure": {"background": self.dark_theme['bg'], "foreground": self.dark_theme['label_fg']}
            },
            "TButton": {
                "configure": {"background": self.dark_theme['button_bg'], "foreground": self.dark_theme['button_fg'],
                             "bordercolor": "#404040", "lightcolor": "#404040", "darkcolor": "#1a1a1a"},
                "map": {
                    "background": [("active", "#3d3d3d"), ("pressed", "#252525")],
                    "foreground": [("active", self.dark_theme['button_fg'])]
                }
            },
            "TFrame": {
                "configure": {"background": self.dark_theme['frame_bg']}
            },
            "TLabelFrame": {
                "configure": {"background": self.dark_theme['frame_bg'], "foreground": self.dark_theme['label_fg'],
                             "bordercolor": "#404040", "lightcolor": "#404040", "darkcolor": "#1a1a1a"}
            },
            "TLabelFrame.Label": {
                "configure": {"background": self.dark_theme['frame_bg'], "foreground": self.dark_theme['label_fg']}
            },
            "TEntry": {
                "configure": {"fieldbackground": self.dark_theme['entry_bg'], "foreground": self.dark_theme['entry_fg'],
                             "bordercolor": "#404040", "lightcolor": "#505050", "darkcolor": "#1a1a1a",
                             "insertcolor": self.dark_theme['entry_fg']}
            },
            "TCombobox": {
                "configure": {"fieldbackground": self.dark_theme['entry_bg'], "foreground": self.dark_theme['entry_fg'],
                             "bordercolor": "#404040", "arrowcolor": self.dark_theme['entry_fg'],
                             "lightcolor": "#505050", "darkcolor": "#1a1a1a"}
            },
            "TSpinbox": {
                "configure": {"fieldbackground": self.dark_theme['entry_bg'], "foreground": self.dark_theme['entry_fg'],
                             "bordercolor": "#404040", "arrowcolor": self.dark_theme['entry_fg'],
                             "lightcolor": "#505050", "darkcolor": "#1a1a1a"}
            },
            "TCheckbutton": {
                "configure": {"background": self.dark_theme['bg'], "foreground": self.dark_theme['fg'],
                             "focuscolor": "#0d7377"}
            },
            "TNotebook": {
                "configure": {"background": self.dark_theme['bg'], "bordercolor": "#404040"}
            },
            "TNotebook.Tab": {
                "configure": {"background": "#2d2d2d", "foreground": self.dark_theme['fg'],
                             "bordercolor": "#404040"},
                "map": {
                    "background": [("selected", self.dark_theme['bg']), ("active", "#3d3d3d")],
                    "foreground": [("selected", self.dark_theme['fg'])]
                }
            }
        })
    
    def apply_theme(self, is_dark_mode):
        """Apply the selected theme"""
        style = ttk.Style()
        
        if is_dark_mode:
            theme = self.dark_theme
            style.theme_use("dark_theme")
        else:
            theme = self.light_theme
            style.theme_use("light_theme")
        
        # Apply theme to root window
        self.app.root.configure(bg=theme['bg'])
        
        # Apply theme to custom widgets (ScrolledText, etc.)
        self.apply_custom_widget_theme(theme)
    
    def apply_custom_widget_theme(self, theme):
        """Apply theme to custom widgets that don't use ttk styles"""
        # Update ScrolledText widgets
        if hasattr(self.app, 'control_tab') and hasattr(self.app.control_tab, 'status_text'):
            self.app.control_tab.status_text.configure(
                bg=theme['text_bg'],
                fg=theme['text_fg'],
                insertbackground=theme['text_fg'],
                selectbackground=theme['select_bg'],
                selectforeground=theme['select_fg']
            )
        
        if hasattr(self.app, 'status_tab') and hasattr(self.app.status_tab, 'log_text'):
            self.app.status_tab.log_text.configure(
                bg=theme['text_bg'],
                fg=theme['text_fg'],
                insertbackground=theme['text_fg'],
                selectbackground=theme['select_bg'],
                selectforeground=theme['select_fg']
            )
        
        # Update info text colors in display tab
        self.update_info_text_colors(theme)
    
    def update_info_text_colors(self, theme):
        """Update colored info text to be theme-appropriate"""
        if hasattr(self.app, 'display_tab') and hasattr(self.app.display_tab, 'resolution_frame'):
            # Find and update info labels in the resolution frame
            for widget in self.app.display_tab.resolution_frame.winfo_children():
                if isinstance(widget, ttk.Frame):
                    for child in widget.winfo_children():
                        if isinstance(child, ttk.Label):
                            text = child.cget('text')
                            if 'DPI scaling' in text:
                                # Info text - use light blue in dark mode
                                if theme == self.dark_theme:
                                    child.configure(foreground=theme['info_text_fg'])
                                else:
                                    child.configure(foreground='blue')
                            elif 'resolution matches' in text and 'native' in text:
                                # Normal text - use default
                                child.configure(foreground=theme['label_fg'])
                            elif 'detection fails' in text:
                                # Gray text - use appropriate gray
                                if theme == self.dark_theme:
                                    child.configure(foreground='#aaaaaa')
                                else:
                                    child.configure(foreground='gray')
        
        # Update control tab hotkey info
        if hasattr(self.app, 'control_tab') and hasattr(self.app.control_tab, 'frame'):
            self.update_control_tab_colors(theme)
    
    def update_control_tab_colors(self, theme):
        """Update colored text in control tab"""
        # This method will recursively find and update colored labels
        def update_widget_colors(widget):
            if isinstance(widget, ttk.Label):
                text = widget.cget('text')
                if 'Press \'P\' anywhere' in text:
                    # Info text - use appropriate color
                    if theme == self.dark_theme:
                        widget.configure(foreground=theme['info_text_fg'])
                    else:
                        widget.configure(foreground='blue')
            
            # Recursively check children
            try:
                for child in widget.winfo_children():
                    update_widget_colors(child)
            except:
                pass
        
        if hasattr(self.app, 'control_tab'):
            update_widget_colors(self.app.control_tab.frame)
    
    def get_text_color_for_type(self, text_type, is_dark_mode):
        """Get appropriate text color for different text types"""
        if is_dark_mode:
            theme = self.dark_theme
            color_map = {
                'info': theme['info_text_fg'],
                'link': theme['link_fg'],
                'success': theme['success_fg'],
                'warning': theme['warning_fg'],
                'error': theme['error_fg'],
                'normal': theme['label_fg'],
                'disabled': theme['disabled_fg']
            }
        else:
            color_map = {
                'info': 'blue',
                'link': 'blue',
                'success': 'green',
                'warning': 'orange',
                'error': 'red',
                'normal': 'black',
                'disabled': 'gray'
            }
        
        return color_map.get(text_type, color_map['normal'])