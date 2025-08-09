import pyautogui
from .library_checker import is_available

# Import screeninfo if available
if is_available('screeninfo'):
    from screeninfo import get_monitors

def get_monitor_info():
    """Get information about all available monitors"""
    if not is_available('screeninfo'):
        # Fallback to primary monitor only
        screen_width, screen_height = pyautogui.size()
        return [{
            'index': 0,
            'name': 'Primary Monitor',
            'width': screen_width,
            'height': screen_height,
            'x': 0,
            'y': 0,
            'is_primary': True
        }]
    
    monitors = []
    for i, monitor in enumerate(get_monitors()):
        monitors.append({
            'index': i,
            'name': f"Monitor {i + 1}",
            'width': monitor.width,
            'height': monitor.height,
            'x': monitor.x,
            'y': monitor.y,
            'is_primary': monitor.is_primary
        })
    
    return monitors

def select_monitor():
    """Let user select which monitor to use"""
    monitors = get_monitor_info()
    
    if len(monitors) == 1:
        print(f"Using {monitors[0]['name']}: {monitors[0]['width']}x{monitors[0]['height']}")
        return monitors[0]
    
    print("\n====== Monitor Selection ======")
    for i, monitor in enumerate(monitors):
        status = " (Primary)" if monitor['is_primary'] else ""
        print(f"{i + 1}. {monitor['name']}: {monitor['width']}x{monitor['height']}{status}")
    
    while True:
        try:
            choice = input(f"\nSelect monitor (1-{len(monitors)}): ").strip()
            monitor_index = int(choice) - 1
            
            if 0 <= monitor_index < len(monitors):
                selected_monitor = monitors[monitor_index]
                print(f"Selected: {selected_monitor['name']} ({selected_monitor['width']}x{selected_monitor['height']})")
                return selected_monitor
            else:
                print(f"Please enter a number between 1 and {len(monitors)}")
        except ValueError:
            print("Please enter a valid number")

def get_monitor_resolution(monitor):
    """Get resolution for selected monitor, accounting for Windows DPI scaling"""
    print(f"\n====== Resolution Detection for {monitor['name']} ======")
    print("Windows DPI scaling can cause incorrect resolution detection.")
    print(f"Detected resolution: {monitor['width']}x{monitor['height']}")
    
    # Check for likely DPI scaling
    
    
    options = ["1920×1080 (Full HD)", "2560×1440 (QHD)", "3840×2160 (4K UHD)", "Custom resolution"]
    
    for i, option in enumerate(options):
        print(f"{i + 2}. {option}")
    
    max_option = len(options) + 1
    
    while True:
        try:
            choice = input(f"\nSelect option (1-{max_option}): ").strip()
            choice_num = int(choice)
            
            if choice_num == 1:
                return monitor['width'], monitor['height']
            elif choice_num == 2:
                return 1920, 1080
            elif choice_num == 3:
                return 2560, 1440
            elif choice_num == 4:
                return 3840, 2160
            elif choice_num == 5:
                return get_custom_resolution()
            elif choice_num == max_option:
                return get_custom_resolution()
            else:
                print(f"Please enter a number between 1 and {max_option}")
        except ValueError:
            print("Please enter a valid number")

def get_custom_resolution():
    """Get custom resolution from user input"""
    while True:
        try:
            resolution_input = input("Enter custom resolution (format: WIDTHxHEIGHT, e.g., 1550x900): ").strip()
            
            if 'x' not in resolution_input.lower():
                print("Please use format: WIDTHxHEIGHT (e.g., 1920x1080)")
                continue
            
            width_str, height_str = resolution_input.lower().split('x', 1)
            width = int(width_str.strip())
            height = int(height_str.strip())
            
            if width <= 0 or height <= 0:
                print("Width and height must be positive numbers")
                continue
            
            if width < 800 or height < 600:
                print("Warning: Very small resolution detected. Are you sure?")
                confirm = input("Continue? (y/n): ").strip().lower()
                if confirm not in ['y', 'yes']:
                    continue
            
            print(f"Custom resolution set: {width}x{height}")
            return width, height
            
        except ValueError:
            print("Invalid format. Please use WIDTHxHEIGHT (e.g., 1920x1080)")