from .logger import debug_log

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

def detect_button(screenshot, used_mss, detection_settings, monitor_settings, resolution_info=None):
    """
    Main button detection function with simplified coordinate logic
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
    
    # Get resolution info
    if resolution_info:
        monitor_width = resolution_info.get('monitor_width', 0)
        monitor_height = resolution_info.get('monitor_height', 0)
        screen_width = resolution_info.get('screen_width', 0)
        screen_height = resolution_info.get('screen_height', 0)
    else:
        monitor_width = screen_width = screenshot.size[0]
        monitor_height = screen_height = screenshot.size[1]
    
    debug_log(f"=== DETECTION START ===")
    debug_log(f"Screenshot size: {screenshot.size[0]}x{screenshot.size[1]}")
    debug_log(f"Monitor: {monitor_width}x{monitor_height} at offset ({monitor_offset_x}, {monitor_offset_y})")
    debug_log(f"Screen resolution: {screen_width}x{screen_height}")
    debug_log(f"Search range: X{x_start_relative}-{x_end_relative}, Y{check_row_relative}")
    debug_log(f"Screenshot method: {'MSS (cropped)' if used_mss else 'PyAutoGUI (full desktop)'}")
    
    # Determine if we need to apply scaling
    needs_scaling = (monitor_width != screen_width or monitor_height != screen_height)
    if needs_scaling:
        scale_x = monitor_width / screen_width
        scale_y = monitor_height / screen_height
        debug_log(f"Scaling needed: scale_x={scale_x}, scale_y={scale_y}")
    else:
        scale_x = scale_y = 1.0
        debug_log("No scaling needed - monitor matches screen resolution")
    
    # Scan from right to left
    for x in range(x_end_relative - 1, x_start_relative - 1, -1):
        try:
            # Get pixel color based on screenshot method
            if used_mss:
                # MSS: coordinates are within the cropped screenshot
                if x >= screenshot.size[0] or check_row_relative >= screenshot.size[1]:
                    continue
                pixel_color = screenshot.getpixel((x, check_row_relative))
                pixel_location_desc = f"MSS screenshot coords ({x}, {check_row_relative})"
            else:
                # pyautogui: need absolute coordinates for full desktop screenshot
                abs_x = x + monitor_offset_x
                abs_y = check_row_relative + monitor_offset_y
                if abs_x >= screenshot.size[0] or abs_y >= screenshot.size[1] or abs_x < 0 or abs_y < 0:
                    continue
                pixel_color = screenshot.getpixel((abs_x, abs_y))
                pixel_location_desc = f"PyAutoGUI desktop coords ({abs_x}, {abs_y})"
            
            # Check if target color matches
            if color_match(pixel_color, target_color, tolerance):
                debug_log(f"Found target color at {pixel_location_desc}: {pixel_color}")
                
                # Calculate click coordinates
                if used_mss:
                    # MSS: apply scaling to screenshot coordinates, then add monitor offset
                    if needs_scaling:
                        scaled_x = x * scale_x
                        scaled_y = check_row_relative * scale_y
                        click_x = int(scaled_x) + monitor_offset_x
                        click_y = int(scaled_y) + monitor_offset_y
                        debug_log(f"MSS with scaling: ({x}, {check_row_relative}) -> scaled({scaled_x}, {scaled_y}) -> final({click_x}, {click_y})")
                    else:
                        click_x = x + monitor_offset_x
                        click_y = check_row_relative + monitor_offset_y
                        debug_log(f"MSS no scaling: ({x}, {check_row_relative}) -> final({click_x}, {click_y})")
                    
                    # Secondary color check uses screenshot coordinates
                    screenshot_x = x
                    screenshot_y = check_row_relative
                    
                else:
                    # pyautogui: apply scaling to relative coordinates, then add monitor offset
                    if needs_scaling:
                        scaled_x = x * scale_x
                        scaled_y = check_row_relative * scale_y
                        click_x = int(scaled_x) + monitor_offset_x
                        click_y = int(scaled_y) + monitor_offset_y
                        debug_log(f"PyAutoGUI with scaling: relative({x}, {check_row_relative}) -> scaled({scaled_x}, {scaled_y}) -> final({click_x}, {click_y})")
                    else:
                        click_x = x + monitor_offset_x
                        click_y = check_row_relative + monitor_offset_y
                        debug_log(f"PyAutoGUI no scaling: relative({x}, {check_row_relative}) -> final({click_x}, {click_y})")
                    
                    # Secondary color check uses absolute coordinates in full desktop screenshot
                    screenshot_x = x + monitor_offset_x
                    screenshot_y = check_row_relative + monitor_offset_y
                
                # Validate click coordinates
                debug_log(f"Click coordinates validation:")
                debug_log(f"  - Target monitor bounds: X{monitor_offset_x}-{monitor_offset_x + monitor_width}, Y{monitor_offset_y}-{monitor_offset_y + monitor_height}")
                debug_log(f"  - Click coordinates: ({click_x}, {click_y})")
                debug_log(f"  - Within monitor bounds: X={monitor_offset_x <= click_x <= monitor_offset_x + monitor_width}, Y={monitor_offset_y <= click_y <= monitor_offset_y + monitor_height}")
                
                # Check for secondary color
                secondary_found = check_secondary_color(
                    screenshot, screenshot_x, screenshot_y, secondary_color, 
                    tolerance, search_area_size, used_mss
                )
                
                if secondary_found:
                    debug_log("✅ Secondary color confirmed! Button detected.")
                    debug_log(f"🎯 FINAL CLICK COORDINATES: ({click_x}, {click_y})")
                    return True, click_x, click_y
                else:
                    debug_log("❌ Target color found but secondary color not detected")
                    
        except (IndexError, OSError) as e:
            debug_log(f"Pixel access error: {e}")
            continue
    
    # No button found
    debug_log("❌ No button found in scan")
    return False, 0, 0