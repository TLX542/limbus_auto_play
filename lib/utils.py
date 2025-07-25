import keyboard
import time


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

"""
Centralized output utilities for consistent logging and console output
"""

from .logger import debug_log
from .library_checker import is_available

def display_configuration(settings, selected_monitor, screen_width, screen_height, 
                         monitor_offset_x, monitor_offset_y, to_console=True, to_log=False):
    """
    Display configuration information to console and/or log
    
    Args:
        settings: Dict with all settings
        selected_monitor: Monitor dictionary
        screen_width, screen_height: Resolution
        monitor_offset_x, monitor_offset_y: Monitor position
        to_console: Whether to print to console
        to_log: Whether to log to debug file
    """
    
    info_lines = [
        "====== Limbus Company Auto Player ======",
        "Settings loaded from settings.ini",
        f"Selected monitor: {selected_monitor['name']}",
        f"Monitor resolution: {screen_width}x{screen_height}",
        f"Monitor position: {monitor_offset_x}, {monitor_offset_y}",
        f"Windows mouse API available: {'Yes' if is_available('windows_mouse') else 'No'}",
        f"MSS library available: {'Yes' if is_available('mss') else 'No (install with: pip install mss)'}",
        f"Detection row: {settings['check_row_relative']} ({settings['check_row_percentage']:.2f}% from top)",
        f"Detection range: X{settings['x_start_relative']}-{settings['x_end_relative']} (right to left scan)",
        f"Target color: RGB{settings['target_color']}",
        f"Secondary color: RGB{settings['secondary_color']}",
        f"Tolerance: {settings['tolerance']}",
        f"Check interval: {settings['check_interval']}s",
        f"Alt+Tab after click: {'Enabled' if settings['alt_tab_after_click'] else 'Disabled'}",
        f"Reset cursor position: {'Enabled' if settings['reset_cursor_position'] else 'Disabled'}",
        f"Force cursor to monitor: {'Enabled' if settings['force_cursor_to_monitor'] else 'Disabled'}",
        f"Debug logging: {'Enabled (log.txt)' if settings['debug_logging'] else 'Disabled'}",
        "Press 'P' to stop during operation.",
        "=" * 50
    ]
    
    if to_console:
        print("\n" + "\n".join(info_lines))
    
    if to_log and settings['debug_logging']:
        debug_log("=== CONFIGURATION ===")
        debug_log(f"Selected monitor: {selected_monitor}")
        debug_log(f"Screen resolution: {screen_width}x{screen_height}")
        debug_log(f"Monitor offset: {monitor_offset_x}, {monitor_offset_y}")
        debug_log(f"Detection row: {settings['check_row_relative']} ({settings['check_row_percentage']:.2f}%)")
        debug_log(f"Detection range: X{settings['x_start_relative']}-{settings['x_end_relative']}")
        debug_log(f"Target color: {settings['target_color']}")
        debug_log(f"Secondary color: {settings['secondary_color']}")
        debug_log(f"Tolerance: {settings['tolerance']}")
        debug_log(f"Search area size: {settings['search_area_size']}")
        debug_log("=== STARTING DETECTION LOOP ===")