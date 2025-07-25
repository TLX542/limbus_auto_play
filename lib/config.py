import configparser
import os
import sys


def load_settings():
    """Load settings from settings.ini file"""
    config = configparser.ConfigParser()
    
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    settings_file = os.path.join(script_dir, 'settings.ini')
    
    # Check if settings.ini exists
    if not os.path.exists(settings_file):
        print(f"Error: settings.ini not found!")
        print(f"Looking for: {settings_file}")
        print("Please ensure settings.ini is in the same directory as this script.")
        input("Press Enter to exit...")
        sys.exit(1)
    
    try:
        config.read(settings_file)
        
        # Load debug setting first
        debug_logging = config.getboolean('DEBUG', 'DEBUG_LOGGING', fallback=False)
        
        # Load colors
        target_r = config.getint('DETECTION', 'TARGET_COLOR_R', fallback=59)
        target_g = config.getint('DETECTION', 'TARGET_COLOR_G', fallback=1)
        target_b = config.getint('DETECTION', 'TARGET_COLOR_B', fallback=0)
        target_color = (target_r, target_g, target_b)
        
        secondary_r = config.getint('DETECTION', 'SECONDARY_COLOR_R', fallback=246)
        secondary_g = config.getint('DETECTION', 'SECONDARY_COLOR_G', fallback=175)
        secondary_b = config.getint('DETECTION', 'SECONDARY_COLOR_B', fallback=100)
        secondary_color = (secondary_r, secondary_g, secondary_b)
        
        # Load other detection settings
        check_row_percentage = config.getfloat('DETECTION', 'CHECK_ROW_PERCENTAGE', fallback=74.17)
        x_start_from_center = config.getint('DETECTION', 'X_START_FROM_CENTER', fallback=-1)
        x_end_at_edge = config.getint('DETECTION', 'X_END_AT_EDGE', fallback=-1)
        tolerance = config.getint('DETECTION', 'TOLERANCE', fallback=10)
        search_area_size = config.getint('DETECTION', 'SEARCH_AREA_SIZE', fallback=50)
        
        # Load timing settings
        check_interval = config.getint('TIMING', 'CHECK_INTERVAL', fallback=2)
        
        # Load behavior settings
        alt_tab_after_click = config.getboolean('BEHAVIOR', 'ALT_TAB_AFTER_CLICK', fallback=False)
        reset_cursor_position = config.getboolean('BEHAVIOR', 'RESET_CURSOR_POSITION', fallback=True)
        force_cursor_to_monitor = config.getboolean('BEHAVIOR', 'FORCE_CURSOR_TO_MONITOR', fallback=True)
        
        return {
            'script_dir': script_dir,
            'debug_logging': debug_logging,
            'check_row_percentage': check_row_percentage,
            'x_start_from_center': x_start_from_center,
            'x_end_at_edge': x_end_at_edge,
            'target_color': target_color,
            'secondary_color': secondary_color,
            'tolerance': tolerance,
            'search_area_size': search_area_size,
            'check_interval': check_interval,
            'alt_tab_after_click': alt_tab_after_click,
            'reset_cursor_position': reset_cursor_position,
            'force_cursor_to_monitor': force_cursor_to_monitor
        }
        
    except Exception as e:
        print(f"Error reading settings.ini: {e}")
        print("Please check your settings.ini file for errors.")
        input("Press Enter to exit...")
        sys.exit(1)