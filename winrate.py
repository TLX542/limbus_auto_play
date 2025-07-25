import pyautogui
import keyboard
import time
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
        
        # Get screen dimensions
        screen_width, screen_height = pyautogui.size()
        
        # Load detection settings - now using percentage
        check_row_percentage = config.getfloat('DETECTION', 'CHECK_ROW_PERCENTAGE', fallback=74.17)
        check_row = int((check_row_percentage / 100) * screen_height)
        
        x_start_from_center = config.getint('DETECTION', 'X_START_FROM_CENTER', fallback=-1)
        x_start = int(screen_width / 2) if x_start_from_center == -1 else x_start_from_center
        
        x_end_at_edge = config.getint('DETECTION', 'X_END_AT_EDGE', fallback=-1)
        x_end = screen_width if x_end_at_edge == -1 else x_end_at_edge
        
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
        tolerance = config.getint('DETECTION', 'TOLERANCE', fallback=10)
        search_area_size = config.getint('DETECTION', 'SEARCH_AREA_SIZE', fallback=50)
        
        # Load timing settings
        check_interval = config.getint('TIMING', 'CHECK_INTERVAL', fallback=2)
        
        # Load behavior settings
        alt_tab_after_click = config.getboolean('BEHAVIOR', 'ALT_TAB_AFTER_CLICK', fallback=False)
        reset_cursor_position = config.getboolean('BEHAVIOR', 'RESET_CURSOR_POSITION', fallback=True)
        
        return {
            'screen_width': screen_width,
            'screen_height': screen_height,
            'check_row': check_row,
            'check_row_percentage': check_row_percentage,
            'x_start': x_start,
            'x_end': x_end,
            'target_color': target_color,
            'secondary_color': secondary_color,
            'tolerance': tolerance,
            'search_area_size': search_area_size,
            'check_interval': check_interval,
            'alt_tab_after_click': alt_tab_after_click,
            'reset_cursor_position': reset_cursor_position
        }
        
    except Exception as e:
        print(f"Error reading settings.ini: {e}")
        print("Please check your settings.ini file for errors.")
        input("Press Enter to exit...")
        sys.exit(1)

# Load all settings from settings.ini
settings = load_settings()

# Extract settings for easier access
screen_width = settings['screen_width']
screen_height = settings['screen_height']
CHECK_ROW = settings['check_row']
CHECK_ROW_PERCENTAGE = settings['check_row_percentage']
X_START = settings['x_start']
X_END = settings['x_end']
TARGET_COLOR = settings['target_color']
SECONDARY_COLOR = settings['secondary_color']
TOLERANCE = settings['tolerance']
SEARCH_AREA_SIZE = settings['search_area_size']
CHECK_INTERVAL = settings['check_interval']
ALT_TAB_AFTER_CLICK = settings['alt_tab_after_click']
RESET_CURSOR_POSITION = settings['reset_cursor_position']

def color_match(c1, c2, tol):
    return all(abs(a - b) <= tol for a, b in zip(c1, c2))

def check_secondary_color(screenshot, center_x, center_y):
    """Check if secondary color exists in 50x50 area around center point"""
    half_size = SEARCH_AREA_SIZE // 2
    
    # Calculate search boundaries (ensure we don't go outside screen)
    start_x = max(0, center_x - half_size)
    end_x = min(screen_width, center_x + half_size)
    start_y = max(0, center_y - half_size)
    end_y = min(screen_height, center_y + half_size)
    
    # Search for secondary color in the area
    for x in range(start_x, end_x):
        for y in range(start_y, end_y):
            pixel_color = screenshot.getpixel((x, y))
            if color_match(pixel_color, SECONDARY_COLOR, TOLERANCE):
                return True
    return False

def should_stop():
    """Check if 'p' key is pressed"""
    return keyboard.is_pressed('p')

def interruptible_sleep(duration):
    """Sleep for duration seconds, but check for key presses every 0.1 seconds"""
    end_time = time.time() + duration
    while time.time() < end_time:
        if should_stop():
            return True  # Signal that we should stop
        time.sleep(0.1)
    return False

try:
    print("====== Limbus Company Auto Player ======")
    print("Settings loaded from settings.ini")
    print(f"Screen resolution: {screen_width}x{screen_height}")
    print(f"Detection area: X{X_END}-{X_START} (right to left), Y{CHECK_ROW} ({CHECK_ROW_PERCENTAGE:.2f}% from top)")
    print(f"Target color: RGB{TARGET_COLOR}")
    print(f"Secondary color: RGB{SECONDARY_COLOR}")
    print(f"Tolerance: {TOLERANCE}")
    print(f"Check interval: {CHECK_INTERVAL}s")
    print(f"Alt+Tab after click: {'Enabled' if ALT_TAB_AFTER_CLICK else 'Disabled'}")
    print(f"Reset cursor position: {'Enabled' if RESET_CURSOR_POSITION else 'Disabled'}")
    print("Press 'P' to stop.")
    print("=" * 40)
    while True:
        # Check for stop condition to exit
        if should_stop():
            break
            
        screenshot = pyautogui.screenshot()
        # Changed to scan from right to left (X_END-1 down to X_START, step -1)
        for x in range(X_END - 1, X_START - 1, -1):
            pixel_color = screenshot.getpixel((x, CHECK_ROW))
            if color_match(pixel_color, TARGET_COLOR, TOLERANCE):
                # First color found, now check for secondary color in surrounding area
                if check_secondary_color(screenshot, x, CHECK_ROW):
                    # Save current cursor position (if we need to restore it later)
                    if RESET_CURSOR_POSITION:
                        original_x, original_y = pyautogui.position()
                    
                    # Move cursor to the found location and left click
                    pyautogui.moveTo(x, CHECK_ROW)
                    time.sleep(0.1)  # Small delay to ensure cursor movement
                    pyautogui.click(x, CHECK_ROW)
                    time.sleep(0.1) 
                    keyboard.press_and_release('enter')
                    
                    # Optional Alt+Tab to switch away from game
                    if ALT_TAB_AFTER_CLICK:
                        time.sleep(0.2)  # Small delay before Alt+Tab
                        keyboard.press_and_release('alt+tab')

                    # Restore cursor to original position (if enabled)
                    if RESET_CURSOR_POSITION:
                        pyautogui.moveTo(original_x, original_y)
                    else:
                        pyautogui.moveTo(25, 25)
                    break
        
        # Interruptible sleep that can be stopped by key press
        if interruptible_sleep(CHECK_INTERVAL):
            break
            
    print("Stopped by key press (P).\nGoodbye!")
except KeyboardInterrupt:
    print("Stopped by user.")
    input("Press Enter to exit...")
except Exception as e:
    print(f"Exited with error: {e}")
    input("Please report this issue on GitHub: https://github.com/TLX542/limbus_auto_play/issues\nPress Enter to exit...")