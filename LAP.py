#!/usr/bin/env python3
"""
Limbus Company Auto Player - Main Application

This is the main entry point for the Limbus Company automation script.
It coordinates all the modules to detect and click the Win Rate button.
"""

import time
import keyboard

# Import our custom modules
from lib.config import load_settings
from lib.monitor import select_monitor, get_monitor_resolution
from lib.mouse import smart_click
from lib.screenshot import take_monitor_screenshot
from lib.detection import detect_button
from lib.logger import setup_logging, debug_log
from lib.utils import should_stop, interruptible_sleep, display_configuration
from lib.scaling_utils import get_scaling_factor

def handle_button_click(click_x, click_y, selected_monitor, settings):
    """Handle the button click and post-click actions"""
    # Use the unified smart click function
    smart_click(
        click_x, click_y,
        target_monitor=selected_monitor,
        force_cursor_to_monitor=settings['force_cursor_to_monitor'],
        restore_cursor=settings['reset_cursor_position']
    )
    
    time.sleep(0.1) 
    keyboard.press_and_release('enter')
    
    # Optional Alt+Tab to switch away from game
    if settings['alt_tab_after_click']:
        time.sleep(0.2)
        keyboard.press_and_release('alt+tab')

def main():
    """Main application loop"""
    try:
        # Load configuration
        base_settings = load_settings()
        
        # Multi-monitor setup
        selected_monitor = select_monitor()
        screen_width, screen_height = get_monitor_resolution(selected_monitor)
        scaling_factor = get_scaling_factor()
        
        # Store monitor offset for coordinate calculations
        monitor_offset_x = selected_monitor['x']
        monitor_offset_y = selected_monitor['y']
        
        # Calculate resolution-dependent settings
        check_row_relative = int((base_settings['check_row_percentage'] / 100) * screen_height)
        
        x_start_from_center = base_settings['x_start_from_center']
        if x_start_from_center == -1:
            x_start_relative = int(screen_width / 2)
        else:
            x_start_relative = x_start_from_center
        
        x_end_at_edge = base_settings['x_end_at_edge']
        if x_end_at_edge == -1:
            x_end_relative = screen_width
        else:
            x_end_relative = x_end_at_edge
        
        # Combine all settings
        settings = {
            **base_settings,
            'check_row_relative': check_row_relative,
            'x_start_relative': x_start_relative,
            'x_end_relative': x_end_relative
        }
        
        # Setup logging after we have the debug setting
        setup_logging(settings['debug_logging'], settings['script_dir'])
        
        # Display configuration (both console and log if debug enabled)
        display_configuration(
            settings, selected_monitor, screen_width, screen_height, 
            monitor_offset_x, monitor_offset_y, 
            to_console=True, to_log=settings['debug_logging']
        )
        
        # Prepare detection settings
        detection_settings = {
            'x_start_relative': x_start_relative,
            'x_end_relative': x_end_relative,
            'check_row_relative': check_row_relative,
            'target_color': settings['target_color'],
            'secondary_color': settings['secondary_color'],
            'tolerance': settings['tolerance'],
            'search_area_size': settings['search_area_size']
        }
        
        monitor_settings = {
            'monitor_offset_x': monitor_offset_x,
            'monitor_offset_y': monitor_offset_y
        }
        
        # Main detection loop
        scan_count = 0
        while True:
            # Check for stop condition to exit
            if should_stop():
                break
            
            scan_count += 1
            debug_log(f"Scan #{scan_count}...")
            
            # Take screenshot using appropriate method
            screenshot, used_mss = take_monitor_screenshot(selected_monitor, screen_width, screen_height)
            
            # Detect the button (removed scaling_factor parameter as it's now handled internally)
            button_found, click_x, click_y = detect_button(
                screenshot, used_mss, detection_settings, monitor_settings
            )
            
            if button_found:
                debug_log("Button clicked successfully!")
                handle_button_click(click_x, click_y, selected_monitor, settings)
            else:
                debug_log("Win Rate button not detected in this scan")
            
            # Interruptible sleep that can be stopped by key press
            if interruptible_sleep(settings['check_interval']):
                break
                
        debug_log("Stopped by key press (P). Goodbye!")
        print("Stopped by key press (P).\nGoodbye!")
        
    except KeyboardInterrupt:
        debug_log("Stopped by user interrupt (Ctrl+C)")
        print("Stopped by user.")
        input("Press Enter to exit...")
    except Exception as e:
        debug_log(f"Exited with error: {e}")
        print(f"Exited with error: {e}")
        input("Please report this issue on GitHub: https://github.com/TLX542/limbus_auto_play/issues\nPress Enter to exit...")

if __name__ == "__main__":
    main()