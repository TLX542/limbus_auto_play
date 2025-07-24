import pyautogui
import keyboard
import time

# CONFIGURATION
screen_width, screen_height = pyautogui.size()
CHECK_ROW = screen_height - 279     # 279 pixels from the bottom
X_START = int(screen_width / 2)
X_END = screen_width

TARGET_COLOR = (59, 1, 0)           # RGB for #3B0100
SECONDARY_COLOR = (246, 175, 100)   # RGB for #F6AF64
TOLERANCE = 10                      # Adjust if needed
CHECK_INTERVAL = 2                  # Seconds between checks
SEARCH_AREA_SIZE = 50               # 50x50 pixel area around first color

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
    print("Script running. Press 'P' to stop.")
    while True:
        # Check for stop condition to exit
        if should_stop():
            break
            
        screenshot = pyautogui.screenshot()
        for x in range(X_START, X_END):
            pixel_color = screenshot.getpixel((x, CHECK_ROW))
            if color_match(pixel_color, TARGET_COLOR, TOLERANCE):
                # First color found, now check for secondary color in surrounding area
                if check_secondary_color(screenshot, x, CHECK_ROW):
                    print(f"Both colors found, Primary at ({x}, {CHECK_ROW}) with color {pixel_color}")
                    
                    # Save current cursor position
                    original_x, original_y = pyautogui.position()
                    
                    # Move cursor to the found location and left click
                    pyautogui.moveTo(x, CHECK_ROW)
                    time.sleep(0.1)  # Small delay to ensure cursor movement
                    pyautogui.click(x, CHECK_ROW)
                    time.sleep(0.1)  # Small delay after click
                    
                    # Press enter only
                    keyboard.press_and_release('enter')
                    time.sleep(0.1)
                    
                    # Restore cursor to original position
                    pyautogui.moveTo(original_x, original_y)
                    break
        
        # Interruptible sleep that can be stopped by key press
        if interruptible_sleep(CHECK_INTERVAL):
            break
            
    print("Stopped by key press.")
except KeyboardInterrupt:
    print("Stopped by user.")
except Exception as e:
    print(f"Exited with error: {e}")