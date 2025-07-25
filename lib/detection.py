from logger import debug_log
from scaling_utils import apply_scaling

def color_match(c1, c2, tol):
    """Check if two colors match within tolerance"""
    return all(abs(a - b) <= tol for a, b in zip(c1, c2))

def check_secondary_color(screenshot, center_x, center_y, secondary_color, tolerance, search_area_size, used_mss):
    """Check if secondary color exists in search area around center point"""
    half_size = search_area_size // 2
    
    # Calculate search boundaries
    start_x = max(0, center_x - half_size)
    end_x = min(screenshot.size[0], center_x + half_size)
    start_y = max(0, center_y - half_size)
    end_y = min(screenshot.size[1], center_y + half_size)
    
    debug_log(f"Secondary color search area: X{start_x}-{end_x}, Y{start_y}-{end_y}")
    debug_log(f"Center point: X{center_x}, Y{center_y}")
    debug_log(f"Screenshot method: {'mss' if used_mss else 'pyautogui'}")
    
    # Search for secondary color in the area
    colors_found = []
    for x in range(start_x, end_x, 2):  # Step by 2 for faster scanning
        for y in range(start_y, end_y, 2):
            try:
                pixel_color = screenshot.getpixel((x, y))
                colors_found.append(pixel_color)
                if color_match(pixel_color, secondary_color, tolerance):
                    debug_log(f"Found secondary color at X{x}, Y{y}: {pixel_color}")
                    return True
            except (IndexError, OSError):
                continue
    
    # Show some sample colors for debugging
    if colors_found:
        sample_colors = colors_found[::len(colors_found)//5] if len(colors_found) > 5 else colors_found
        debug_log(f"Sample colors in search area: {sample_colors[:5]}")
    debug_log("Secondary color not found in search area")
    return False

def calculate_click_coordinates(x, check_row_relative, monitor_offset_x, monitor_offset_y, used_mss):
    """Calculate click coordinates based on screenshot method and scaling"""
    if used_mss:
        # MSS: screenshot is cropped to the specific monitor
        # Apply scaling and add monitor offset for absolute coordinates
        scaled_x, scaled_y = apply_scaling(x, check_row_relative)
        click_x = scaled_x + monitor_offset_x
        click_y = scaled_y + monitor_offset_y
        screenshot_x = x  # For secondary color check
        screenshot_y = check_row_relative
    else:
        # pyautogui: screenshot is the entire desktop
        # Coordinates are already absolute
        abs_x = x + monitor_offset_x
        abs_y = check_row_relative + monitor_offset_y
        click_x = abs_x
        click_y = abs_y
        screenshot_x = abs_x  # For secondary color check
        screenshot_y = abs_y
    
    return click_x, click_y, screenshot_x, screenshot_y

def detect_button(screenshot, used_mss, detection_settings, monitor_settings):
    """
    Main button detection function
    
    Args:
        screenshot: PIL Image object
        used_mss: Boolean indicating if MSS was used for screenshot
        detection_settings: Dict with detection parameters
        monitor_settings: Dict with monitor parameters
    
    Returns:
        Tuple: (found, click_x, click_y) where found is boolean and coordinates are for clicking
    """
    # Extract settings
    x_start_relative = detection_settings['x_start_relative']
    x_end_relative = detection_settings['x_end_relative']
    check_row_relative = detection_settings['check_row_relative']
    target_color = detection_settings['target_color']
    secondary_color = detection_settings['secondary_color']
    tolerance = detection_settings['tolerance']
    search_area_size = detection_settings['search_area_size']
    
    monitor_offset_x = monitor_settings['monitor_offset_x']
    monitor_offset_y = monitor_settings['monitor_offset_y']
    
    # Scan from right to left
    for x in range(x_end_relative - 1, x_start_relative - 1, -1):
        try:
            # Get pixel color based on screenshot method
            if used_mss:
                pixel_color = screenshot.getpixel((x, check_row_relative))
            else:
                abs_x = x + monitor_offset_x
                abs_y = check_row_relative + monitor_offset_y
                pixel_color = screenshot.getpixel((abs_x, abs_y))
            
            # Check if target color matches
            if color_match(pixel_color, target_color, tolerance):
                debug_log(f"Found target color at relative X{x}, Y{check_row_relative}: {pixel_color}")
                
                # Calculate coordinates for secondary color check
                click_x, click_y, screenshot_x, screenshot_y = calculate_click_coordinates(
                    x, check_row_relative, monitor_offset_x, monitor_offset_y, used_mss
                )
                
                # Check for secondary color using appropriate coordinates
                secondary_found = check_secondary_color(
                    screenshot, screenshot_x, screenshot_y, secondary_color, 
                    tolerance, search_area_size, used_mss
                )
                
                if secondary_found:
                    debug_log("Secondary color confirmed! Button detected.")
                    debug_log(f"Click coordinates: ({click_x}, {click_y})")
                    debug_log(f"Monitor offset: ({monitor_offset_x}, {monitor_offset_y})")
                    debug_log(f"Relative coordinates: ({x}, {check_row_relative})")
                    debug_log(f"Used MSS: {used_mss}")
                    
                    return True, click_x, click_y
                else:
                    debug_log("Target color found but secondary color not detected")
        except (IndexError, OSError):
            # Skip pixels that are out of bounds
            continue
    
    # No button found
    return False, 0, 0