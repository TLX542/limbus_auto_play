import time
import pyautogui
from logger import debug_log
from library_checker import is_available

# Get library availability
WINDOWS_MOUSE_AVAILABLE = is_available('windows_mouse')

if WINDOWS_MOUSE_AVAILABLE:
    import ctypes
    from ctypes import wintypes
    user32 = ctypes.windll.user32

def get_cursor_pos():
    """Get current cursor position using best available method"""
    if WINDOWS_MOUSE_AVAILABLE:
        point = wintypes.POINT()
        user32.GetCursorPos(ctypes.byref(point))
        return point.x, point.y
    else:
        return pyautogui.position()

def move_cursor(x, y, verify=False):
    """Move cursor to coordinates with optional verification"""
    debug_log(f"Moving cursor to ({x}, {y})")
    
    if WINDOWS_MOUSE_AVAILABLE:
        user32.SetCursorPos(int(x), int(y))
        if verify:
            time.sleep(0.05)
            actual_x, actual_y = get_cursor_pos()
            return abs(actual_x - x) <= 2 and abs(actual_y - y) <= 2
    else:
        pyautogui.moveTo(x, y, duration=0.1)
        if verify:
            actual_x, actual_y = get_cursor_pos()
            return abs(actual_x - x) <= 5 and abs(actual_y - y) <= 5
    
    return True

def click_at_position(x, y):
    """Perform a click at the specified position"""
    debug_log(f"Clicking at ({x}, {y})")
    
    if WINDOWS_MOUSE_AVAILABLE:
        # Move and verify position
        for attempt in range(3):
            user32.SetCursorPos(int(x), int(y))
            time.sleep(0.05)
            
            actual_x, actual_y = get_cursor_pos()
            if abs(actual_x - x) <= 2 and abs(actual_y - y) <= 2:
                break
        
        # Perform click
        user32.mouse_event(0x0002, 0, 0, 0, 0)  # MOUSEEVENTF_LEFTDOWN
        time.sleep(0.05)
        user32.mouse_event(0x0004, 0, 0, 0, 0)  # MOUSEEVENTF_LEFTUP
    else:
        pyautogui.moveTo(x, y, duration=0.1)
        time.sleep(0.1)
        pyautogui.click(x, y)

def ensure_cursor_on_monitor(monitor, x_offset=100, y_offset=100):
    """Ensure cursor is on the specified monitor"""
    current_x, current_y = get_cursor_pos()
    
    # Check if cursor is already on target monitor
    if (monitor['x'] <= current_x < monitor['x'] + monitor['width'] and
        monitor['y'] <= current_y < monitor['y'] + monitor['height']):
        return True
    
    # Move cursor to monitor
    target_x = max(monitor['x'], min(monitor['x'] + monitor['width'] - 1, monitor['x'] + x_offset))
    target_y = max(monitor['y'], min(monitor['y'] + monitor['height'] - 1, monitor['y'] + y_offset))
    
    debug_log(f"Moving cursor to monitor {monitor['name']} at ({target_x}, {target_y})")
    return move_cursor(target_x, target_y, verify=True)

def smart_click(x, y, target_monitor=None, force_cursor_to_monitor=False, restore_cursor=False):
    """
    Intelligent click function that handles multi-monitor setups
    
    Args:
        x, y: Click coordinates
        target_monitor: Monitor dict (optional)
        force_cursor_to_monitor: Whether to ensure cursor is on target monitor first
        restore_cursor: Whether to restore cursor position after click
    """
    original_pos = None
    if restore_cursor:
        original_pos = get_cursor_pos()
    
    # Ensure cursor is on target monitor if requested
    if force_cursor_to_monitor and target_monitor:
        if not ensure_cursor_on_monitor(target_monitor):
            debug_log("Warning: Could not reliably move cursor to target monitor")
    
    # Perform the click
    click_at_position(x, y)
    
    # Restore cursor position if requested
    if restore_cursor and original_pos:
        debug_log(f"Restoring cursor to original position: {original_pos}")
        move_cursor(original_pos[0], original_pos[1])
    elif target_monitor and not restore_cursor:
        # Move to safe position on target monitor
        safe_x = target_monitor['x'] + 25
        safe_y = target_monitor['y'] + 25
        move_cursor(safe_x, safe_y)