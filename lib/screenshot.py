import pyautogui
from PIL import Image
from .logger import debug_log
from .library_checker import is_available

# Import mss if available
if is_available('mss'):
    from mss import mss

def take_monitor_screenshot(monitor, screen_width, screen_height):
    """Take a screenshot of a specific monitor using best available method"""
    if is_available('mss'):
        # Use mss for better multi-monitor support
        with mss() as sct:
            try:
                # Create monitor region with corrected dimensions
                monitor_region = {
                    "top": monitor['y'],
                    "left": monitor['x'], 
                    "width": screen_width,
                    "height": screen_height,
                }
                
                debug_log(f"MSS capturing region: {monitor_region}")
                
                # Take screenshot of specific region
                screenshot_data = sct.grab(monitor_region)
                # Convert to PIL Image
                screenshot = Image.frombytes("RGB", screenshot_data.size, screenshot_data.bgra, "raw", "BGRX")
                debug_log(f"Screenshot taken using mss: {screenshot.size[0]}x{screenshot.size[1]}")
                return screenshot, True  # True indicates we used mss
            except Exception as e:
                debug_log(f"mss failed, falling back to pyautogui: {e}")
    
    # Fallback to pyautogui (works for primary monitor, limited for secondary)
    screenshot = pyautogui.screenshot()
    debug_log(f"Screenshot taken using pyautogui: {screenshot.size[0]}x{screenshot.size[1]}")
    return screenshot, False  # False indicates we used pyautogui